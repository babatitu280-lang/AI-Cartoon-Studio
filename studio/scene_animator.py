from pathlib import Path
import math

from studio.frame_renderer import render_character_frame


def render_scene_animation(
    background_path,
    character_path,
    keyframes,
    output_dir,
    duration,
    fps=24
):
    if duration <= 0:
        raise ValueError("Duration must be positive.")

    if fps <= 0:
        raise ValueError("FPS must be positive.")

    if not keyframes:
        raise ValueError("At least one keyframe is required.")

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    total_frames = math.ceil(duration * fps)
    rendered_frames = []

    for frame_number in range(total_frames):
        current_time = frame_number / fps

        output_path = (
            output_dir /
            f"frame_{frame_number + 1:06d}.png"
        )

        render_scene_animation_frame(
            background_path,
            character_path,
            keyframes,
            current_time,
            output_path
        )

        rendered_frames.append(output_path)

    return rendered_frames


def render_scene_animation_frame(
    background_path,
    character_path,
    keyframes,
    current_time,
    output_path
):
    return render_character_frame(
        background_path,
        character_path,
        keyframes,
        current_time,
        output_path
    )
