import os

path = __file__
print(os.path.abspath(path))  # 返回绝对路径
print(os.path.basename(path))  # 返回文件名
print(os.path.splitdrive(path))   #一般用在windows下，返回驱动器名和路径组成的元组
print(os.path.splitext("D:/WrokSpace/PythonProjects/LearnPython/demo/oss"))  #分割路径，返回路径名和文件扩展名的元组