
import tempfile
import subprocess
from pathlib import Path

from studio.audio import AudioCue
from studio.audio_mixer import mix_audio


def main():
    with tempfile.TemporaryDirectory() as temp:
        folder = Path(temp)

        sound_one = folder / "sound_one.wav"
        sound_two = folder / "sound_two.wav"
        output = folder / "mixed_audio.wav"

        # Generate two temporary test sounds.
        for filename, frequency in [
            (sound_one, 440),
            (sound_two, 660)
        ]:
            subprocess.run([
                "ffmpeg", "-y",
                "-f", "lavfi",
                "-i", f"sine=frequency={frequency}:duration=1",
                "-c:a", "pcm_s16le",
                str(filename)
            ], check=True, capture_output=True)

        cues = [
            AudioCue(
                filename=str(sound_one),
                start=0,
                volume=0.5
            ),
            AudioCue(
                filename=str(sound_two),
                start=0.5,
                volume=0.5
            )
        ]

        result = mix_audio(
            cues,
            output,
            episode_duration=2
        )

        assert result.is_file()
        assert result.stat().st_size > 0

        print("Audio mixer test passed!")


if __name__ == "__main__":
    main()
