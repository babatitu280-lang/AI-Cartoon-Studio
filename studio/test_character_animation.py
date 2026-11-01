from studio.character_animation import (
    Keyframe,
    animate_character,
    create_walk_cycle
)


def main():
    frames = [
        Keyframe(0, 0, 0),
        Keyframe(2, 100, 0)
    ]

    middle = animate_character(frames, 1)

    assert 0 < middle["x"] < 100
    assert middle["y"] == 0

    walk = create_walk_cycle(
        start_x=0,
        end_x=200,
        start_time=0,
        duration=2
    )

    assert len(walk) == 3
    assert walk[0].x == 0
    assert walk[-1].x == 200

    final = animate_character(walk, 2)

    assert final["x"] == 200

    print("Character animation tests passed!")


if __name__ == "__main__":
    main()
