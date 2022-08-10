# Write a Python program to concatenate all elements in a list into a string and return it
from unittest import result


def concatenate_list_data(list):
    result=''
    for element in list:
        result += str(element)
    return result

print(concatenate_list_data([2,5,13,2]))
