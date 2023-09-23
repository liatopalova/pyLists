#задача 1

line = input("Enter a line please: ")
letter_count = 0
for char in line:
    if char.isalpha():
        letter_count += 1
print(f"Number of letters in line: {letter_count}")
digit_count = 0
for char in line:
    if char.isdigit():
        digit_count += 1
print(f"Number of digits in line: {digit_count}")


