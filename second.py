
import random
name = input("What's your name?")
print("Hello", name)
print ("We will play a game")
numbers = [1, 2, 3, 4]
random_number = random.choice(numbers)
number_chosen = int(input("Choose a number between 1 and 4"))
if (random_number == number_chosen) :
  print ("Congratulations, you have won")
else:
 print ("Sorry, you have lost, the number was", random_number)