from pathlib import Path
import sys

import nbformat


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    notebooks_dir = root / "notebooks"
    notebooks = sorted(notebooks_dir.rglob("*.ipynb"))

    if not notebooks:
        print("No notebooks found.")
        return 1

    failed = []
    for nb_path in notebooks:
        try:
            with nb_path.open("r", encoding="utf-8") as f:
                nb = nbformat.read(f, as_version=4)
            nbformat.validate(nb)
            print(f"OK: {nb_path.relative_to(root)}")
        except Exception as exc:
            failed.append((nb_path, str(exc)))

    if failed:
        print("\nValidation errors:")
        for path, err in failed:
            print(f"- {path.relative_to(root)}: {err}")
        return 1

    print("\nAll notebooks are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
