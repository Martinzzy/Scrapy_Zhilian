# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import re
import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst,MapCompose,Join
from w3lib.html import remove_tags

def return_value(value):
    return value

def get_lowsalary(value):
    data = re.match('(\d+)-(\d+)', value)
    if data.group(1):
        low_salary = data.group(1)
        return int(low_salary)
    else:
        return 0

def get_highsalary(value):
    data = re.match('(\d+)-(\d+)', value)
    if data.group(2):
        high_salary = data.group(2)
        return int(high_salary)
    else:
        return 0

def get_num(value):
    data = re.match('(\d+)',value)
    if data:
        return int(data.group(1))
    else:
        return 0

class ZhilianItemLoader(ItemLoader):

    default_output_processor = TakeFirst()


class JobsItem(scrapy.Item):
    position = scrapy.Field()
    company = scrapy.Field()
    advantages = scrapy.Field(output_processor=Join(','),input_processor=MapCompose(remove_tags),)
    low_salary = scrapy.Field(input_processor=MapCompose(get_lowsalary))
    high_salary = scrapy.Field(input_processor=MapCompose(get_highsalary))
    data = scrapy.Field()
    experiences = scrapy.Field()
    num = scrapy.Field(input_processor=MapCompose(get_num))
    type = scrapy.Field()
    degree = scrapy.Field()
    task = scrapy.Field()
    place = scrapy.Field()
    describe = scrapy.Field(output_processor=Join(','),input_processor=MapCompose(remove_tags))
