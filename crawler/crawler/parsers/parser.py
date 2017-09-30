import re

# Import parsers
from crawler.parsers.washington_post import parse_washington_post_references


# As article links can be a bit nebulous, we want to specify a regex
# pattern to match against each given url to determine the most
# appropriate parser.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Note:
#   If you don't import your parser and add it to this map,
#   it will not be picked up for a relevant url by the spider!
parser_map = {
    '.+\.washingtonpost\.com.+': parse_washington_post_references
}


# Precompile the parser_map for matching against given patterns
precompiled_map_items = [(re.compile(pattern), parser)
                         for pattern, parser in parser_map.items()]


def get_parser(url):
    """Return the most appropriate parser for the given media url

    Note:
        This will return the FIRST MATCH it comes to. It is important
        that the regex patterns defined above are as specific as
        possible without limiting our ability to detect a correct match

    Args:
        url (str): url to retrieve parser with

    Returns:
        appropriate reference parsing function for url
    """
    for pattern, parser in precompiled_map_items:
        if pattern.match(url):
            return parser
