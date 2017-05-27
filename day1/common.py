import time


def timer(func):
    def deco(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(end_time - start_time)

    return deco


@timer
def print_hello(name, age):
    time.sleep(2)
    print("hello %s! you are %s year old?" % (name, age))


print_hello("dinson", 10)
