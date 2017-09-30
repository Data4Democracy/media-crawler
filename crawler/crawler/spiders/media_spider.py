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
        max_depth (int): maximum depth to go to in depth-first crawl
    """
    name = 'media_spider'
    parent_node_lookup = {}

    def __init__(self, media_url='', max_depth=3, *args, **kwargs):
        super(MediaSpider, self).__init__(*args, **kwargs)
        assert media_url, '''
        media_spider was not initialized with starting media_url
        '''
        self._media_url = media_url
        self._max_depth = max_depth

    def start_requests(self):
        """Start crawl wih given media url
        """
        # Yield a request which will be picked up by the spider
        yield scrapy.Request(self._media_url, self.parse_media_references)

    def get_node_depth(self, node_url):
        """Given the URL of a media node, track its depth in the current crawl
        """
        depth = 0
        parent_node = node_url # At depth zero, start with current node
        while parent_node is not None:
            # Inclusive of the first node given, count every parent traversed
            depth += 1
            # use .get() to default to None if a parent node can't be found
            parent_node = self.parent_node_lookup.get(parent_node, None)
        return depth

    def parse_media_references(self, response):
        """Given a response to a scrapy.Request, parse out and delegate all media references

        This performs a depth-first tree traversal across the references in the given
        media. The depth of the traversal (and therefore the tree) is determined by the
        max_depth argument passed into the spider on initialization (defaults to max_depth=3)
        """
        # Try to retrieve a parser for the given url
        parser = get_parser(response.url)
        # Clean up the url to use as an identifier
        clean_url = response.url.split('?')[0]
        # Get the depth of the crawl thus far
        crawl_depth = self.get_node_depth(clean_url)

        # If there was a valid parser found...
        if parser:
            # Parse out the references
            references = parser(response)

            # If the max depth hasn't been reached, continue the crawl
            if crawl_depth < self._max_depth:
                # For every reference, delegate a request for it to be scraped as well
                for ref in references:
                    # Clean kwargs from ref url
                    clean_ref_url = ref['href'].split('?')[0]
                    # Track parent nodes to determine depth
                    self.parent_node_lookup[clean_ref_url] = clean_url
                    # Yield a request for Scrapy to process
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
