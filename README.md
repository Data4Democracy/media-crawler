# Media Crawler and Reference Tree Generator

## Project Vision

The goal of this project is, given any article (or item in general) on a media site such as Washington Post, The Hill, CNN, Forbes, AP, and even Breitbart, we can take the references made in that site (links as `<a>` tags) and connect that article to the articles it references--then connect those articles to the articles, tweets, and videos they reference. This will result in a tree of references with the original article as a root, and will allow us to combine these trees into a media reference graph at a large scale.

## Tools Ideal for Implementation

* [Scrapy](https://doc.scrapy.org/en/latest/index.html)
  * For performing the [Broad Crawl](https://doc.scrapy.org/en/latest/topics/broad-crawls.html) across all the domains which this will need to.
  * Scrapy is preferred for its predefined API with item pipelines and response-handling delegating
* [Twitter API](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/get-statuses-show-id)
  * This will allow us to parse out embedded and linked tweets into tractable form
* [Newspaper](http://newspaper.readthedocs.io/en/latest/)
  * This is a really great API for parsing out the full text of articles as well as meta data where necessary
