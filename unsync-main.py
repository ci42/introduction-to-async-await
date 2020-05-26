# requires the unsync package:
# pip install unsync

from unsyncable import synchronous_process, asynchronous, synchronous_thread
import time

def main():
    tasks = [f for f in (synchronous_process(), asynchronous(), synchronous_thread())]

    for t in tasks:
        print(t.result())

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'time elapsed: {end - start}')
