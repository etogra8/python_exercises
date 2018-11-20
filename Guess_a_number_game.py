# Guess a number Game

## Step 1 create game with guess equal to 5

# guess = int(input("I am thinking of a number between 1 and 10. What is it? "))
# while guess != 5:
#     guess = int(input("Nope, thats not it. Try again?"))
#     if guess == 5:
#         break

# print("You got it")

# Step 2 Add high and low hints to game
# guess = int(input("I am thinking of a number between 1 and 10. What is it? "))

# while guess != 5:
#     if guess == 5:
#         break
#     elif guess < 5:
#         guess = int(input("%d is too low. What's the number? " % guess))
#     elif guess > 5:
#         guess = int(input("%d is too high. What's the number? " % guess))
#     else:
#         print("Not a number. Enter a number between 1 and 10.")

# print("You got it")

## Step 3 implement random integer into game
# import random

# secretNumber = random.randint(1,10)
# guess = int(input("I am thinking of a number between 1 and 10. What is it? "))

# while guess != secretNumber:
#     if guess == secretNumber:
#         break
#     elif guess < secretNumber:
#         guess = int(input("%d is too low. What's the number? " % guess))
#     elif guess > secretNumber:
#         guess = int(input("%d is too high. What's the number? " % guess))
#     else:
#         print("Not a number. Enter a number between 1 and 10.")

# print("You got it")

## Step 4 Added limit of 5 turns to game
# import random

# secretNumber = random.randint(1,10)
# guess = int(input("I am thinking of a number between 1 and 10. What is it? "))
# turn = 5

# while turn >= 1:
#     turn -= 1
#     print("Turns left: ", turn)
   
#     if turn == 0:
#         print("You lose")
#     elif guess == secretNumber:
#         print("You win")      
#         break
#     elif guess < secretNumber:
#         guess = int(input("%d is too low. What's the number? " % guess))
#     elif guess > secretNumber:
#         guess = int(input("%d is too high. What's the number? " % guess))
#     else:
#         print("Not a number. Enter a number between 1 and 10.")
    
    
## Bonus: Added new choice for player to replay game when player wins
# import random

# secretNumber = random.randint(1,10)

# turn = 5
# while turn >= 1:
#     if turn == 5:
#         guess = int(input("I am thinking of a number between 1 and 10. What is it? "))
#     else:
#         pass
#     turn -= 1
#     print("Turns left: ", turn)
    
#     if turn == 0:
#         print("You lose")
#     elif guess == secretNumber:
#         print("You win")
#         again = input("Do you want to play again. Enter (Y) or (N): ")
#         if again == "Y":
#             turn = 5
#         elif again == "N":
#             print("Bye")
#             break
#     elif guess < secretNumber:
#         guess = int(input("%d is too low. What's the number? " % guess))
#     elif guess > secretNumber:
#         guess = int(input("%d is too high. What's the number? " % guess))
#     else:
#         print("Not a number. Enter a number between 1 and 10.")

