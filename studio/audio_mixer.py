
from pathlib import Path
import subprocess


def mix_audio(
    audio_cues,
    output_path,
    episode_duration,
    sample_rate=44100
):
    """
    Combine timed audio clips into one episode audio track.

    Each cue must contain:
    filename, start, volume
    """

    if episode_duration <= 0:
        raise ValueError("Episode duration must be positive.")

    if sample_rate <= 0:
        raise ValueError("Sample rate must be positive.")

    if not audio_cues:
        raise ValueError("No audio cues supplied.")

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    command = ["ffmpeg", "-y"]

    for cue in audio_cues:
        filename = Path(cue.filename)

        if not filename.is_file():
            raise FileNotFoundError(
                f"Audio file not found: {filename}"
            )

        if cue.start < 0 or cue.start >= episode_duration:
            raise ValueError("Audio cue starts outside episode.")

        if not 0 <= cue.volume <= 1:
            raise ValueError("Audio volume must be between 0 and 1.")

        command.extend(["-i", str(filename)])

    filters = []

    for index, cue in enumerate(audio_cues):
        delay_ms = round(cue.start * 1000)

        filters.append(
            f"[{index}:a]"
            f"volume={cue.volume},"
            f"adelay={delay_ms}|{delay_ms},"
            f"apad,"
            f"atrim=duration={episode_duration}"
            f"[a{index}]"
        )

    inputs = "".join(
        f"[a{index}]"
        for index in range(len(audio_cues))
    )

    filters.append(
        f"{inputs}amix=inputs={len(audio_cues)}:"
        f"duration=longest:normalize=0,"
        f"alimiter=limit=0.95,"
        f"atrim=duration={episode_duration}[out]"
    )

    command.extend([
        "-filter_complex", ";".join(filters),
        "-map", "[out]",
        "-ar", str(sample_rate),
        "-c:a", "aac",
        "-b:a", "192k",
        str(output_path)
    ])

    subprocess.run(command, check=True)

    if not output_path.is_file() or output_path.stat().st_size == 0:
        raise RuntimeError("Audio mixing failed.")

    return output_path
