from __future__ import annotations
from typing import NamedTuple

from bs4 import BeautifulSoup
import httpx
from httpx import URL


class Socials(NamedTuple):
    facebook: str | None
    instagram: str | None
    twitter: str | None
    linkedin: str | None
    tiktok: str | None


def process_url(*, url: URL=None ) -> {URL: Socials}:
    response = httpx.get(url)
    body = BeautifulSoup( response.read() )

    facebook_anchors = body.select('a[href*="facebook.com"], a[href*="fb.com"]')
    facebook_links = [anchor.get('href') for anchor in facebook_anchors]

    instagram_anchors = body.select('a[href*="instagram.com"], a[href*="ig.me"]')
    instagram_links = [anchor.get('href') for anchor in instagram_anchors]

    twitter_anchors = body.select('a[href*="x.com"], a[href*="twitter.com"], a[href*="t.co"]')
    twitter_links = [anchor.get('href') for anchor in twitter_anchors]

    linkedin_anchors = body.select('a[href*="linkedin.com"]')
    linkedin_links = [anchor.get('href') for anchor in linkedin_anchors]

    tiktok_anchors = body.select('a[href*="tiktok.com"]')
    tiktok_links = [anchor.get('href') for anchor in tiktok_anchors]

    return {url: Socials(
        next(iter(facebook_links), None),
        next(iter(instagram_links), None),
        next(iter(twitter_links), None),
        next(iter(linkedin_links), None),
        next(iter(tiktok_links), None),
    )}


if __name__ == "__main__":
    pass