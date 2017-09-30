# Media Crawler and Reference Tree Generator

## Project Purpose

The goal of this project is, given any article (or item in general) on a media site such as Washington Post, The Hill, CNN, Forbes, AP, and even Breitbart, we can take the references made in that site (links as `<a>` tags) and connect that article to the articles it references--then connect those articles to the articles, tweets, and videos they reference. This will result in a tree of references with the original article as a root, and will allow us to combine these trees into a media reference graph at a large scale.

_Example small tree with Washington Post article as root:_
![small-dag](https://i.imgur.com/M8SbyPK.png)

Once enough of these smaller trees are amassed, connections can be made to draw out a much larger media ecosystem as a single graph (perhaps with isolated subgraphs, denoting closed networks).

This will, ideally, give us a foundation for performing analysis on media. What sort of connections exist between various media-entities? What entities commonly use themselves as a reference? Can we use the articles, their references, and some natural-language tools to understand a more specific problem?

Hopefully, this can be a tool that serves all of those purposes.

## Installing Dependencies

At a minimum, you will need `Scrapy` and `BeautifulSoup` for the baseline functionality described below. Install those with yoru virtual environment of choice, ensuring that you are using Python `3.6.x` in said environment. 

## Starting the MediaSpider Crawl

To start the crawling process, you will need to pass a url to the MediaSpider via the Scrapy CLI.

First, `cd` into `media-crawler/crawler`, (where the `scrapy.cfg` file is). Then, run this command, passing the spider the URL you want to start with.

```bash
scrapy crawl media_spider -o media.json -a media_url="https://www.washingtonpost.com/news/post-politics/wp/2017/09/07/did-facebook-ads-traced-to-a-russian-company-violate-u-s-election-law/?tid=a_inl&utm_term=.e24142917aa8"
```

Here, we use a Washington Post article as the starting point. Feel free to use this as a baseline test.

**Note: This defaults to crawling 3 nodes deep in any reference tree (ie: three references down from the starting media item). You can change this via `DEPTH_LIMIT` in crawler/crawler/settings.py**


## Contributing

For contributing, the typical open-source git-flow applies.

Fork the project, then make a branch off of `master` with a clear and concise name describing your intentions with the branch--something like `handle-old-wapo-format`.

Then, make your changes to the code in that branch in your Fork on your machine (following instructions above to ensure it works and doesn't throw any unexpected errors).

When documenting your code, please refer to the [Google Python Docstring Standard](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).

After that, commit the changes to your branch with a _clear heading_ and _specific details as to what you have changed_. Then, push the branch up to your forked copy of the repository.

At this point, go to Pull Requests at the top of the GitHub page and select `New pull request`. On this next screen, you will see an option to `Compare Across Forks`. Click this, and you will be able to compare the branch on your fork with the master branch of the main repository in a pull request.

If you have any further questions about using git or if some of this doesn't make sense, please check out the `#github-help` channel on the D4D Slack.

For any other issues, please ping @josephpd3 in the #p-media-crawler channel.
