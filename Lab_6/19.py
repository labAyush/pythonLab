original_dict = {'c1': 'Red', 'c2': 'Green', 'c3': None}
new_dict = {key: value for key, value in original_dict.items() if value is not None}
print(new_dict)