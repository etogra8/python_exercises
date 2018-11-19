# entries = {
#     "John": "444-444-4444",
#     "Sandra": "555-555-5555",
#     "Phillip": "333-333-3333", 
#     "Mark": "777-777-7777"
# }




# while True:
#     print("Electronic Phone Book")
#     print("=====================")
#     print("1. Look up an entry")
#     print("2. Set an entry")
#     print("3. Delete an entry")
#     print("4. List all entries")
#     print("5. Quit")
#     userIn = int(input("What do you want to do? "))
#     if userIn == 5:
#         print("Bye")
#         break   
    
#         quit(userIn)

#     elif userIn == 1:
#         def lookUp(userIn):
#             name = input("Enter Name: ")
#             if name not in entries:
#                 print(entries.get(name))
#             elif name in entries:
#                 number = entries[name]
#                 print("Found entry for {name}: {number}" .format(name=name, number=number))

#         lookUp(userIn)

#     elif userIn == 2:
#         def setEntry(userIn):
#             name = input("Name: ")
#             number = input("Phone Number: ")
#             entries[name] = number
#             print("Entry stored for {name}." .format(name=name))

#         setEntry(userIn)

#     elif userIn == 3:
#         def delete(userIn):
#             name = input("Name; ")
#             del entries[name]
#             print("Entry for {name} has been deleted." .format(name=name))

#         delete(userIn)

#     elif userIn == 4:
#         def listAll(userIn):
#             count = 0
#             for key, value in entries.items():
#                 count += 1
#                 print("{count}. {key}: {value}" .format(count=count, key=key, value=value))
                    
#         listAll(userIn)