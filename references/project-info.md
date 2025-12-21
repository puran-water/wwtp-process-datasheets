# Project Information

## Why Markdown as Source of Truth?

This skill follows [Puran Water's core principles](https://github.com/puran-water) for AI-native engineering tools:

| Principle | Benefit |
|-----------|---------|
| **LLM-native format** | Markdown is the native "word processor" for AI agents, enabling seamless reading/writing without parsing overhead |
| **Git version control** | Plain text templates are diffable—track changes, rollback errors, review PRs on engineering datasheets like code |
| **Machine-readable** | No binary blobs; all content is structured text that can be parsed, validated, and transformed programmatically |
| **Cross-platform** | Renders in GitHub, VS Code, Obsidian, and any text editor without proprietary software |
| **Client deliverable conversion** | When vendors require traditional formats, automated scripts convert markdown to professionally-styled Excel |

This inverts the traditional workflow where engineers fill Excel templates manually. Instead:
1. **AI agents** can read, populate, and validate markdown templates programmatically
2. **Engineers** review and approve in plain text with full git history
3. **Vendors** receive professional Excel datasheets generated from the version-controlled source

## Python Requirements

```bash
pip install openpyxl pyyaml
```

| Package | Version | Purpose |
|---------|---------|---------|
| openpyxl | >=3.0.0 | Excel file generation and manipulation |
| pyyaml | >=6.0.0 | YAML frontmatter parsing in templates |

Python 3.8+ required.

## License

Proprietary - Puran Water
