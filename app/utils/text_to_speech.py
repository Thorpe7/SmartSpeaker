""" Script for converting bot response to speech. """

import os
import logging
from pathlib import Path, PosixPath

from pydub import AudioSegment
from pydub.playback import play
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs

log = logging.getLogger(__name__)

CLIENT = ElevenLabs(
    api_key=os.getenv("ELEVEN_LABS_API"),
)


def text_to_speech(bot_response: str, output_path: PosixPath) -> None:
    """Convert bot response to speech & saves as audio file.

    Args:
        bot_response (str): Bot response text
        output_path (PosixPath): Path to save audio file (.wav)

    Returns:
        None

    """

    response = CLIENT.text_to_speech.convert(
        voice_id="G17SuINrv2H9FC6nvetn",
        optimize_streaming_latency="0",
        output_format="mp3_22050_32",
        text=bot_response,
        model_id="eleven_turbo_v2",
        voice_settings=VoiceSettings(
            stability=0.0,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
        ),
    )

    with open(output_path, "wb") as f:
        for chunk in response:
            f.write(chunk)

    log.info("Bot response converted to speech & saved as %s", output_path)

    play_sound(output_path)

    return output_path


def play_sound(file_path: PosixPath) -> None:
    """Play the audio file.

    Args:
        file_path (PosixPath): Path to audio file

    Returns:
        None

    """
    audio_output = AudioSegment.from_mp3(file_path)
    play(audio_output)


if __name__ == "__main__":
    text_to_speech("Hello, my name is Bucket", Path.cwd() / "bot_audio.mp3")
    play_sound(Path.cwd() / "bot_audio.mp3")
