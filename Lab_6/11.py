my_dict = {'math': 90, 'science': 95, 'english': 90}
value_to_find = 90
keys_with_value = []
for key, value in my_dict.items():
    if value == value_to_find:
        keys_with_value.append(key)
print(keys_with_value)