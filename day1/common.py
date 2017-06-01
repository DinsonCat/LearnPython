import os
import os.path
import re

rootdir = "D:\GitProjects\PythonWeb\pythonbasis"  # 指明被遍历的文件夹


def search_file(dir):
    for i in os.listdir(dir):
        if i.startswith("."): continue

        if os.path.isdir(dir + os.sep + i):
            search_file(dir + os.sep + i)
        else:
            if i.endswith("html"):
                # 替换文本
                replese_file(dir + os.sep + i)
            else:
                continue


def replese_file(path):
    print("替换文本：%s" % path)
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    with open(path, "w", encoding="utf-8") as f_w:
        for line in lines:
            if line.strip() != "":

                s = re.search("href=\"./[0-9]{2}day/index.html\"", line)

                if s is not None:
                    s1 = s.group()
                    #                 line = line.replace(s1, "href=\"#\"")
                    print(s1)
                    f_w.write("%s \n" % line.strip())


search_file(rootdir)

# for i in os.listdir(rootdir):
#     if i.startswith("."): continue
#
#     print(os.path.isdir(rootdir + os.sep + i))


# print(os.path.isfile(os.path.join(rootdir,i)))

# if i == "index.html":
#     with open(rootdir + os.sep + i, "r", encoding="utf-8") as f:
#         lines = f.readlines()
#
#         with open(rootdir + os.sep + i, "w", encoding="utf-8") as f_w:
#             for line in lines:
#                 if line.strip() != "":
#
#                     s = re.search("href=\"./[0-9]{2}day/index.html\"", line)
#
#                     if s is not None:
#                         s1 = s.group()
#                         line = line.replace(s1, "href=\"#\"")
#                         print(s1 )
#                     f_w.write("%s \n"%line.strip())
