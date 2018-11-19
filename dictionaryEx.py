## Excercise 1
# phonebook_dict = {
#     "Alice": "703-493-1834",
#     "Bob": "857-284-1234",
#     "Elizabeth": "484-584-2923"
# }
## 1.1
# print(phonebook_dict["Elizabeth"])

## 1.2
# phonebook_dict["Kareem"] = "938-489-1234"

## 1.3
# del phonebook_dict["Alice"]

## 1.4
# phonebook_dict["Bob"] = "968-345-2345"

## 1.5
# print(phonebook_dict)

## 2
# ramit = {
#     "name": "Ramit",
#     "email": "ramit@gmail.com",
#     "interests": ["movies", "tennis"],
#     "friends": [
#         {
#             "name": "Jasmine",
#             "email": "jasmine@yahoo.com",
#             "interests": ["photography", "tennis"]
#         },
#         {
#             "name": "Jan",
#             "email": "jan@hotmail.com",
#             "interests": ["movies", "tv"]
#         }
#     ]
# }

## 2.1 Email address of Ramit
# print(ramit["email"])

## 2.2 prints Ramit's first interest
# print(ramit["interests"][0])

## 2.3 prints Jasmine's email
# print(ramit["friends"][0]["email"])

## 2.4 prints Jan's second interests
# print(ramit["friends"][1]["interests"][1])

## 3 Letter histogram
# word = "banana"
# tally = {}
# word = "".join(sorted(word))

# for i in word:
#     if i in tally:
#         tally[i] = tally[i] + 1
#     else:
#         tally[i] = 1

# print(tally)

## 4 Word histogram
# sentence = "To be or not to be"
# sentence = sentence.lower().split()
# tally = {}

# for i in sentence:
#     if i in tally:
#         tally[i] = tally[i] + 1
#     else:
#         tally[i] = 1

# print(tally)