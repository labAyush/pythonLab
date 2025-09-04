original_dict = {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
n = 5
sorted_items = sorted(original_dict.items(), key=lambda item: item[1], reverse=True)
max_keys = [item[0] for item in sorted_items[:n]]
print(f"{n} maximum value(s) in the said dictionary: {max_keys}")