# Write a Python program to print a dictionary in table format.
dict1 = {}

dict1 = {1: ["Akash", 21, 'Data Structures'],
		2: ["Amit", 20, 'Machine Learning'],
		3: ["Akashy", 21, 'OOPS with java'],
		}

print("{:<10} {:<10} {:<10}".format('NAME', 'AGE', 'COURSE'))


for key, value in dict1.items():
	name, age, course = value
	print("{:<10} {:<10} {:<10}".format(name, age, course))
