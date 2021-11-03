import threading
from threading import Thread
import time


class HtmlSpider(Thread):
    def __init__(self, url, sema):
        super().__init__()
        self.url = url
        self.sema = sema

    def run(self):
        time.sleep(2)
        print('get html is succeed')
        self.sema.release()


class UrlProducer(Thread):
    def __init__(self, sema):
        super().__init__()
        self.sema = sema

    def run(self):
        for i in range(20):
            self.sema.acquire()
            html_read = HtmlSpider('www.baidu.com{}'.format(i), self.sema)
            html_read.start()


if __name__ == '__main__':
    sema = threading.Semaphore(3)
    url_proceduer = UrlProducer(sema)
    url_proceduer.start()
