# _*_ coding:utf-8 _*

import baike_spider
# import html_parser,url_manager,html_outputer,html_downloader
# from baike_spider import html_downloader
# from baike_spider import html_outputer, html_parser

class SpiderMain(object):

    def __init__(self):
        self.urls = baike_spider.url_manager.UrlManager()
        self.downloader = baike_spider.html_downloader.HtmlDownloader()
        self.parser = baike.spider.html_parser.HtmlParser()
        self.outputer = baike_spider.html_outputer.HtmlOupter()

    def craw(self, root_rul):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d : %s' % (count, new_url)
                html_cont = self.downloader.download(new_url)
                new_url, new_data = self.parser.parser(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 1000:
                    break

                count = count + 1

            except:
                print"crawl failed"

        self.outputer.output_html()


if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
