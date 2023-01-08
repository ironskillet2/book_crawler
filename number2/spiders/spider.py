import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from number2.items import BookItem



class bookSpider(CrawlSpider):
    name = 'books'

    start_urls = [
        'http://books.toscrape.com/'
    ]

    rules = (
        Rule(LinkExtractor(restrict_css=".nav-list > li > ul > li > a"), follow=True),
        Rule(LinkExtractor(restrict_css=".product_pod > h3 > a"), callback="parse_book")
    )

    def parse_book(self, response):
        book_item = BookItem()

        book_item["title"] = response.css(".col-sm-6.product_main > h1::text").get()
        book_item["price"] = response.css(".price_color::text").get().replace('00', ' ')
        return book_item             
        