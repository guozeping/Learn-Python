from threading import Thread
from threading import Semaphore
import time

nums = 1000
def run(semaphore):
    semaphore.acquire()
    global nums
    nums = nums - 1
    print("nums:---", nums)
    time.sleep(10)
    semaphore.release()
    print("==========================")



if __name__ == '__main__':
    semaphore = Semaphore(5)
    for i in range(100):
        thread = Thread(target=run, args=(semaphore,))
        thread.start()