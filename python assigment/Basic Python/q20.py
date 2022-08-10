# Write a Python program to sort three integers without using conditional statements and
# loops.
first_integer=int(input("Enter first integer "))
second_integer=int(input("Enter second integer "))
third_integer=int(input("Enter Third integer "))

minmum=min(first_integer,second_integer,third_integer)
maximum=max(first_integer,second_integer,third_integer)

middium=(first_integer + second_integer + third_integer)-minmum-maximum

print(minmum,middium,maximum)
