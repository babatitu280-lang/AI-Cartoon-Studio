from pathlib import Path
from PIL import Image


def load_character_image(path):
    """Load a transparent 2D character image."""
    path = Path(path)

    if not path.is_file():
        raise FileNotFoundError(
            f"Character image not found: {path}"
        )

    image = Image.open(path).convert("RGBA")

    if image.width == 0 or image.height == 0:
        raise ValueError("Character image is empty.")

    return image


def resize_character(image, height):
    """Resize a character while preserving its proportions."""
    if height <= 0:
        raise ValueError("Height must be positive.")

    ratio = height / image.height
    width = round(image.width * ratio)

    return image.resize(
        (width, height),
        Image.Resampling.LANCZOS
    )


def composite_scene(
    background_path,
    character_layers,
    output_path
):
    """
    Place transparent 2D characters over a 3D background.

    character_layers example:
    [
        {
            "path": "assets/characters/bobo/idle.png",
            "x": 500,
            "y": 400,
            "height": 350
        }
    ]
    """

    background_path = Path(background_path)
    output_path = Path(output_path)

    if not background_path.is_file():
        raise FileNotFoundError(
            f"Background not found: {background_path}"
        )

    scene = Image.open(background_path).convert("RGBA")

    for layer in character_layers:
        character = load_character_image(layer["path"])

        character = resize_character(
            character,
            int(layer["height"])
        )

        x = int(layer["x"])
        y = int(layer["y"])

        scene.alpha_composite(character, (x, y))

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    scene.save(output_path, "PNG")

    return output_path
