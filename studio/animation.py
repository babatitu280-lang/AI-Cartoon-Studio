# AI Cartoon Studio
# Core 2D animation calculations

import math


def clamp(value, minimum=0.0, maximum=1.0):
    return max(minimum, min(value, maximum))


def linear(t):
    return clamp(t)


def ease_in(t):
    t = clamp(t)
    return t * t


def ease_out(t):
    t = clamp(t)
    return 1 - (1 - t) ** 2


def ease_in_out(t):
    t = clamp(t)
    return 3 * t**2 - 2 * t**3


def interpolate(start, end, progress):
    progress = clamp(progress)
    return start + (end - start) * progress


def bounce(progress, height=30, bounces=2):
    progress = clamp(progress)
    return abs(math.sin(progress * math.pi * bounces)) * height


def animate_position(start, end, progress):
    return (
        interpolate(start[0], end[0], ease_in_out(progress)),
        interpolate(start[1], end[1], ease_in_out(progress))
    )


def animate_rotation(progress, degrees=360):
    return interpolate(0, degrees, ease_in_out(progress))
