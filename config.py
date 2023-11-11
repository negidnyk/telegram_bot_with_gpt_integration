from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.environ.get("BOT_TOKEN")
OPENAI_KEY = os.environ.get("OPENAI_KEY")
