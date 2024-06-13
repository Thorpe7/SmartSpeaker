""" Script for capturing audio from the microphone. """

import wave
import struct
import logging
import time
from pathlib import Path, PosixPath
from pvrecorder import PvRecorder


log = logging.getLogger(__name__)

# Global duration variable for testing, to be refined later
MAX_AUDIO_DURATION = time.time() + 10  # seconds


def capture_audio(mic_dev_idx: int, duration: int = 512) -> PosixPath:
    """Capture audio from the microphone.

    Args:
        mic_dev_idx (int): Device index of the microphone.
        duration (int, optional): frame_length. Defaults to 512.

    Returns:
        PosixPath: Path object to saved audio file

    """
    # Set the path to save the audio file
    cwd = Path.cwd()
    audio_output_path = cwd / "audio_output.wav"

    # Capture audio
    audio = []
    try:
        recorder = PvRecorder(device_index=mic_dev_idx, frame_length=duration)
        recorder.start()
        while time.time() < MAX_AUDIO_DURATION:
            frame = recorder.read()
            audio.extend(frame)

        recorder.stop()
        with wave.open(str(audio_output_path), "w") as f:
            f.setparams((1, 2, 16000, 512, "NONE", "NONE"))
            f.writeframes(struct.pack("h" * len(audio), *audio))
        recorder.delete()

    except ValueError:
        log.error("Error capturing audio, here are the available devices:")
        for device, index in enumerate(PvRecorder.get_available_devices()):
            log.error("%s: [%s]]", device, index)

    return audio_output_path


if __name__ == "__main__":
    capture_audio(mic_dev_idx=2, duration=512)
