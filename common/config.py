import os

SHORT_URL_KEY_LENGTH = int(os.environ.get("SHORT_URL_KEY_LENGTH", 6))
SHORTENER_URL_PREFIX = os.environ.get("SHORTENER_URL_PREFIX")
