"""Generate the static download catalog from files directly inside downloads/."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
directory = root / "downloads"
directory.mkdir(exist_ok=True)
files = [
    {"name": path.name, "size": path.stat().st_size}
    for path in sorted(directory.iterdir(), key=lambda path: path.name.casefold())
    if path.is_file() and not path.is_symlink()
    and not path.name.startswith(".")
]
(root / "downloadpage" / "files.json").write_text(
    json.dumps(files, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
print(f"Download catalog: {len(files)} files")
