import urllib.request
import re

global_car = []


class Car(object):
    def __init__(self, name, img, letter, series_club):
        self.name = name
        self.img = img
        self.letter = letter
        self.series_club = series_club

    def __str__(self):
        result = ""
        for index, club_str in enumerate(self.series_club):
            if index is not len(self.series_club) - 1:
                result += "\"%s\"," % club_str
            else:
                result += "\"%s\"" % club_str

        return "{\"brandname\":\"%s\",\"brandimg\":\"%s\",\"letter\":\"%s\",\"seriesclub\":[%s]}" % (
            self.name, self.img, self.letter, result)

    def add_club(self, model):
        self.series_club.append(model)


def create_url():
    url = []
    for char in range(65, 91):
        base_url = "http://www.autohome.com.cn/grade/carhtml/%s.html" % (chr(char))
        url.append(base_url)
    return url


def main():
    urls = create_url()

    for url in urls:

        web = urllib.request.urlopen(url)

        web_data = web.read().decode("gbk")

        web_data = str(web_data).replace("\n", "").replace("\r", "")

        # print(web_data)
        # 剥离品牌
        all_brand = re.findall(r"<dl(.+?)</dl>", web_data)
        print(all_brand)
        print("*" * 99)

        for brand in all_brand:
            name = re.findall(r"<dt>.+?<div><a .+?>(.+?)</a></div></dt>", brand)
            club = re.findall(r"<h4.*?><a .+?>(.+?)</a>", brand)
            img = re.findall(r"src=\"(.+?)\">", brand)
            letter = re.match(r"http://www.autohome.com.cn/grade/carhtml/(.).html", url)

            name_str = "无数据"
            img_str = "无数据"
            if len(name) > 0:
                name_str = name[0]
            if len(img) > 0:
                img_str = img[0]

            global_car.append(Car(name_str, img_str, letter.group(1), club))

    f = open("d:/test.txt", "a", encoding="utf-8")
    f.write("{\"datas\":[")
    for index, car in enumerate(global_car):
        f.write(car.__str__())
        if index is not len(global_car) - 1:
            f.write(",")
    f.write("]}")
    f.close()


if __name__ == '__main__':
    main()
