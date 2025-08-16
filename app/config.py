import os

from dotenv import load_dotenv
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

is_dotenv_loaded = load_dotenv()
print(f"Is dotenv loaded? {is_dotenv_loaded}")

DEBUG = os.getenv("DEBUG", False)
if not DEBUG:
    print("Not in debug mode")
