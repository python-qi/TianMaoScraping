#coding:utf-8
import url_manager, html_downLoader, html_parser, html_outputer
import robotparser
import logging
import sys
if sys.getdefaultencoding()!="utf-8":
    reload(sys)
    sys.setdefaultencoding("utf-8")

class SpiderMain(object):
    def __init__(self):
        self.url_manager=url_manager.Url_Manager()
        self.html_downloader=html_downLoader.HtmlDownLoader()
        self.html_parser=html_parser.HtmlParser()
        self.outputer=html_outputer.OutPuter()

    def craw(self,rool_url):
        pass

if __name__=="__main__":
    root_url='https://search.jd.com/Search'