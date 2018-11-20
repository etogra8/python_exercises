# ## 1 Basics
# class Person:
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.friends = []

#     def greet(self, otherPerson):
#         print(f"Hello {otherPerson.name}, I am {self.name}")
        
# 1.1 Create an instance object of sonny
# sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")


# # 1.2 Create instance object of jordan
# jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

# # 1.3 sonny greets jordan
# Person.greet(sonny, jordan)

# # 1.4 jordan greets sonny
# Person.greet(jordan, sonny)

# # 1.5 prints Sonny's email and phone
# print(f"{sonny.name}'s email is {sonny.email}. His phone number is {sonny.phone}")

# # 1.6 prints Jordan's email and phone
# print(f"{jordan.name}'s email is {jordan.email}. His phone number is {jordan.phone}")

## 2 Creating a class and adding method to print make, model, and year of car
# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def printInfo(self):
#         print(f"{self.year} {self.make} {self.model}")

# car = Vehicle("Nissan", "Altima", "2015")
# Vehicle.printInfo(car)

## adding method to print contact info of person
# class Person:
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone
#     def greet(self, otherPerson):
#         print(f"Hello {otherPerson.name}, I am {self.name}")
    
#     def printInfo(self):
#         print(f"{self.name}'s email: {self.email}, {self.name}'s phone number: {self.phone}")


# sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
# jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

# sonny.printInfo()

## add addFriends method and numFriends method
# class Person:
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.friends = []
#     def greet(self, otherPerson):
#         print(f"Hello {otherPerson.name}, I am {self.name}")
    
#     def printInfo(self):
#         print(f"{self.name}'s email: {self.email}, {self.name}'s phone number: {self.phone}")

#     def addFriends(self, friend):
#         self.friends.append(friend)

#     def numFriends(self):
#         print(len(self.friends))


# sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
# jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

# jordan.addFriends(sonny)
# sonny.addFriends(jordan)
# jordan.numFriends()

## Count number of greetings for each person
# class Person:
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.friends = []
#         self.greetingCount = 0

#     def greet(self, otherPerson):
#         print(f"Hello {otherPerson.name}, I am {self.name}")
#         self.greetingCount += 1
    
#     def printInfo(self):
#         print(f"{self.name}'s email: {self.email}, {self.name}'s phone number: {self.phone}")

#     def addFriends(self, friend):
#         self.friends.append(friend)

#     def numFriends(self):
#         print(len(self.friends))


# sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
# jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

# sonny.greet(jordan)
# sonny.greet(jordan)
# print(sonny.greetingCount)

## obj to string 
# class Person:
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.friends = []
#         self.greetingCount = 0

#     def greet(self, otherPerson):
#         print(f"Hello {otherPerson.name}, I am {self.name}")
#         self.greetingCount += 1
    
#     def printInfo(self):
#         print(f"{self.name}'s email: {self.email}, {self.name}'s phone number: {self.phone}")

#     def addFriends(self, friend):
#         self.friends.append(friend)

#     def numFriends(self):
#         print(len(self.friends))

#     def objToString(self):
#         print(f"Person: {self.name} {self.email} {self.phone}")
        
# sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
# jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")


# sonny.objToString()

## count unique greeted people people 

# class Person:
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.friends = []
#         self.greetingCount = 0
#         self.uniqueGreets = []

#     def greet(self, otherPerson):
#         print(f"Hello {otherPerson.name}, I am {self.name}")
#         self.greetingCount += 1
#         if otherPerson in self.uniqueGreets:
#             pass
#         else:
#             self.uniqueGreets.append(otherPerson)
    
#     def printInfo(self):
#         print(f"{self.name}'s email: {self.email}, {self.name}'s phone number: {self.phone}")

#     def addFriends(self, friend):
#         self.friends.append(friend)

#     def numFriends(self):
#         print(len(self.friends))

#     def objToString(self):
#         print(f"Person: {self.name} {self.email} {self.phone}")

#     def uniqueGreetsCount(self):
#         print(len(self.uniqueGreets))
        
# sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
# jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")
# mark = Person("Mark", "mark@gmail.com", "444-333-5555")

# sonny.greet(jordan)
# sonny.greet(jordan)
# sonny.greet(mark)
# sonny.greet(mark)
# sonny.greet(mark)
# sonny.uniqueGreetsCount()
# print(sonny.greetingCount)

