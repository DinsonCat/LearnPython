import re
import os

root_url = "D:\MH"


class Json(object):
    def __init__(self):
        self.types = set()

    def appends(self, kind):
        self.types.add(kind)

    def __str__(self):
        result = "{"
        for kind in self.types:
            result += kind + ","
        result += "}"
        return result


result = "{\"data\":["

lists = os.listdir(root_url)

count = 0


def get_file_name():
    global count
    count += 1
    if count < 10:
        return "mh_ic_00%d.png" % count
    elif count < 100:
        return "mh_ic_0%d.png" % count
    else:
        return "mh_ic_%d.png" % count


current = ""
isFrist = True
for item in lists:

    item = item.replace(".png", "")
    item_names = item.split("-")
    new_name = get_file_name()

    if item_names[0] != current:
        current = item_names[0]
        if result.endswith(","):
            result = result[0:-1]
        if isFrist:
            result += "{\"%s\":[" % (item_names[0])
            isFrist = False
        else:
            result += "]},{\"%s\":[" % (item_names[0])

        if item_names.__len__() == 3:
            n = re.findall(r"(.+)【", item_names[2])
            result += "{\"name\":\"%s\",\"species\":\"%s\",\"icon\":\"http://ondlsj2sn.bkt.clouddn.com/%s\"}," % (
            n[0], item_names[1], new_name)
        elif item_names.__len__() == 2:

            n = re.findall(r"(.+)【", item_names[1])
            result += "{\"name\":\"%s\",\"icon\":\"http://ondlsj2sn.bkt.clouddn.com/%s\"}," % (n[0], new_name)
    else:
        if item_names.__len__() == 3:

            n = re.findall(r"(.+)【", item_names[2])
            result += "{\"name\":\"%s\",\"species\":\"%s\",\"icon\":\"http://ondlsj2sn.bkt.clouddn.com/%s\"}," % (
            n[0], item_names[1], new_name)
        elif item_names.__len__() == 2:
            n = re.findall(r"(.+)【", item_names[1])
            result += "{\"name\":\"%s\",\"icon\":\"http://ondlsj2sn.bkt.clouddn.com/%s\"}," % (n[0], new_name)


    # 重命名
    old = root_url + os.sep + item + ".png"
    new = root_url + os.sep + new_name
    print(old + " ------- " + new)
    os.rename(old, new)

if result.endswith(","):
    result = result[0:-1]

result += "]}]}"
print(result)
