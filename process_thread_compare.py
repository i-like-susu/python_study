import time
from concurrent.futures import ThreadPoolExecutor, as_completed, ProcessPoolExecutor


def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    with ProcessPoolExecutor(5) as executor:
        all_task = [executor.submit(fib, num) for num in range(25, 35)]
        start_time = time.time()
        for futurn in as_completed(all_task):
            data = futurn.result()
            print('data is {}'.format(data))
        print('total time is {}'.format(time.time() - start_time))
