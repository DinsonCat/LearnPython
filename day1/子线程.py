from threading import Thread
import time


def println():
    print("--------heh---------")
    time.sleep(1)


def main():
    for i in range(5):
        t = Thread(target=println)
        t.start()


if __name__ == "__main__":
    main()
