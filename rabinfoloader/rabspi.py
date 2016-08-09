#coding=UTF8
import csv
import logging
import mysql.connector

from grab.spider import Spider, Task

class rspider(Spider):
    initial_urls = ['http://www.alekseysavin.com/myblog/']

    def prepare(self):
        self.result_file_file = csv.writer(open('result.csv', 'w'))
        self.result_counter = 0

    def task_initial(self, grab, task):
        print 'Home Page'

        for elem in grab.doc.select('/h3'):
            yield Task('spi', url=elem.get('href'))

    def task_post(self, grab, task):
        print 'Blog post: %s' % task.url

        post = {
            'url': task.url,
            'title': grab.xpath_text('//h3[@class="article"]'),
        }

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    bot = rspider(thread_number=1)
    bot.run()
