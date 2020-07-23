import os
import time


def get_time_string():
    return time.strftime("%Y%m%d-%H%M%S")


def delete_file(filedir):
    try:
        os.remove(filedir)
    except FileNotFoundError:
        pass
