import functools


def eat_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("いただきます")
        result = func(*args, **kwargs)
        print("ごちそうさまでした")
        return result
    return wrapper


@eat_decorator
def eat_food():
    print("もぐもぐ...")


if __name__ == "__main__":
    eat_food()
