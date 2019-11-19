# import random

# # create variable for loop
# cont = 'y'

# while cont == 'y':
# # Get a random number
# 	rand_num = random.randint(1,10)
# 	#print(rand_num)
# 	correct = False

# 	while correct == False:

# # Get the user's guess
# 		guess = input("Guess a number between 1 and 10: ")
# 		guess = int(guess)

# # Compare the guess to the random number. If the number is the same,
# # tell the user they won, and ask them if they want to play again.
# # If the number is different, ask them to try again.
	
# 		if guess:
# 			if rand_num == guess:
# 				print("You're a freaking genius! You got it!")
# 				correct = True
# 				cont = input("Do you want to keep playing? (y/n) ")
# 				if (cont != 'y'):
# 					print("Thanks for playing, loser!")
# 					break
# 			elif rand_num > guess:
# 				print("Too low! Try again!")
# 			else:
# 				print("Too high! Try again!")
# 		else: 
# 			print("Something went wrong!")


# # Instructor solution 1
# rand_num = random.randint(1,10)
# guess = None

# while guess != rand_num:
# 	guess = input("Pick a number from 1 to 10: ")
# 	guess = int(guess)
# 	if guess > rand_num:
# 		print("Too high!")	
# 	elif guess < rand_num:
# 		print("Too low!")
# 	else:
# 		print("You got it!")


# Instructor solution 2
rand_num = random.randint(1,10)
guess = None

while True:
	guess = input("Pick a number from 1 to 10: ")
	guess = int(guess)
	if guess > rand_num:
		print("Too high!")	
	elif guess < rand_num:
		print("Too low!")
	else:
		print("You got it!")
		play_again = input("Do you want to play again? (y/n)")
		if play_again == "y":
			rand_num = random.randint(1,10)
			guess = None
		else:
			print("Thanks for playing")
			break