import threading
from threading import Thread, Condition


class TianMao(Thread):
    def __init__(self, cond):
        super().__init__(name='天猫精灵')
        self.cond = cond

    def run(self):
        with self.cond:
            print('{}:小爱同学'.format(self.name))
            self.cond.notify()
            self.cond.wait()

            print('{}:我们来对古诗吧'.format(self.name))
            self.cond.notify()
            self.cond.wait()


class XiaoAi(Thread):
    def __init__(self, cond):
        super().__init__(name='小爱')
        self.cond = cond

    def run(self):
        with self.cond:
            self.cond.wait()
            print('{}:在'.format(self.name))
            self.cond.notify()

            self.cond.wait()
            print('{}:好啊'.format(self.name))
            self.cond.notify()


if __name__ == '__main__':
    cond = threading.Condition()
    xiao_ai = XiaoAi(cond)
    tian_mao = TianMao(cond)

    xiao_ai.start()
    tian_mao.start()
