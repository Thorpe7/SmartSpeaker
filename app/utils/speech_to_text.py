""" Script running Whisper to convert speech to text. """

import logging
from pathlib import Path, PosixPath
import whisper

log = logging.getLogger(__name__)


def speech_to_text(audio_path: PosixPath) -> str:
    """Convert speech to text using Whisper.

    Args:
        audio_path (PosixPath): Path to audio file (.wav)

    Returns:
        str: Output text from speech-to-text conversion

    """
    model = whisper.load_model("base")
    result = model.transcribe(str(audio_path), fp16=False)
    return result["text"]


if __name__ == "__main__":
    speech_to_text(Path.cwd() / "audio_output.wav")
