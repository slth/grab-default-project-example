# -*- coding: utf-8 -*-
"""
Github projects spy
"""
from optparse import OptionParser

from grab import Grab
from grab.spider import Spider, Task
from weblib.logs import default_logging

from spiders.explore import ExploreSpider
from spiders.lang_python import LangPythonSpider
from config import default_spider_params, Session

if __name__ == '__main__':
    default_logging()
    parser = OptionParser()

    # command line options
    parser.add_option("-p", "--python", action="store_true",
                      dest="parse_python", default=False)

    options, args = parser.parse_args()

    bot = ExploreSpider(**default_spider_params())

    #print dir(bot)

    #bot.setup_proxylist(proxy_file='proxylist.txt',proxy_type='http', auto_change=True)

    #print bot.load_proxylist.__doc__
    #bot.load_proxy(source='proxylist.txt',proxy_type='http') #, auto_change=True)
    #bot.setup_grab(timeout=4096, connect_timeout=10)
    bot.run()
    print bot.render_stats() 