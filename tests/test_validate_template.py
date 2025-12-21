#!/usr/bin/env python3
"""
Tests for validate_template.py

Run with: pytest tests/test_validate_template.py -v
"""

import sys
from pathlib import Path

# Add scripts directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

import pytest
from validate_template import (
    parse_frontmatter,
    find_sections,
    validate_table_structure,
    validate_field_types,
    validate_field_id_uniqueness,
    extract_field_ids,
    validate_template,
    REQUIRED_FRONTMATTER,
    VALID_FIELD_TYPES,
    DATA_TABLE_COLUMNS,
)


FIXTURES_DIR = Path(__file__).parent / 'fixtures'


class TestParseFrontmatter:
    """Tests for YAML frontmatter parsing."""

    def test_valid_frontmatter(self):
        content = """---
schema_version: 1
template_id: TEST-01
title: TEST EQUIPMENT
service: TEST SERVICE
has_motor: true
---
# Body content
"""
        fm, end_line, errors = parse_frontmatter(content)

        assert fm['schema_version'] == 1
        assert fm['template_id'] == 'TEST-01'
        assert fm['title'] == 'TEST EQUIPMENT'
        assert fm['has_motor'] is True
        assert not any(e.severity == 'ERROR' for e in errors)

    def test_missing_frontmatter(self):
        content = "# No frontmatter here"
        fm, end_line, errors = parse_frontmatter(content)

        assert fm == {}
        assert any('Missing YAML frontmatter' in e.message for e in errors)

    def test_unclosed_frontmatter(self):
        content = """---
schema_version: 1
template_id: TEST-01
# Missing closing ---
"""
        fm, end_line, errors = parse_frontmatter(content)

        assert any('Unclosed YAML frontmatter' in e.message for e in errors)

    def test_missing_required_fields(self):
        content = """---
schema_version: 1
---
# Missing required fields
"""
        fm, end_line, errors = parse_frontmatter(content)

        error_msgs = [e.message for e in errors]
        assert any('template_id' in msg for msg in error_msgs)
        assert any('title' in msg for msg in error_msgs)
        assert any('service' in msg for msg in error_msgs)
        assert any('has_motor' in msg for msg in error_msgs)


class TestFindSections:
    """Tests for section detection."""

    def test_find_sections(self):
        content = """# Title

## Document Control

Some content

## Operating / Design Data

More content

## Materials

Material content
"""
        sections = find_sections(content)

        assert 'Document Control' in sections
        assert 'Operating / Design Data' in sections
        assert 'Materials' in sections

    def test_empty_content(self):
        sections = find_sections("")
        assert sections == {}


class TestValidateTableStructure:
    """Tests for table structure validation."""

    def test_valid_table(self):
        table = """| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | flow | Flow Rate | 100 | m3/h | number | |
"""
        errors = validate_table_structure(table, DATA_TABLE_COLUMNS, 'Test', 1)
        assert not any(e.severity == 'ERROR' for e in errors)

    def test_missing_columns(self):
        table = """| Field | Value |
|-------|-------|
| Flow | 100 |
"""
        errors = validate_table_structure(table, DATA_TABLE_COLUMNS, 'Test', 1)
        # Should warn about missing columns
        assert any('columns' in e.message.lower() for e in errors)

    def test_empty_table(self):
        errors = validate_table_structure("", DATA_TABLE_COLUMNS, 'Test', 1)
        assert any('No table found' in e.message for e in errors)


class TestValidateFieldTypes:
    """Tests for field type validation."""

    def test_valid_field_types(self):
        table = """| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | flow | Flow Rate | 100 | m3/h | number | |
| 2 | name | Name | test | | text | |
| 3 | mode | Mode | | | dropdown | ["A","B"] |
"""
        errors = validate_field_types(table, 'Test', 1)
        assert not any(e.severity == 'ERROR' for e in errors)

    def test_invalid_field_type(self):
        table = """| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | flow | Flow Rate | 100 | m3/h | badtype | |
"""
        errors = validate_field_types(table, 'Test', 1)
        assert any('Invalid field type' in e.message for e in errors)

    def test_invalid_dropdown_options(self):
        table = """| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | mode | Mode | | | dropdown | not-json |
"""
        errors = validate_field_types(table, 'Test', 1)
        assert any('dropdown' in e.message.lower() for e in errors)


class TestExtractFieldIds:
    """Tests for field ID extraction."""

    def test_extract_field_ids(self):
        table = """| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | flow_in | Inlet Flow | | m3/h | number | |
| 2 | flow_out | Outlet Flow | | m3/h | number | |
"""
        field_ids = extract_field_ids(table, 'Test', 1)

        ids = [fid for fid, _, _ in field_ids]
        assert 'flow_in' in ids
        assert 'flow_out' in ids


class TestValidateFieldIdUniqueness:
    """Tests for field ID uniqueness validation."""

    def test_unique_field_ids(self):
        sections = {
            'Operating / Design Data': (10, """
| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | flow | Flow | | m3/h | number | |
| 2 | pressure | Pressure | | bar | number | |
"""),
            'Materials': (30, """
| # | field_id | Component | Material |
|---|----------|-----------|----------|
| 1 | tank | Tank | SS |
"""),
        }
        errors = validate_field_id_uniqueness(sections)
        assert not any('Duplicate' in e.message for e in errors)

    def test_duplicate_field_ids(self):
        sections = {
            'Operating / Design Data': (10, """
| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | flow | Flow A | | m3/h | number | |
| 2 | flow | Flow B | | m3/h | number | |
"""),
        }
        errors = validate_field_id_uniqueness(sections)
        assert any('Duplicate field_id' in e.message for e in errors)


class TestValidateTemplate:
    """Integration tests for full template validation."""

    def test_valid_template(self):
        filepath = FIXTURES_DIR / 'valid_template.md'
        passed, errors = validate_template(filepath)

        # Print errors for debugging
        for e in errors:
            if e.severity == 'ERROR':
                print(f"Unexpected error: {e}")

        assert passed, f"Valid template should pass. Errors: {[str(e) for e in errors]}"

    def test_invalid_template(self):
        filepath = FIXTURES_DIR / 'invalid_template.md'
        passed, errors = validate_template(filepath)

        assert not passed, "Invalid template should fail"

        # Check for expected errors
        error_msgs = ' '.join(e.message for e in errors)
        assert 'Duplicate field_id' in error_msgs or 'duplicate' in error_msgs.lower()
        assert 'Invalid field type' in error_msgs or 'badtype' in error_msgs.lower()

    def test_missing_file(self):
        filepath = FIXTURES_DIR / 'nonexistent.md'
        passed, errors = validate_template(filepath)

        assert not passed
        assert any('not found' in e.message.lower() for e in errors)


class TestConstants:
    """Tests for validation constants."""

    def test_required_frontmatter_fields(self):
        required = set(REQUIRED_FRONTMATTER.keys())
        expected = {'schema_version', 'template_id', 'title', 'service', 'has_motor'}
        assert required == expected

    def test_valid_field_types(self):
        expected = ['number', 'text', 'dropdown', 'date', 'readonly']
        assert set(VALID_FIELD_TYPES) == set(expected)


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
