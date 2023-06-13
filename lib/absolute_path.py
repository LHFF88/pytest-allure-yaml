import os


def absolutes_path():
    absolute_path = (os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    return absolute_path
