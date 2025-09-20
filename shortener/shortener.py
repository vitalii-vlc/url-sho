from validators import url as is_valid_url, ValidationError
from secrets import token_urlsafe

from common.config import SHORT_URL_KEY_LENGTH, SHORTENER_URL_PREFIX
from common.schemas import ShortUrl
from shortener.storage import StorageProtocol


class URLShortener:
    def __init__(self, storage: StorageProtocol):
        self.storage = storage
        self.url_object = None

    def save(self):
        if not self.url_object:
            raise Exception('No URL object to save')
        self.storage.set(self.url_object.model_dump())

    def shorten(self, url: str):
        if isinstance(is_valid_url(url), ValidationError):
            raise ValueError(f'Invalid URL: {url}')

        key = token_urlsafe(SHORT_URL_KEY_LENGTH)
        short_url = f"{SHORTENER_URL_PREFIX}{key}"
        self.url_object = ShortUrl(long_url=url, short_url=short_url, key=key)
        self.save()
        return self.url_object
