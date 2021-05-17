#!/usr/bin/env  python
# --*--coding:utf-8 --*--
# 1.队列
# from multiprocessing import Process,Queue
#
# def worker(queue):
#     for i in range(10):
#         queue.put(i)
#
#
# if __name__ == '__main__':
#     q = Queue(10)
#     process = Process(target=worker,args=(q,))
#     process.start()
#     print(q.get())
#     print(q.get())
#     process.join()

# 2.管道
from multiprocessing import Process,Pipe

def worker(conn):
    conn.send([1,2,3])
    conn.close()

if __name__ == '__main__':
    pare_conn, child_conn = Pipe()
    process = Process(target=worker,args=(child_conn,))
    process.start()
    obj = pare_conn.recv()
    print(obj)
    process.join()