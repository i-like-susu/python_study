from threading import Thread


class TianMao(Thread):
    def __init__(self):
        super().__init__(name='天猫精灵')

    def run(self):
        print('{}:小爱同学'.format(self.name))


class XiaoAi(Thread):
    def __init__(self):
        super().__init__(name='小爱')

    def run(self):
        print('{}:在'.format(self.name))


if __name__ == '__main__':
    xiao_ai = XiaoAi()
    tian_mao = TianMao()

    tian_mao.start()
    xiao_ai.start()
