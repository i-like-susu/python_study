import threading
import time

class SafeQueue:
    def __init__(self, max_size=0):
        self.queue = []
        self.max_size = max_size
        self.condition = threading.Condition()
        self.lock = threading.Lock()
        pass

    # 当前队列元素的数量
    def size(self):
        self.lock.acquire()
        size = len(self.queue)
        self.lock.release()
        return size

    # 往队列里面放入元素
    def put(self, item):
        if self.size() >= self.max_size:
            return Exception
        self.lock.acquire()
        self.queue.append(item)
        self.lock.release()
        self.condition.acquire()
        self.condition.notify()
        self.condition.release()

    # 批量放入元素
    def batch_put(self, item_list):
        if not isinstance(item_list, list):
            item_list = list(item_list)
        for item in item_list:
            self.put(item)

    # 从队列中取出元素
    def pop(self, block=False, timeout=0):
        if self.size() == 0:
            if block:
                self.condition.acquire()
                self.condition.wait(timeout)
                self.condition.release()
            else:
                return None
        if self.size() == 0:
            return None
        self.lock.acquire()
        item = self.queue.pop()
        self.lock.release()
        return item

    #  根据索引从队列中取出元素
    def get(self, index, block=False, timeout=0):
        if self.size() == 0:
            if block:
                self.condition.acquire()
                self.condition.wait(timeout)
                self.condition.release()
            else:
                None
        if self.size() == 0:
            return None
        self.lock.acquire()
        item = self.queue.pop(index)
        self.lock.release()
        return item


if __name__ == '__main__':
    queue = SafeQueue(max_size=100)

    def producer():
        while True:
            queue.put('abc')
            time.sleep(3)

    def customer():
        while True:
            item = queue.pop(block=True, timeout=2)
            print('fetch data {}'.format(item))
            time.sleep(1)

    thread_1 = threading.Thread(target=producer)
    thread_2 = threading.Thread(target=customer)

    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()
