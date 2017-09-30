import logging
import re
import scrapy
from scrapy.utils.response import get_base_url

from crawler.parsers import get_parser
from crawler.items import MediaItem


class MediaSpider(scrapy.Spider):
    """Scrapy Spider for crawling various forms of internet media to retrieve references

    Args:
        media_url (str): url to parse as root
    """
    name = 'media_spider'

    def __init__(self, media_url='', *args, **kwargs):
        super(MediaSpider, self).__init__(*args, **kwargs)
        assert media_url, '''
        media_spider was not initialized with starting media_url
        '''
        self._media_url = media_url

    def start_requests(self):
        """Start crawl wih given media url
        """
        # Yield a request which will be picked up by the spider
        yield scrapy.Request(self._media_url, self.parse_media_references)

    def parse_media_references(self, response):
        """Given a response to a scrapy.Request, parse out and delegate all media references
        """
        # Try to retrieve a parser for the given url
        parser = get_parser(response.url)
        # Clean up the url to use as an identifier
        clean_url = response.url.split('?')[0]

        # If there was a valid parser found...
        if parser:
            # Parse out the references
            references = parser(response)

            # For every reference, delegate a request for it to be scraped as well
            for ref in references:
                yield scrapy.Request(ref['href'], self.parse_media_references)

            # After processing all references, yield the root media item given.
            # Note: this is recursive, technically, so this is the root of the
            # current reference tree starting with the scope of this function.
            yield MediaItem(
                url=clean_url,
                media_type='Article', # TODO: Tweets and other types need to be accounted for
                references=references
            )

        # If a relevant parser was not found...
        else:
            # yield a MediaItem with only a URL to identify item as a leaf node
            yield MediaItem(
                url=clean_url,
                media_type='Unknown',
                references=None
            )
