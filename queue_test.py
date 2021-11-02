from queue import Queue
from threading import Thread
import time

queue_data = Queue(20)

def handle_queue():
    global queue_data
    while True:
        data = queue_data.get()
        data = str(data) + "-hello"
        time.sleep(3)
        print(data)



def generate_queue():
    global queue_data
    for i in range(100):
        queue_data.put(i)
        time.sleep(1)


if '__main__' == __name__:
    generate_thread = Thread(target=generate_queue)
    handle_thread_1 = Thread(target=handle_queue)
    handle_thread_2 = Thread(target=handle_queue)
    handle_thread_3 = Thread(target=handle_queue)
    handle_thread_1.start()
    handle_thread_2.start()
    handle_thread_3.start()
    generate_thread.start()
    generate_thread.join()
    handle_thread_1.join()
    handle_thread_2.join()
    handle_thread_3.join()





