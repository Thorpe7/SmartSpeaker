""" Script containing the SmartSpeaker class. """

import logging

from .utils.capture_audio import capture_audio
from .utils.speech_to_text import speech_to_text
from .utils.text_to_gpt import text_to_gpt
from .utils.text_to_speech import text_to_speech

log = logging.getLogger(__name__)


def main():
    """Main function for the smart speaker application."""
    # Capture audio
    audio_path = capture_audio(mic_dev_idx=0, duration=512)  # 2 for linux mic

    # Convert speech to text
    text = speech_to_text(audio_path)

    # Pass text to GPT
    bot_response = text_to_gpt(text)

    # Pass response to text-to-speech
    bot_response_file = text_to_speech(bot_response, output_path="bot_response.mp3")

    return bot_response_file


if __name__ == "__main__":
    main()
