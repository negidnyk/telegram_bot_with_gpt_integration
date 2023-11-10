import asyncio
import logging
import sys
from bot.bot_config import start


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(start())


