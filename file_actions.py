from typing import *

def calc_sum_of_numbers_in_file(filename: str) -> int:
    """
    Calculates the sum of all the numbers found in the file ./files/<filename>".
    """
    file = open("./files/{}".format(filename))
    data = file.read().split(",")
    
    sum = 0
    for item in data:
        sum += int(item)

    return sum


