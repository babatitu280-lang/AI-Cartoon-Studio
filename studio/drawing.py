from PIL import Image, ImageDraw


def create_frame(width=1920, height=1080):
    image = Image.new("RGB", (width, height), "#B9E5FF")
    draw = ImageDraw.Draw(image)

    # Ground
    draw.rectangle(
        (0, height * 0.75, width, height),
        fill="#79B85A"
    )

    return image


def draw_character(image, character, x, y, scale=1.0):
    draw = ImageDraw.Draw(image)

    if character == "bobo":
        body_color = "#F4B52E"
        belly_color = "#F7D58A"
        spike_color = "#79502E"
        radius = int(95 * scale)
    elif character == "rexy":
        body_color = "#9655C9"
        belly_color = "#C99AE8"
        spike_color = "#60358C"
        radius = int(65 * scale)
    else:
        raise ValueError("Unknown character")

    # Body
    draw.ellipse(
        (x - radius, y - radius, x + radius, y + radius),
        fill=body_color,
        outline="#30243B",
        width=max(2, int(5 * scale))
    )

    # Belly
    draw.ellipse(
        (
            x - radius * 0.55,
            y - radius * 0.05,
            x + radius * 0.55,
            y + radius * 0.75
        ),
        fill=belly_color
    )

    # Eye
    eye_radius = max(3, int(9 * scale))
    draw.ellipse(
        (
            x + radius * 0.25,
            y - radius * 0.35,
            x + radius * 0.25 + eye_radius * 2,
            y - radius * 0.35 + eye_radius * 2
        ),
        fill="white",
        outline="#30243B"
    )

    # Spike
    draw.polygon(
        [
            (x - radius * 0.4, y - radius * 0.8),
            (x - radius * 0.1, y - radius * 1.4),
            (x + radius * 0.1, y - radius * 0.7)
        ],
        fill=spike_color,
        outline="#30243B"
    )

    return image


def create_test_frame(output_path="test_frame.png"):
    image = create_frame()
    draw_character(image, "bobo", 650, 650, 1.0)
    draw_character(image, "rexy", 1050, 650, 0.8)
    image.save(output_path)
    return output_path
