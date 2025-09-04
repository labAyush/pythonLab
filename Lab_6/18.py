my_dict = {'a': 50, 'b': 58, 'c': 56, 'd': 40, 'e': 100, 'f': 20}
sorted_values = sorted(my_dict.values(), reverse=True)
top_3_values = sorted_values[:3]
print(top_3_values)