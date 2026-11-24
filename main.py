"""One-Liner Laugh Lab entry — robot vacuum excuse after eating a sock.

Writes one short funny line to /output/entry.txt for the make.fun judge.
The line is the excuse a robot vacuum gives after eating a sock.
"""

from pathlib import Path

# Final winning line — deadpan machine-voice turn at the END.
ENTRY_LINE = "Sock ingested. Suction optimal. Returning to dock. Mission accomplished."

# Gate checks: UTF-8 text, 1–200 characters, not only whitespace, single line.
assert 1 <= len(ENTRY_LINE) <= 200, f"Entry must be 1–200 characters, got {len(ENTRY_LINE)}"
assert "\n" not in ENTRY_LINE, "Entry must be a single line (no newlines)"
assert ENTRY_LINE.strip(), "Entry must not be only whitespace"

# Write to /output/entry.txt, creating the directory if needed.
output_dir = Path("/output")
output_dir.mkdir(parents=True, exist_ok=True)
output_path = output_dir / "entry.txt"
output_path.write_text(ENTRY_LINE, encoding="utf-8")

print(ENTRY_LINE)