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
    rssURL: str = 'https://eg.indeed.com/rss?q=software%20engineer&l=cairo&sort=date&vjk=bb9215551b02825d'
    rssReaderAPI(rssURL)
