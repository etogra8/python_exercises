# # 1
# def greeting(name):
#     print("Hello {}" .format(name))

# greeting("John")

# # 2
# import matplotlib.pyplot as plot

# def f(x):
#     return x + 1

# xs = list(range(-3, 3))
# ys = []

# for x in xs:
#     ys.append(f(x))

# plot.plot(xs, ys)
# plot.show()

# # 3
# import matplotlib.pyplot as plot

# def f(x):
#     return x ** 2

# xs = list(range(-100, 100))
# ys = []

# for x in xs:
#     ys.append(f(x))

# plot.plot(xs, ys)
# plot.show()

# # 4
# import matplotlib.pyplot as plot

# def f(x):
#     if x % 2 == 0:
#         return -1
#     else:
#         return 1

# xs = list(range(-5, 5))
# ys = []

# for x in xs:
#     ys.append(f(x))

# plot.bar(xs, ys)
# plot.show()

# # 5
# import matplotlib.pyplot as plot
# from math import sin

# def f(x):
#     return sin(x)

# xs = list(range(-5, 5))
# ys = []

# for x in xs:
#     ys.append(f(x))

# plot.plot(xs, ys)
# plot.show()

# # 6
# import matplotlib.pyplot as plot
# from numpy import arange
# from math import sin

# def f(x):
#     return sin(x)

# xs = arange(-5, 6, 0.1)
# ys = []

# for x in xs:
#     ys.append(f(x))

# plot.plot(xs, ys)
# plot.show()

# # 7
# import matplotlib.pyplot as plot
# from numpy import arange

# def f(x):
#     return 1.8 * x + 32

# xs = arange(-3, 3, 0.1)
# ys = []

# for x in xs:
#     ys.append(f(x))

# plot.plot(xs, ys)
# plot.show()

# # 8
# def playAgain():
#     while True:
#         userIn = str(input("Do you want to play again? Enter (Y) for yes and (N) for no:  "))
#         userIn = userIn.upper()
#         if userIn == "Y":
#             print(userIn)
#         else:
#             return False

# playAgain()

# # 9
# def playAgain():
#     again = True  
#     while again == True:
#         userIn = input("Do you want to play again? Enter (Y) for yes and (N) for no: ")
#         userIn = userIn.upper()    
#         if userIn == "Y":
#             return True
#             break
#         elif userIn == "N":
#             return False
#         else:
#             print("Invalid request. Enter (Y) or (N).")
#             again

# playAgain()
        
