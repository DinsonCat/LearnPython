import os

# path = __file__
# print(os.path.abspath(path))  # 返回绝对路径
# print(os.path.basename(path))  # 返回文件名
# print(os.path.splitdrive(path))   #一般用在windows下，返回驱动器名和路径组成的元组
# print(os.path.splitext("D:/WrokSpace/PythonProjects/LearnPython/demo/oss"))  #分割路径，返回路径名和文件扩展名的元组

import time

print("start")

start_time = time.time()
# for a in range(1, 998):
#     for b in range(1, 999 - a):
#         for c in range(1000 - a - b):
#             if (a * a + b * b)==((1000-a-b) * (1000-a-b)):
#                 print(a,b,1000-a-b)

for a in range(1, 999):
    for b in range(1, 1000):
        if (a * a + b * b) == ((1000 - a - b) * (1000 - a - b)):
            print(a, b, 1000 - a - b)
end_time = time.time()
print("耗时：%fms" % (end_time - start_time))
print("end")
#
# print("*" * 20)
#
# start_time = time.time()
# for a in range(0, 1001):
#     for b in range(0, 1001):
#         for c in range(0, 1001):
#             if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
#                 print("a,b,c:%d %d %d" % (a, b, c))
# end_time = time.time()
# print("耗时：%fms" % (end_time - start_time))
# print("end")
