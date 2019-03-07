# -*- coding: utf-8 -*-
import scrapy
# Any additional imports (items, libraries,..)


class TrialSpider(scrapy.Spider):
    name = 'trial'
    # Start with Browse Page: http://pstrial-a-2018-10-19.toscrape.com/browse/
    start_urls = ['http://pstrial-a-2018-10-19.toscrape.com/browse/']  #

    def parse(self, response):
        # Put your logic to process artworks directory

        # 1. #subcats all h3.. get their h3


        # yield Next Subcategories
        # 2. Get Art in this category
        # 3. Yield Next Page's Art in same category page

        pass