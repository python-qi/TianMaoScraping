#coding:utf-8
import sys
import urllib2
if sys.getdefaultencoding()!='utf-8':
    reload(sys)
    sys.setdefaultencoding("utf-8")
if __name__=="__main__":
    url='https://search.jd.com/Search?keyword=水果&enc=utf-8&page=3'
    html=urllib2.urlopen(url).read()
    print html