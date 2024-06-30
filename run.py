""" Run script for calling smart speaker application. """

import logging

from app.smart_speaker import main

logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler()])
log = logging.getLogger(__name__)


if __name__ == "__main__":
    main()
