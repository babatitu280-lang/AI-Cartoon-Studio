# AI Cartoon Studio
# Permanent reusable asset library

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

ASSETS_DIR = PROJECT_ROOT / "assets"

CHARACTER_ASSETS = {
    "bobo": {
        "folder": ASSETS_DIR / "characters" / "bobo",
        "design_status": "provisional",
    },
    "rexy": {
        "folder": ASSETS_DIR / "characters" / "rexy",
        "design_status": "provisional",
    },
}


def get_character_folder(name):
    name = name.lower()

    if name not in CHARACTER_ASSETS:
        raise ValueError(f"Unknown character: {name}")

    return CHARACTER_ASSETS[name]["folder"]


def get_character_asset(name, asset_name):
    folder = get_character_folder(name)
    asset_path = folder / asset_name

    if not asset_path.is_file():
        raise FileNotFoundError(
            f"Character asset not found: {asset_path}"
        )

    return asset_path


def list_character_assets(name):
    folder = get_character_folder(name)

    if not folder.exists():
        return []

    return sorted(
        path for path in folder.iterdir()
        if path.is_file()
    )
