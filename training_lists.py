example_list = [1, 2, 3, 4, 5, 6, 7]
print(len(example_list))
example_list.append('python')
print(example_list)
print(example_list[0])
print(example_list[-1])
print(example_list[:7])
print(example_list[1:4])
del example_list[2]
print(example_list)
print(len(example_list))
print(example_list.index(6))
example_list1 = ['Антонина', 'Янина', 'Владислав', 'Андрей']
list(reversed(example_list1))
print(list(reversed(example_list1)))
sorted(example_list1)
print(sorted(example_list1))
for s in sorted(example_list1):
	print(s)