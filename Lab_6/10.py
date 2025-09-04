my_dict = {'name': 'Hari', 'city': 'Bhaktapur'}
# The key 'age' does not exist, so it returns the default value
age = my_dict.get('age', 'Key not available')
print(age)