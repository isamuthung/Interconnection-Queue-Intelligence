# src/caiso_queue/paths.py
from pathlib import Path

def get_repo_root() -> Path:
    """
    Returns the repository root path.

    Works whether the notebook is run from:
    - repo root, or
    - notebooks/ directory
    """
    root = Path.cwd()

    # Common case: notebook is executed with CWD = repo_root/notebooks
    if root.name == "notebooks":
        root = root.parent

    return root

def get_paths():
    """
    Returns common project paths:
    (ROOT, RAW, PROCESSED, OUTPUTS)

    Ensures PROCESSED and OUTPUTS exist.
    """
    root = get_repo_root()
    raw = root / "data" / "raw"
    processed = root / "data" / "processed"
    outputs = root / "outputs"

    processed.mkdir(parents=True, exist_ok=True)
    outputs.mkdir(parents=True, exist_ok=True)

    return root, raw, processed, outputs
