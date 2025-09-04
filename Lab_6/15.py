num_dict = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
sorted_num_dict = {}
for key, value in num_dict.items():
    sorted_num_dict[key] = sorted(value)
print(sorted_num_dict)