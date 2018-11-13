#1
# first_name = input("What is your name? ")
# sentence = "Good morning %s." % first_name

# print(sentence)

#2
# first_name = input("Type your first name: ")
# first_name = first_name.upper()
# sentence = "Hello %s, nice to meet you." % first_name

# print(sentence)

#3
# print("Complete the sentence below.")
# print("___(name)___'s favorite color is ___(color)___.")

# name = input("What is name? ")
# color = input("What is color? ")

# print("%s's favorite color is %s." % (name, color))

#4
# day = int(input("Chose a day (0-6): "))

# if day == 0:
#     print("Sunday")
# elif day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# elif day == 4:
#     print("Thursday")
# elif day == 5:
#     print("Friday")
# elif day == 6:
#     print("Saturday")
# else:
#     print("%s is not between 0 and 6" % day)

#5
# day = int(input("Chose a day (0-6): "))

# if day <= 4:
#     print("Go to work")
# else:
#     print("Sleep in")

#6
# degC = int(input("Enter temperature in C: "))

# degF = degC * 1.8 + 32
# print("%s F" % degF)

#7
# bill = int(input("Enter the bill total: "))
# service = input("Enter the level of service (good, fair, or bad): ")
# service = service.lower()

# if service == "good":
#     tip = bill * .2
#     total = bill + tip
#     print("Tip amount: ${:.2f}" .format(tip))
#     print ("Total amount: ${:.2f}" .format(total))
# elif service == "fair":
#     tip = bill * .15
#     total = bill + tip
#     print("Tip amount: ${:.2f}" .format(tip))
#     print("Total amount: ${:.2f}" .format(total))
# elif service == "bad":
#     tip = bill * .1
#     total = bill + tip
#     print("Tip amount: ${:.2f}" .format(tip))
#     print("Total amount: ${:.2f}" .format(total))
# else:
#     print("Enter a valid level of service.")

#8
# bill = int(input("Enter bill total: "))
# service = input("Enter level of service (good, fair, or bad): ").lower()
# split = int(input("Split how many ways? "))

# if service == "good":
#     tip = bill * .2
#     total = bill + tip
#     perPerson = total / split
#     print("Tip amount: ${:.2f}" .format(tip))
#     print("Total amount: ${:.2f}" .format(total))
#     print("Amount per person: ${:.2f}" .format(perPerson))
# elif service == "fair":
#     tip = bill * .15
#     total = bill + tip
#     perPerson = total / split
#     print("Tip amount: ${:.2f}" .format(tip))
#     print("Total amount: ${:.2f}" .format(total))
#     print("Amount per person: ${:.2f}" .format(perPerson))
# elif service == "bad":
#     tip = bill * .1
#     total = bill + tip 
#     perPerson = total / split
#     print("Tip amount: ${:.2f}" .format(tip))
#     print("Total amount: ${:.2f}" .format(total))
#     print("Amount per person: ${:.2f}" .format(perPerson))
# else:
#     print("Enter a valid level of service.")

#9.1
# count = 1

# while count <= 10:
#     print(count)
#     count += 1

#10
# count = 0

# while True:
#     print("You have %d coins." % count)
#     count += 1
#     answer = input("Do you want another? ").lower()
#     if answer == "no":
#         break
# print("Bye")