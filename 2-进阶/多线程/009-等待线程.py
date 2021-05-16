from threading import Thread

nums = 1000000000000000
def run():
    for i in range(1000000):
        global nums
        nums = nums - 1
        print(nums)


if __name__ == '__main__':
    thread = Thread(target=run)
    thread.start()
    thread.join(timeout=2)
