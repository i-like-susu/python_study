import multiprocessing
import time

def get_html(n):
    time.sleep(n)
    # print('i am process')
    return n

if __name__ == '__main__':
    # process = multiprocessing.Process(target=get_html, args=(2,))
    # process.start()
    # process.join()
    # print('i am main')

    # 使用进程池
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # result = pool.apply_async(get_html, args=(3,))
    #
    # pool.close()
    # pool.join()
    # print(result.get())

    #imap
    for result in pool.imap(get_html, [1, 5, 3]):
        print('{} sleep success'.format(result))

    #imap_unordered