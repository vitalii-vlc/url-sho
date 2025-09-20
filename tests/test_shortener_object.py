import pytest

from common.config import SHORT_URL_KEY_LENGTH
from shortener.shortener import URLShortener
from shortener.storage import FakeStorage


class TestShortenerController:
    shortener = URLShortener(storage=FakeStorage())

    @pytest.mark.parametrize(
        "url_config",
        [{
            "url": "https://example.com",
            "exception": None
        },
        {
            "url": "https://example.com/path/to/resource",
            "exception": None
        },
        {
            "url": "https://example.com?query=to-resource",
            "exception": None
        },
        {
            "url": "https://example.com/path/to/resource?query=to-resource",
            "exception": None
        },
        {
            "url": "invalid_url",
            "exception": ValueError
        }]
    )
    def test_shortener_controller(self, url_config: dict):
        url, exception = url_config.values()
        if exception:
            with pytest.raises(exception):
                self.shortener.shorten(url)
        else:
            short_url = self.shortener.shorten(url).model_dump()
            assert short_url["long_url"] == url
            assert short_url["key"] in short_url["short_url"]
