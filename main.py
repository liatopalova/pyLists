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

#задача 2

string = input("Enter a line please: ")
letter = input("Enter a symbol:")
symbol_count = string.count(letter)
print(f"Number of symbols in string: {symbol_count}")

#задача 3

text = input("Enter text: ")
word = input("Enter word: ")
if word in text:
    repl = input("Enter word for replace: ")
    repl_text = text.replace(word, repl)
    print(f"New text: {repl_text}")
else:
    print("Error!")

#задача 4

text_line = "Lorem ipsum dolor sit amet, consectetur adipiscing"
print(text_line[2:3])
text_line_rev = text_line[::-1]
print(text_line_rev[1:2])
print(text_line[:5])
print(text_line[:-2])
print(text_line[0::2])
print(text_line[1::2])
print(text_line[::-1])
print(text_line[-1::-2])
print(len(text_line))

#додатково

some_text = "nay, thou 1 art not dead. ukraine,and 2 the skies! a brethren,smile 3: once more!!!"

new_text = ""
capitalize_next = True
for char in some_text:
    if capitalize_next and char.isalpha():
        new_text += char.upper()
        capitalize_next = False
    else:
        new_text += char

    if char in [".", "!", "?"]:
        capitalize_next = True
print(new_text)

digit_count = 0
for char in some_text:
    if char.isdigit():
        digit_count += 1
print(f"Number of digits in line: {digit_count}")

pun_mark = [",", ".", "!", ":", ";", "?", "-"]
result = 0
for char in some_text:
    if char in pun_mark:
        result += 1
print(f"Punctuation: {result}")

ex_mark = "!"
result = 0
for ex_mark in some_text:
    if ex_mark == "!":
        result += 1
print(f"Exclamation: {result}")

