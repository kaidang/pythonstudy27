# -*- coding:utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import re
url ="http://tsunlaw.com/index.php/tarticle/226-zhandeqiang"
#url ="http://heyddo.com/labourlawnews"
#url ="http://baike.baidu.com/view/21087.htm"
headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
request  = urllib2.Request(url,headers=headers)
#request.add_header('User-Agent','Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6')
response = urllib2.urlopen(request)

#print response.read()

html_doc = response.read()
# 用 html.parser 解析
#soup = BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')
# 用第三方插件 lxml 解析(需安装)
soup = BeautifulSoup(html_doc,'lxml',from_encoding='utf-8')

#links = soup.find_all('a',string='关于天尚')
links = soup.find_all('a')
# 使用[0]获取全部内容,否则为乱码

#print links[0]
print type (links)

for link in links:
    print link.name,link['href'],link.get_text()



#print soup.title.get_text()
