import datetime
import sys


def get_current_date():
    """
    :return: DateTime object
    """
    return datetime.datetime


def get_current_platform():
    """
    :return: current platform
    """
    return sys.platform
    
def countNumbers(switch):
    return list(range(2 if switch else 1, 100, 2))
    
def functionWithException(int):
    return int + 1
