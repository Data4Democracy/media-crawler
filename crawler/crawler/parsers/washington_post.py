from bs4 import BeautifulSoup
from unicodedata import normalize


def parse_washington_post_references(response):
    """Given a typical article on The Washington Post, parse out reference links

    Args:
        response: scrapy response object

    Returns:
        list(dict) of references and their respective contexts
    """
    # Create list to store references
    references = []

    # Get all <p> tags in the article body
    article_p_tags = response.xpath('//article[@itemprop="articleBody"]')[0].css('p')

    # Preserve all tags which have links within their children
    linking_p_tags = [tag for tag in article_p_tags if len(tag.css('a'))]

    # For every tag, create a reference for every link therein
    for tag in linking_p_tags:
        # Use BeautifulSoup + unicodedate.normalize to get a clean context
        # to use in establishing the context of each link reference
        context_soup = BeautifulSoup(tag.get())

        # A lot of times we will get some weird \xa0 (special whitespace) characters
        # in the mix. We do not want these in our results. For information on this, see:
        # https://docs.python.org/2/library/unicodedata.html#unicodedata.normalize
        cleaned_context = normalize('NFKD', context_soup.get_text())

        # Grab every link within with a css selector
        for link in tag.css('a'):
            # Get the href from inside the anchor (link) tag
            link_href = link.xpath('@href').extract()[0]

            # Get the inner text of the link to use as a reference
            # with respect to the context
            link_text = link.xpath('text()').extract()[0]

            # Use what we retrieved to create a dict object containing the data
            reference = {
                'href': link_href,
                'text': link_text,
                'context': cleaned_context
            }
            references.append(reference)
    # Return our created list
    return references
