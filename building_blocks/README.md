# Building Blocks

Reusable code blocks organized by language. Each block is a standalone capability with no project-specific logic.

## Structure

```
building_blocks/
├── python/     # Python modules (e.g., file storage, pagination)
├── html/       # HTML templates / patterns
├── js/         # JavaScript utilities
├── css/        # CSS patterns / components
```

## Per block

Each building block lives in its own folder inside the language directory:

```
python/my_block/
├── README.md   # What it is, how to use it, 1-2 examples
├── ...         # Code files
```

## Rules

- No project-specific code. Blocks must work across diverse projects.
- Each block has a precise, succinct README.
- Prefer standalone blocks. If blocks must be used together, note the dependency in the README.
- Planners check this library before defining tasks — reuse before creating new.
