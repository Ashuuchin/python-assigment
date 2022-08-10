# Write a Python program to convert a list into a nested dictionary of keys.

test_list1 = ["gfg", 'is', 'best']
test_list2 = ['ratings', 'price', 'score']
test_list3 = [5, 6, 7]

print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))
print("The original list 3 is : " + str(test_list3))

res = [{a: {b: c}} for (a, b, c) in zip(test_list1, test_list2, test_list3)]


print("The constructed dictionary : " + str(res))

# Method 2
num_list = [1, 2, 3, 4]
new_dict = current = {}
for name in num_list:
    current[name] = {}
    current = current[name]
print(new_dict)
