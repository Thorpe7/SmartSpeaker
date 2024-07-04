""" Script for passing text to GPT & returning response. """

import os
import logging
from openai import OpenAI

log = logging.getLogger(__name__)

CLIENT = OpenAI(
    organization=os.getenv("OPENAI_ORG"),
    project=os.getenv("OPENAI_PROJ"),
    api_key=os.getenv("BUCKET_ID"),
)


def text_to_gpt(text: str) -> str:
    """Pass text to GPT & return response.

    Args:
        text (str): Input text to GPT

    Returns:
        str: Response from GPT

    """
    # Create a conversation thread object
    thread = CLIENT.beta.threads.create()

    # Create assistant object, previously created on OpenAI
    assistant = CLIENT.beta.assistants.retrieve(
        assistant_id=os.getenv("OPENAI_ASSISTANT_ID"),
    )

    # Add user message to the conversation thread
    message = CLIENT.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=text,
    )
    log.debug("User message: %s", message.data[0].content[0].text.value)

    # Add mechanism for streaming, current implementation w/o streaming
    # Create a run passing the assistant and the message thread
    run = CLIENT.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=assistant.id,
    )

    if run.status == "completed":
        messages = CLIENT.beta.threads.messages.list(thread_id=thread.id)
        bot_response = messages.data[0].content[0].text.value
        log.info("Bot response: %s", bot_response)

    else:
        bot_response = "There was an issue passing text to your assistant..."
        print(run.status)

    return bot_response


if __name__ == "__main__":
    text_to_gpt("Hello, what is your name?")
