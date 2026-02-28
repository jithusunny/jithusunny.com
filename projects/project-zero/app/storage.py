from pathlib import Path
from datetime import datetime

RAW_DIR = Path(__file__).resolve().parent.parent.parent.parent / "raw"


def _parse_thought_path(txt_file: Path) -> dict | None:
    """Parse a thought file path into metadata. Returns None if path doesn't match expected structure."""
    try:
        rel = txt_file.relative_to(RAW_DIR)
    except ValueError:
        return None

    parts = rel.parts
    if len(parts) != 4 or parts[3] == "index.txt":
        return None

    year, month, day = parts[0], parts[1], parts[2]
    time_str = parts[3].replace(".txt", "")

    if len(time_str) != 4:
        return None

    try:
        dt = datetime(int(year), int(month), int(day), int(time_str[:2]), int(time_str[2:]))
    except (ValueError, IndexError):
        return None

    return {"rel_path": str(rel), "datetime": dt}


def list_thoughts() -> list[dict]:
    """Return all thoughts sorted newest first, with metadata and preview."""
    thoughts = []
    if not RAW_DIR.exists():
        return thoughts

    for txt_file in RAW_DIR.rglob("*.txt"):
        parsed = _parse_thought_path(txt_file)
        if parsed is None:
            continue

        content = txt_file.read_text(encoding="utf-8").strip()
        preview = content[:120]
        if len(content) > 120:
            preview += "…"

        thoughts.append({
            "path": parsed["rel_path"],
            "datetime": parsed["datetime"],
            "date_display": parsed["datetime"].strftime("%b %d, %Y · %I:%M %p"),
            "preview": preview,
        })

    thoughts.sort(key=lambda t: t["datetime"], reverse=True)
    return thoughts


def read_thought(rel_path: str) -> dict | None:
    """Read a single thought by its path relative to RAW_DIR."""
    file_path = RAW_DIR / rel_path
    if not file_path.exists() or not file_path.is_file():
        return None

    parsed = _parse_thought_path(file_path)
    if parsed is None:
        return None

    content = file_path.read_text(encoding="utf-8")

    return {
        "path": parsed["rel_path"],
        "datetime": parsed["datetime"],
        "date_display": parsed["datetime"].strftime("%b %d, %Y · %I:%M %p"),
        "content": content,
    }


def save_thought(content: str) -> str:
    """Save a new thought and return its path relative to RAW_DIR."""
    now = datetime.now()
    dir_path = RAW_DIR / now.strftime("%Y") / now.strftime("%m") / now.strftime("%d")
    dir_path.mkdir(parents=True, exist_ok=True)

    hour, minute = now.hour, now.minute

    while True:
        filename = f"{hour:02d}{minute:02d}.txt"
        file_path = dir_path / filename
        if not file_path.exists():
            break
        minute += 1
        if minute >= 60:
            minute = 0
            hour += 1

    file_path.write_text(content, encoding="utf-8")
    return str(file_path.relative_to(RAW_DIR))
