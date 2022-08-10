# Write a Python program to remove the first occurrence of a specified element from an array 
from array import array


array=[4,5,4,5,8,9,5,5]
print("Occurrences of the integer 5 is: "+str(array.count(5)))
array.remove(5)
print(array)