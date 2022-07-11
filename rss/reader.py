#
# reader.py
# Author: Ahmad Abdalmageed
# Date: 7/11/22
#

import requests
import xml.etree.ElementTree as ET


class FeedReader:
    """
    RSS Feed Reader
    """
    def __init__(self, url: str):
        """
        Function initializer
        :param url: Given RSS Feed URL
        :return: None
        """
        self.url = url

    def getResponse(self) -> requests.Response:
        """
        Requests the Content of the RSS feed URL
        :return: requests.Response with all RSS Feed Content
        """
        try:
            res = requests.get(self.url, headers={"Accept-Language": "en-US,en;q=0.5"})
            res.raise_for_status()
        except requests.exceptions.RequestException as error:
            print(f"Error While Parsing Check Link : {self.url}")
            raise SystemExit(error)
        return res

    def parseData(self) -> ET.ElementTree:
        """
        XML Data Parser
        :return: ET.ElementTree Instance
        """
        try:
            root = ET.fromstring(self.getResponse().content)
        except ET.ParseError as error:
            print("Error Occurred while parsing XML, Try another URL")
            raise SystemExit(error)
        else:
            items = root[0].findall('item')
        return items

    def readFeed(self):
        """
        RSS Feed Reader and Printer
        :return: None
        """
        items = self.parseData()

        for item in items:
            print("------------------------------------------------------------------")
            print(f'---- {item.find("title").text.upper()}')
            print(f'---- {item.find("description").text}')
            print(f'---- {item.find("link").text}')
