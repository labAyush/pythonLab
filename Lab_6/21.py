original_dict = {'a': 5, 'b': 14, 'c': 32, 'd': 35}
max_key = max(original_dict, key=original_dict.get)
min_key = min(original_dict, key=original_dict.get)
print(f"Maximum and minimum key values: ('{max_key}', '{min_key}')")