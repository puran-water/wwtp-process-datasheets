#!/usr/bin/env python3
"""
Generate Bill of Materials (BOM) from a filled package template.

This script reads a populated package datasheet and its corresponding BOM
definition file to generate a list of component datasheets required for
the RFQ package.

Usage:
    python generate_bom.py <package_template.md> [--output <output_file>]

Example:
    python generate_bom.py filled/101-SC_project.md --output bom_101-SC.csv

Supported qty_rule expressions:
    - Single field: "num_screens"
    - Addition: "num_trains + 1"
    - Multiplication: "num_vessels * 2"
    - Combined: "num_basins * units_per_basin + 1"
    - Fixed: "fixed" (uses 'qty' field)
    - Conditional: "conditional" (uses 'condition_field' and 'condition_value')
"""

import argparse
import csv
import operator
import re
import sys
from pathlib import Path

import yaml


# =============================================================================
# EXPRESSION PARSING
# =============================================================================

# Supported operators for safe expression evaluation
OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,  # Integer division for quantities
}


def tokenize_expression(expr: str) -> list[str]:
    """
    Tokenize an arithmetic expression into operands and operators.

    Example: "num_trains + 1" -> ["num_trains", "+", "1"]
    """
    # Split on operators while keeping them
    tokens = re.split(r'\s*([+\-*/])\s*', expr.strip())
    return [t.strip() for t in tokens if t.strip()]


def evaluate_expression(expr: str, field_values: dict) -> int:
    """
    Safely evaluate an arithmetic expression using field values.

    Supports: field names, integers, +, -, *, /

    Examples:
        "num_trains" -> field_values['num_trains']
        "num_trains + 1" -> field_values['num_trains'] + 1
        "num_basins * 2" -> field_values['num_basins'] * 2
        "num_vessels * units_per_vessel + 1" -> calculated result
    """
    tokens = tokenize_expression(expr)

    if not tokens:
        return 1

    # Convert tokens to values
    values = []
    ops = []

    for token in tokens:
        if token in OPERATORS:
            ops.append(token)
        else:
            # Try to resolve as field name first, then as integer
            if token in field_values:
                try:
                    val = int(float(field_values[token])) if field_values[token] else 0
                except (ValueError, TypeError):
                    val = 0
            else:
                try:
                    val = int(token)
                except ValueError:
                    # Unknown field or invalid token - default to 0
                    val = 0
            values.append(val)

    if not values:
        return 1

    # Evaluate left-to-right with proper operator precedence
    # Handle multiplication/division first
    i = 0
    while i < len(ops):
        if ops[i] in ('*', '/'):
            # Guard against division by zero
            if ops[i] == '/' and values[i + 1] == 0:
                return 0  # Division by zero yields 0 quantity
            result = OPERATORS[ops[i]](values[i], values[i + 1])
            values = values[:i] + [result] + values[i + 2:]
            ops = ops[:i] + ops[i + 1:]
        else:
            i += 1

    # Then handle addition/subtraction
    result = values[0] if values else 0
    for i, op in enumerate(ops):
        if i + 1 < len(values):
            result = OPERATORS[op](result, values[i + 1])

    return max(0, result)  # Never return negative quantities


# =============================================================================
# TEMPLATE PARSING
# =============================================================================

def parse_frontmatter(content: str) -> dict:
    """Extract YAML frontmatter from markdown content."""
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return {}
    try:
        return yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        return {}


def extract_field_values(content: str) -> dict:
    """Extract field_id -> value mappings from the template."""
    values = {}

    # Find all tables with field_id column
    table_pattern = r'\|[^\n]*field_id[^\n]*\|.*?\n\|[-|\s]+\|\n((?:\|[^\n]+\|\n)+)'

    for match in re.finditer(table_pattern, content, re.IGNORECASE):
        table_rows = match.group(1)
        for row in table_rows.strip().split('\n'):
            cells = [c.strip() for c in row.split('|')[1:-1]]
            if len(cells) >= 4:
                # Format: | # | field_id | Field | Value | Units | ...
                field_id = cells[1].strip()
                value = cells[3].strip() if len(cells) > 3 else ''
                if field_id and field_id != 'field_id':
                    values[field_id] = value

    return values


# =============================================================================
# BOM PROCESSING
# =============================================================================

def load_bom_definition(template_id: str, components_dir: Path) -> dict | None:
    """Load BOM definition file for a package template."""
    bom_file = components_dir / f'bom_{template_id}.yaml'
    if not bom_file.exists():
        return None

    try:
        with open(bom_file, 'r') as f:
            return yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(f"Error parsing BOM definition: {e}", file=sys.stderr)
        return None


def evaluate_condition(field_values: dict, condition_field: str, condition_value: str) -> bool:
    """Evaluate a conditional rule against field values."""
    actual_value = field_values.get(condition_field, '')

    # Handle comparison operators
    if condition_value.startswith('>'):
        try:
            threshold = float(condition_value[1:].strip())
            return float(actual_value) > threshold if actual_value else False
        except (ValueError, TypeError):
            return False
    elif condition_value.startswith('<'):
        try:
            threshold = float(condition_value[1:].strip())
            return float(actual_value) < threshold if actual_value else False
        except (ValueError, TypeError):
            return False
    elif condition_value.startswith('!='):
        return actual_value.lower() != condition_value[2:].strip().lower()
    else:
        # Direct comparison (case-insensitive, also checks if value contains the condition)
        return (actual_value.lower() == condition_value.lower() or
                condition_value.lower() in actual_value.lower())


def calculate_quantity(component: dict, field_values: dict) -> int:
    """Calculate component quantity based on rules and field values."""
    qty_rule = component.get('qty_rule', 'fixed')

    if qty_rule == 'fixed':
        return component.get('qty', 1)

    elif qty_rule == 'conditional':
        condition_field = component.get('condition_field', '')
        condition_value = component.get('condition_value', '')

        if not evaluate_condition(field_values, condition_field, condition_value):
            return 0

        # If condition met, evaluate qty_rule_value as expression or use qty
        qty_rule_value = component.get('qty_rule_value')
        if qty_rule_value:
            return evaluate_expression(str(qty_rule_value), field_values)
        return component.get('qty', 1)

    else:
        # qty_rule is an expression (field name, arithmetic, etc.)
        return evaluate_expression(qty_rule, field_values)


def generate_bom(template_path: Path, components_dir: Path) -> list[dict]:
    """Generate BOM from a filled package template."""
    # Read template
    with open(template_path, 'r') as f:
        content = f.read()

    # Parse frontmatter to get template_id
    frontmatter = parse_frontmatter(content)
    template_id = frontmatter.get('template_id', '')

    if not template_id:
        print(f"Error: No template_id found in {template_path}", file=sys.stderr)
        return []

    # Load BOM definition
    bom_def = load_bom_definition(template_id, components_dir)
    if not bom_def:
        print(f"No BOM definition found for {template_id}", file=sys.stderr)
        return []

    # Extract field values from template
    field_values = extract_field_values(content)

    # Generate component list
    bom_items = []
    for component in bom_def.get('components', []):
        qty = calculate_quantity(component, field_values)

        if qty > 0:
            bom_items.append({
                'template_id': component.get('template_id', ''),
                'name': component.get('name', ''),
                'quantity': qty,
                'service': component.get('service', ''),
                'description': component.get('description', '')
            })

    return bom_items


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description='Generate BOM from a filled package template'
    )
    parser.add_argument(
        'template',
        type=Path,
        help='Path to the filled package template'
    )
    parser.add_argument(
        '--output', '-o',
        type=Path,
        help='Output file (CSV format). Prints to stdout if not specified.'
    )
    parser.add_argument(
        '--components-dir',
        type=Path,
        default=Path(__file__).parent.parent / 'components',
        help='Path to components directory containing BOM definitions'
    )

    args = parser.parse_args()

    if not args.template.exists():
        print(f"Error: Template file not found: {args.template}", file=sys.stderr)
        sys.exit(1)

    # Generate BOM
    bom_items = generate_bom(args.template, args.components_dir)

    if not bom_items:
        print("No components found or no BOM definition available.", file=sys.stderr)
        sys.exit(0)

    # Output results
    fieldnames = ['template_id', 'name', 'quantity', 'service', 'description']

    if args.output:
        with open(args.output, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(bom_items)
        print(f"BOM written to {args.output}")
    else:
        # Print to stdout as formatted table
        print("\n" + "=" * 80)
        print("BILL OF MATERIALS")
        print("=" * 80)
        print(f"{'Template':<15} {'Component':<25} {'Qty':>5} {'Service':<20}")
        print("-" * 80)
        for item in bom_items:
            print(f"{item['template_id']:<15} {item['name']:<25} {item['quantity']:>5} {item['service']:<20}")
        print("=" * 80)
        print(f"Total component datasheets required: {len(bom_items)}")


if __name__ == '__main__':
    main()
