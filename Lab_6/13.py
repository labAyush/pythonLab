my_dict = {'c': 3, 'a': 1, 'd': 4, 'b': 2}
sorted_items = sorted(my_dict.items(), key=lambda item: item[1])
sorted_dict = dict(sorted_items)
print(sorted_dict)