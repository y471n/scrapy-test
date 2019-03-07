# -*- coding: utf-8 -*-
from urllib.parse import urlparse

import scrapy
# Any additional imports (items, libraries,..)
from artworks.items import ArtworksItem
from artworks.loaders import ArtworksLoader


class TrialSpider(scrapy.Spider):
    name = 'trial'
    # Start with Browse Page: http://pstrial-a-2018-10-19.toscrape.com/browse/
    start_urls = ['http://pstrial-a-2018-10-19.toscrape.com/browse/']  #
    # start_urls = ['http://pstrial-a-2018-10-19.toscrape.com/browse/qingjapanese/annejoseph/donstyle']  #

    _css_selectors = {
        "main_heading": "h1::text",
        "subcats": "h3",
        "artworks_item_images": "#body div:nth-child(n) a img",
        # "artworks_item_image_relative_url": "::attr('src')",
        "item_page_artist": "h2::text",
        "item_page_title": "h1::text",
        "item_page_image": "#body img::attr('src')",
    }

    _xpath_selectors = {
        "subcat_link": "ancestor::a/@href",
        "artworks_item_relative_url": "ancestor::a/@href",
        "next_link": "//a[text()='Next']/@href",

        "item_page_description": ".//div[@itemprop='description']/p/text()",
    }

    def _get_base_url(self, url):
        parsed_url = urlparse(url)
        return parsed_url.scheme + "://" + parsed_url.netloc

    def parse(self, response):
        # Put your logic to process artworks directory
        parent_heading = response.meta.get("parent_heading")
        category_heading = response.css(self._css_selectors.get("main_heading")).extract_first()
        category_heading = category_heading.split("-")[1].strip()
        category_heading = parent_heading + "," + category_heading if parent_heading else category_heading

        # 1. #subcats all h3.. get their h3
        subcats = response.css(self._css_selectors.get("subcats"))

        # 1. TODO: yield Next Subcategories
        for subcat in subcats:
            category_page = subcat.xpath(self._xpath_selectors.get("subcat_link")).get()
            yield response.follow(category_page, self.parse, meta={"parent_heading": category_heading})

        # 2. Iterate through Link items
        # TODO: 2. Iterate and yield the item page
        item_images = response.css(self._css_selectors.get("artworks_item_images"))
        for item_image in item_images:
            item_page = item_image.xpath(self._xpath_selectors.get("artworks_item_relative_url")).get()
            yield response.follow(item_page, self.parse_item, meta={"category": category_heading})

        # TODO: 3. Follow next pages for item list
        next_link = response.xpath(self._xpath_selectors.get("next_link")).get()
        yield response.follow(next_link, self.parse, meta={"parent_heading": category_heading})

    def parse_item(self, response):
        base_url = self._get_base_url(response.url)
        loader = ArtworksLoader(ArtworksItem(), response=response, base_url=base_url)
        loader.add_value("url", response.url)
        loader.add_css("artist", self._css_selectors.get("item_page_artist"))
        loader.add_css("title", self._css_selectors.get("item_page_title"))
        loader.add_css("image", self._css_selectors.get("item_page_image"))
        # 4. TODO: Img height + width
        loader.add_xpath("description", self._xpath_selectors.get("item_page_description"))
        loader.add_value("path", response.meta.get("category").split(","))

        yield loader.load_item()
