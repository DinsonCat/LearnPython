# linux下才有fork方法
#
# import os
# import time
#
# ret = os.fork()
# print(ret)
# if ret == 0:
#     while True:
#         print("--------1---------")
#         time.sleep(1)
# else:
#     while True:
#         print("--------2---------")
#         time.sleep(1)
#
# from multiprocessing import Process
# import time
#
#
# def f():
#     while True:
#         print("-------1--------")
#         time.sleep(1)
#
#
# if __name__ == '__main__':
#     p = Process(target=f)
#     p.start()
#
# # while True:
# print("-------main-------")
#     # time.sleep(1)

import time

for i in range(100):
    print("\r现在的进度是：%d%%" % i, end="")
    time.sleep(0.1)
