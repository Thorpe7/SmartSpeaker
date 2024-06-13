""" Script containing the SmartSpeaker class. """

from .utils.capture_audio import capture_audio
from .utils.speech_to_text import speech_to_text


def main():
    """Main function for the smart speaker application."""
    # Capture audio
    audio_path = capture_audio(mic_dev_idx=2, duration=512)

    # Convert speech to text
    speech_to_text(audio_path)


if __name__ == "__main__":
    main()
