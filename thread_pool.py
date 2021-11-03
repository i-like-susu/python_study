from concurrent.futures import ThreadPoolExecutor, as_completed, wait
import time


def get_html(times):
    time.sleep(times)
    # print('page {} is succeed'.format(times))
    return times


executor = ThreadPoolExecutor(3)
# 通过submit将执行的函数提交到线程池中，submit是立即返回
# task1 = executor.submit(get_html, (2))
# task2 = executor.submit(get_html, (4))
# task3 = executor.submit(get_html, (6))
# task4 = executor.submit(get_html, (8))

# # done方法判断某个任务是否完成
# print(task1.done())
# # result是阻塞的方法，可以获取task的执行结果
# print(task1.result())
# cancel方法可以取消该任务的执行，前提是该任务还没有执行
# print(task3.cancel())


#as_completed用于返回已经完成的task
urls = [11, 6, 7, 4]
# all_task = [executor.submit(get_html, url) for url in urls]
#用于阻塞线程，等到所有的task执行完在继续执行
# wait(all_task)
# for future in as_completed(all_task):
#     data = future.result()
#     print('get page {} success'.format(data))

# map返回已经完成的task,与as_completed的区别是，map会按照urls的顺序返回，而as_complered则是谁先执行完先打印
for data in executor.map(get_html, urls):
    print('get page {} success'.format(data))





