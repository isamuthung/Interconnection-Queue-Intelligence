from pathlib import Path

def get_repo_root() -> Path:
    root = Path.cwd()
    if root.name == "notebooks":
        root = root.parent
    return root

def get_paths():
    root = get_repo_root()
    raw = root / "data" / "raw"
    processed = root / "data" / "processed"
    outputs = root / "outputs"

    processed.mkdir(parents=True, exist_ok=True)
    outputs.mkdir(parents=True, exist_ok=True)

    return root, raw, processed, outputs
