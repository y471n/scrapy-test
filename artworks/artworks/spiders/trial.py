# -*- coding: utf-8 -*-
import scrapy
# Any additional imports (items, libraries,..)


class TrialSpider(scrapy.Spider):
    name = '<spider_name>'
    start_urls = ['<start_urls>']

    def parse(self, response):
        # Put your logic to process artworks directory
        pass

    def parse_artwork(self, response):
        # Processing each individual artwork here
        pass