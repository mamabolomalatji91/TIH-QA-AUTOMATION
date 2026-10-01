import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent

APP_PATH = PROJECT_ROOT / "app" / "index.html"

DEFAULT_APP_URL = APP_PATH.as_uri()

APP_URL = os.getenv("APP_URL", DEFAULT_APP_URL)

BASE_URL = APP_URL