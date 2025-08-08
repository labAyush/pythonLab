#7. count even and odd numbers until input is 0
even = 0
odd = 0
while True:
    n = int(input("Enter number (0 to stop): "))
    if n == 0:
        break
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
print("Number of even numbers:", even)
print("Number of odd numbers:", odd)
