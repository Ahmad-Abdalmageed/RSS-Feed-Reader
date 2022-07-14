#
# main.py
# Author: Ahmad Abdalmageed
# Date: 7/11/22
#
from rss.reader import FeedReader


def rssReaderAPI(url: str) -> None:
    """
    An API to the RSS Feed Reader Class
    :param url: RSS Feed Reader URL
    :return: None
    """
    reader = FeedReader(url)
    reader.readFeed()


if __name__ == '__main__':
    # Example reading from Indeed Egypt the Feed for Software Engineer Search
    rssURLS = list(input("Enter RSS Feeds (seperated by space ):").split(' '))
    for number, rssURL in enumerate(rssURLS):
        print(f"######################### RSSFeed {number + 1} ##################################")
        rssReaderAPI(rssURL)
