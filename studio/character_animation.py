from dataclasses import dataclass
from studio.animation import (
    ease_in_out,
    interpolate,
    bounce,
)


@dataclass
class Keyframe:
    time: float
    x: float
    y: float
    rotation: float = 0.0
    scale_x: float = 1.0
    scale_y: float = 1.0


def animate_character(keyframes, current_time):
    if not keyframes:
        raise ValueError("At least one keyframe is required.")

    keyframes = sorted(keyframes, key=lambda frame: frame.time)

    if current_time <= keyframes[0].time:
        frame = keyframes[0]
        return frame.__dict__.copy()

    if current_time >= keyframes[-1].time:
        frame = keyframes[-1]
        return frame.__dict__.copy()

    for start, end in zip(keyframes, keyframes[1:]):
        if start.time <= current_time <= end.time:
            duration = end.time - start.time
            progress = (current_time - start.time) / duration
            progress = ease_in_out(progress)

            return {
                "time": current_time,
                "x": interpolate(start.x, end.x, progress),
                "y": interpolate(start.y, end.y, progress),
                "rotation": interpolate(
                    start.rotation, end.rotation, progress
                ),
                "scale_x": interpolate(
                    start.scale_x, end.scale_x, progress
                ),
                "scale_y": interpolate(
                    start.scale_y, end.scale_y, progress
                ),
            }

    raise RuntimeError("Animation interpolation failed.")


def create_walk_cycle(start_x, end_x, start_time, duration):
    if duration <= 0:
        raise ValueError("Duration must be positive.")

    return [
        Keyframe(start_time, start_x, 0, rotation=-3),
        Keyframe(
            start_time + duration / 2,
            (start_x + end_x) / 2,
            -12,
            rotation=3,
            scale_x=1.03,
            scale_y=0.97
        ),
        Keyframe(start_time + duration, end_x, 0)
          ]
