# -*- coding: utf-8 -*-
import scrapy
from ..items import JobsItem,ZhilianItemLoader

class InternetSpider(scrapy.Spider):
    name = 'internet'
    allowed_domains = ['sou.zhaopin.com/jobs/searchresult.ashx?kw=python']
    start_urls = ['http://sou.zhaopin.com/jobs/searchresult.ashx?kw=python']

    custom_settings = {
        'DOWNLOAD_DELAY':2,
        'COOKIES_ENABLED':False,
        'DEFAULT_REQUEST_HEADERS':{
            'Referer':'http://sou.zhaopin.com/jobs/searchresult.ashx?kw=python',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
        }
    }

    def parse(self, response):
        urls = response.xpath('//div[@class="newlist_list_content"]/table[@class="newlist"]/tr[1]/td[1]/div/a[1]/@href').extract()
        if urls:
            for job_url in urls:
                yield scrapy.Request(url=job_url,callback=self.parse_job,dont_filter=True)


        next_page = response.css('.next-page::attr(href)').extract_first()
        if next_page:
            yield scrapy.Request(url=next_page,callback=self.parse,dont_filter=True)

    def parse_job(self,response):

        item_loader = ZhilianItemLoader(item=JobsItem(),response=response)
        item_loader.add_css("position",".inner-left.fl h1::text")
        item_loader.add_css("company",".inner-left.fl h2 a::text")
        item_loader.add_css("advantages",'.welfare-tab-box span')
        item_loader.add_xpath("low_salary",'//div[@class="terminalpage-left"]/ul/li[1]/strong/text()')
        item_loader.add_xpath("high_salary", '//div[@class="terminalpage-left"]/ul/li[1]/strong/text()')
        item_loader.add_xpath("data",'//div[@class="terminalpage-left"]/ul/li[3]/strong/span/text()')
        item_loader.add_xpath("experiences",'//div[@class="terminalpage-left"]/ul/li[5]/strong/text()')
        item_loader.add_xpath("num",'//div[@class="terminalpage-left"]/ul/li[7]/strong/text()')
        item_loader.add_xpath("type",'//div[@class="terminalpage-left"]/ul/li[4]/strong/text()')
        item_loader.add_xpath("degree",'//div[@class="terminalpage-left"]/ul/li[6]/strong/text()')
        item_loader.add_xpath("task",'//div[@class="terminalpage-left"]/ul/li[8]/strong/a/text()')
        item_loader.add_xpath("place",'//div[@class="terminalpage-left"]/ul/li[2]/strong/a/text()')
        item_loader.add_css("describe",'.terminalpage-main.clearfix .tab-cont-box .tab-inner-cont p')
        jobs = item_loader.load_item()
        yield jobs
