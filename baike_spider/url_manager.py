# -*- coding:utf-8 -*-

class UrlManager(object):

    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self):
        if url is None:
            return
        if url not in sefl.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self):
        if urls is None or len(urls) == 0:
            return
        if url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)