# Media Crawler and Reference Tree Generator

## Project Purpose

The goal of this project is, given any article (or item in general) on a media site such as Washington Post, The Hill, CNN, Forbes, AP, and even Breitbart, we can take the references made in that site (links as `<a>` tags) and connect that article to the articles it references--then connect those articles to the articles, tweets, and videos they reference. This will result in a tree of references with the original article as a root, and will allow us to combine these trees into a media reference graph at a large scale.

_Example small tree with Washington Post article as root:_
![small-dag](https://i.imgur.com/M8SbyPK.png)

Once enough of these smaller trees are amassed, connections can be made to draw out a much larger media ecosystem as a single graph (perhaps with isolated subgraphs, denoting closed networks).

## Installing Dependencies

At a minimum, you will need `Scrapy` and `BeautifulSoup` for the baseline functionality described below. Install those with yoru virtual environment of choice, ensuring that you are using Python `3.6.x` in said environment. 

## Starting the MediaSpider Crawl

To start the crawling process, you will need to pass a url to the MediaSpider via the Scrapy CLI.

First, `cd` into `media-crawler/crawler`, (where the `scrapy.cfg` file is). Then, run this command, passing the spider the URL you want to start with:

```bash
scrapy crawl media_spider -a media_url="https://www.washingtonpost.com/news/post-politics/wp/2017/09/07/did-facebook-ads-traced-to-a-russian-company-violate-u-s-election-law/?tid=a_inl&utm_term=.e24142917aa8" -o media.json
```

Here, we use a Washington Post article as an example. Feel free to use this as a baseline test.

**Note: At the moment, we do not control the depth to which the spider scrapes. Once you have scraped enough to determine the performance of the crawler, hit `CTRL-C` once (multiple times won't allow the spider to soft stop) to make the crawl stop. You can see the results in `media-crawler/crawler/media.json`, as this is the file specified in the command above.**
