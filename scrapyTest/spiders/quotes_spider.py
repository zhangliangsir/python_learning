import scrapy

class QuotesSpider(scrapy.Spider):
    
    #scrapy crawl quotes在run-External Tools中执行这个命令就可以爬取数据了
    #scrapy shell "http://quotes.toscrape.com/page/1/"  进入shell进行调试
    
    name = "quotes"

    start_urls = ['http://quotes.toscrape.com/page/1/',]
    
    def parse(self, response):

        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': ''.join(quote.css('div.tags a.tag::text').getall()),
            }
        
        #读取下一页数据,和下面的循环的意思是一样的
#         next_page = response.css('li.next a::attr(href)').extract_first()
#         if next_page is not None:
#             next_page = response.urljoin(next_page)
#             yield scrapy.Request(next_page, callback=self.parse)
                                                                      
        for a in response.css('li.next a'):
            yield response.follow(a, callback=self.parse)
            