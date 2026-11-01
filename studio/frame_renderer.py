from pathlib import Path
from PIL import Image

from studio.character_animation import animate_character


def render_character_frame(
    background_path,
    character_path,
    keyframes,
    current_time,
    output_path
):
    background = Image.open(background_path).convert("RGBA")
    character = Image.open(character_path).convert("RGBA")

    motion = animate_character(keyframes, current_time)

    width = max(1, round(character.width * motion["scale_x"]))
    height = max(1, round(character.height * motion["scale_y"]))

    character = character.resize(
        (width, height),
        Image.Resampling.LANCZOS
    )

    character = character.rotate(
        motion["rotation"],
        resample=Image.Resampling.BICUBIC,
        expand=True
    )

    x = round(motion["x"])
    y = round(motion["y"])

    background.alpha_composite(character, (x, y))

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    background.save(output_path, "PNG")

    return output_path
