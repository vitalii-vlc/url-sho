from pydantic import BaseModel


class ShortUrl(BaseModel):
    long_url: str
    short_url: str
    key: str
