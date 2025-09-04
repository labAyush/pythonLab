sample_string = 'engineerings'
letter_count = {}
for letter in sample_string:
    letter_count[letter] = letter_count.get(letter, 0) + 1
print(letter_count)