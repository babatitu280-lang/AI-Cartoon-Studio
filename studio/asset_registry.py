from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CHARACTER_ROOT = PROJECT_ROOT / "assets" / "characters"

CHARACTER_ASSETS = {
    "bobo": CHARACTER_ROOT / "bobo",
    "rexy": CHARACTER_ROOT / "rexy",
}

def get_character_folder(name):
    name = name.lower()

    if name not in CHARACTER_ASSETS:
        raise ValueError(f"Unknown character: {name}")

    return CHARACTER_ASSETS[name]

def get_character_asset(name, filename):
    folder = get_character_folder(name)
    asset = folder / filename

    if not asset.is_file():
        raise FileNotFoundError(
            f"Character asset not found: {asset}"
        )

    return asset

def list_character_assets(name):
    folder = get_character_folder(name)

    if not folder.exists():
        return []

    return sorted(
        file.name for file in folder.iterdir()
        if file.is_file()
  )
