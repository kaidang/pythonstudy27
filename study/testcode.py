# -*- coding: utf-8 -*-

k = "B5f10******b28******e5****************9d221"
url = r"http://api.map.baidu.com/direction/v1?mode=driving&origin=上地五街&destination=北京大学&origin_region=北京&destination_region=北京&output=json&ak=" + ak
import urllib2
import json
# import httplib2

def getContent(url):
    req = urllib2.Request(url)
    req.set_proxy("siwebproxy01.apac.nokia.com:8080", "http")
    res = urllib2.urlopen(req)
    content = res.read()
    return content


if __name__ == '__main__':
#     httplib2.urllib.parse.unquote('\u6ce8\u91ca')
    content = getContent(url)
    cc = content.decode("unicode_escape")
    ccc = cc.encode("UTF-8")
    print ccc

