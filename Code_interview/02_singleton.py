'''实现单例模式
'''
import time
import threading
from functools import wraps


# __new__方法实现，init函数每次初始化都会执行
class Singleton_1(object):
    # _instance = None

    def __new__(cls, *args, **kwargs):
        print('Singleton_1 __new__')
        if not hasattr(cls, "_instance"):
            cls._instance = object.__new__(cls)
        print(cls._instance)
        return cls._instance


# 加了多线程锁
class Singleton_2(object):
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with cls._instance_lock:
                if not hasattr(cls, "_instance"):
                    print('new singleton class')
                    cls._instance = object.__new__(cls)
        return cls._instance


# 元类实现，init函数只会执行一次
class Singleton_3(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        print('Singleton_3 __call__')
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton_3, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


# 装饰器实现
def singleton(cls):
    instances = {}
    @wraps(cls)
    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return getinstance


class Foo(metaclass=Singleton_3):
    def __init__(self):
        print('Foo __init__')

    def __new__(cls):
        print("Foo __new__")
        return super(Foo, cls).__new__(cls)


@singleton
class Foo_1():
    def __init__(self):
        print('Foo __init__')


if __name__ == '__main__':
    obj1 = Foo()
    print('-' * 20)
    obj2 = Foo()
    print(obj1, obj2)

    # def task():
    #     obj = Foo()
    #     print(obj)

    # for i in range(10):
    #     t = threading.Thread(target=task)
    #     # time.sleep(1)
    #     t.start()

