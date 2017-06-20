import os


class File(object):
    def __init__(self, file_path):
        self.dir_name = file_path
        self.base_name = os.path.basename(file_path)

    def rename_child(self, name, new):
        os.rename(self.child_dir(name), self.child_dir(new))

    def contains(self, name):
        return True if self.base_name.find(name) is not -1 else False

    def is_dir(self):
        return os.path.isdir(self.dir_name)

    def get_child(self):
        return os.listdir(self.dir_name)

    def child_dir(self, name):
        return self.dir_name + os.sep + name

    def parent(self):
        return os.path.dirname(self.dir_name)

    def delete_child(self, name):
        os.remove(self.child_dir(name))
        print("delete: %s.. \033[1;32mOK\033[0m" % os.path.basename(self.child_dir(name)))


def replace_mode():
    msg = " mode:\n 1 for this path\n 2 for this and under path"
    print_format("ATTENTION", msg)
    old_word = input("old word: ")
    if old_word is "":
        pri_fuck()
        return
    new_word = input("new word: ")
    if new_word is "":
        pri_fuck()
        return
    mode = input("mode: ")
    if 0 < int(mode) < 3:
        # 根据输入重命名
        search_file(File(File(__file__).parent()), old_word, new_word, int(mode))
    else:
        pri_fuck()  # 获取指定路径的所有文件名字


def delete_mode():
    msg = " mode:\n 1 for this path\n 2 for this and under path"
    print_format("ATTENTION", msg)
    likes = input("likes: ")
    if likes is "":
        pri_fuck()
        return
    mode = input("mode: ")
    if 0 < int(mode) < 3:
        # 根据输入重命名
        delete_file(File(File(__file__).parent()), likes, int(mode))
    else:
        pri_fuck()  # 获取指定路径的所有文件名字


def delete_file(file, key, mode):
    dir_list = file.get_child()
    for name in dir_list:
        if name.find(key) is not -1:
            file.delete_child(name)
        if mode == 2 and file.is_dir():
            delete_file(file.child_dir(name), key, mode)
    delete_mode()


def search_file(file, old_word, new_word, mode):
    dir_list = file.get_child()
    for name in dir_list:
        if name.find(old_word) is not -1:
            new_name = name.replace(old_word, new_word)
            print(new_name)
            file.rename_child(name, new_name)
        if mode == 2 and file.is_dir():
            search_file(file.child_dir(name), old_word, new_word, mode)
    replace_mode()


win_mini = 60


def print_format(title, msg, mode=-1):
    msg_list = msg.split("\n")
    max_len = win_mini
    max_len = max_len if max_len > len(msg) else len(msg) + 1
    print("\n*%s*" % (" %s " % title).center(max_len, "*"))
    print("*%s*" % (" " * max_len))
    for msg in msg_list:
        if mode == -1:
            print("*%s*" % msg.ljust(max_len, " "))
        elif mode == 0:
            print("*%s*" % msg.center(max_len, " "))
        else:
            print("*%s*" % msg.rjust(max_len, " "))
    print("*%s*" % (" " * max_len))
    print("*%s*" % ("*" * max_len))


def pri_fuck():
    msg = """
                       .::::.
                     .::::::::.
                    :::::::::::  
                ..:::::::::::'
              '::::::::::::'
                .::::::::::
           '::::::::::::::..
                ..::::::::::::.
              ``::::::::::::::::
               ::::``:::::::::'        .:::.
              ::::'   ':::::'       .::::::::.
            .::::'      ::::     .:::::::'::::.
           .:::'       :::::  .:::::::::' ':::::.
          .::'        :::::.:::::::::'      ':::::.
         .::'         ::::::::::::::'         ``::::.
     ...:::           ::::::::::::'              ``::.
    ```` ':.          ':::::::::'                  ::::..
                       '.:::::'     FUCK OFF       ':'````.."""
    print(msg)
    input("")


funs = [["Replace filename in Path", replace_mode], ["del filename in Path", delete_mode]]


def pri_welcome():
    pri_mag = ""
    for index, key in enumerate(funs):
        pri_mag += " %d. %s\n" % (index + 1, key[0])
    print_format("WELCOME", pri_mag)


def main():
    pri_welcome()
    user_code = input("Please input the Numbers : ")
    if user_code.isdigit() and 0 < int(user_code) < len(funs) + 1:
        funs[int(user_code) - 1][1]()
    else:
        pri_fuck()


if __name__ == "__main__":
    main()
