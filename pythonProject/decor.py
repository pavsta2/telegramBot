import timeit
import time
from functools import wraps


def dec(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        wrapper
        :param args:
        :param kwargs:
        :return:
        """
        # start = time.time()
        a = func(*args, **kwargs)
        print(timeit.timeit(stmt="time.sleep(1.2)", number=1))
        return a

    return wrapper


@dec
def my_func():
    """
    my_func
    :return:
    """
    time.sleep(1.2)


if __name__ == '__main__':

    my_func()