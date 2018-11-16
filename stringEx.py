## 1
# s = "hello"

# print(s.upper())

## 2
# s = "hello"

# newWord = s[0].upper() + s[1:]
# print(newWord)

## 3
# s = "hello"

# print(s[::-1])

## 4
# p = "Hello today welcome cat"
# p = p.upper()
# newWord = ''
# num = 0

# for i in p:
#     if i == " ":
#         newWord += " "
#     elif i == "H":
#         newWord += "#"
#     elif i == "E":
#         newWord += "3"
#     elif i == "L":
#         newWord += "1"
#     elif i == "O":
#         newWord += "0"
#     elif i == "T":
#         newWord += "7"
#     elif i == "D":
#         newWord += "|)"
#     elif i == "A":
#         newWord += "4"
#     elif i == "Y":
#         newWord += "j"
#     elif i == "W":
#         newWord += "\/\/"
#     elif i == "C":
#         newWord += "("
#     elif i == "M":
#         newWord += "|V|"

# print(newWord)
    
# 5
# s = "Spoon"

# s = s.replace("oo", "ooooo")

# print(s)

## 6
# s = "lbh zhfg hayrnea jung lbh unir yrnearq"
# a = "abcdefghijklmnopqrstuvwxyz"
# k = 13
# dec = ''
# #e(x) = (x + 13) % 26

# for i in s:
#     if i == " ":
#         dec += " "
#     elif i in a:
#         dec += a[(a.index(i) + k) % 26]

# print("Your decoded message is: " + dec)

