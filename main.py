import random

# Introduction
print("Welcome to Camel!")
print("You have stolen a camel to make your way across the Mobi Desert.")
print("The natives want their camel back and are chasing you down! Survive your")
print("Desert trek and out run the natives.\n")

# Variables
done = True
milesTraveled = 0
nativesTraveled = -20
camelTiredness = 0
thirst = 0
canteen = 3
oasis = -1

# Game Strts
while (done):
        
	# Options
	print("\nOptions:")
	print("A. Drink from your canteen.")
	print("B. Ahead moderate speed.")
	print("C. Ahead full speed.")
	print("D. Stop for the night.")
	print("E. Status check.")
	print("Q. Quit Game.")
	print("\n")

	# User's input (Erase spaces and Capitalize)
	option = input("What will you do? ").strip().upper()

	# Q: Quit Game
	if option == "Q" :
		done = False

	# E: Status Check
	elif option == "E" :
		print("Miles traveled: " + str(milesTraveled))
		print("Drinks in canteen: " +  str(canteen))
		print("The natives are " + str(milesTraveled - nativesTraveled) + " miles behind you.\n")


	# D: Stop for a night
	elif option == "D" :
		print("\nYou stop for a night.")
		print("Your camel is happy.")
		print("The natives don't stop.\n")
		camelTiredness = 0
		nativesTraveled += random.randrange(7, 15)

	# C: full speed ahead
	elif option == "C" :
		miles = random.randrange(10, 21)
		milesTraveled += miles
		thirst += 1
		camelTiredness += random.randrange(1, 4)
		nativesTraveled += random.randrange(7, 15)
		oasis = random.randrange(20)
		if oasis == 10 :
			thirst = 0
			camelTiredness = 0
			canteen = 3
			print("\nAs you travel you happen upon an oasis!")
			print("You fill your canteen and your stomach with water, and")
			print("Your camel is rested!")
			print("The natives continue the chase.\n")
		else :
			print("\nYou push onward at full speed, moving a total of " + str(miles) + " miles")
			print("Your thirst increases.")
			print("The natives continue the chase.\n")

	# B: Moderate speed speed ahead
	elif option.upper() == "B" :
		miles = random.randrange(5, 13)
		milesTraveled += miles
		thirst += 1
		camelTiredness += 1
		nativesTraveled += random.randrange(7, 15)
		oasis = random.randrange(20)
		if oasis == 10 :
			thirst = 0
			camelTiredness = 0
			canteen = 3
			print("\nAs you travel you happen upon an oasis!")
			print("You fill your canteen and your stomach with water, and")
			print("Your camel is rested!")
			print("The natives continue the chase.\n")
		else :
			print("\nYou move forward, moving a total of " + str(miles) + " miles")
			print("Your thirst increases.")
			print("The natives continue the chase.\n")

	# A: Drink from your canteen
	elif option.upper() == "A" :
		if canteen > 0 :
			canteen -= 1
			thirst = 0
			print("\nYou take a drink")
		else:
			print("\nYour canteen is empty. You imagine yourself as a lifeless, dry husk.")

	# Alerts: Thirst
	if thirst > 5 :
		print("\nYou died of thirst!")
		print("Game Over.\n")
		done = True
	elif thirst > 4 :
		print("\nYou are thirsty!")

	# Alerts: Camel's tiredness
	if camelTiredness > 8 :
		print("\nYour camel died of exhaustion!")
		print("With no camel, the natives catch up to you and kill you")
		print("on the spot.")
		print("Game Over.\n")
		done = True
		milesTraveled = 0
		nativesTraveled = -20
		camelTiredness = 0
		thirst = 0
		canteen = 3
		oasis = -1
	elif camelTiredness > 5 :
		print("\nYour camel is tired.\n")

	# Alerts: Successfully Escape + Reset Status
	if milesTraveled >= 200 :
		print("\nCongratulations! You have crossed the entire desert!")
		print("You win!\n")
		done = True
		milesTraveled = 0
		nativesTraveled = -20
		camelTiredness = 0
		thirst = 0
		canteen = 3
		oasis = -1

	# Alerts: Natives distance from you
	if milesTraveled - nativesTraveled <= 0 :
		print("\nThe natives have caught up with you!")
		print("They kill you on the spot, and take their camel back.")
		print("Game Over.\n")
		done = True
		milesTraveled = 0
		nativesTraveled = -20
		camelTiredness = 0
		thirst = 0
		canteen = 3
		oasis = -1
	elif milesTraveled - nativesTraveled < 15 :
		print("\nYou see faint shapes on the horizon behind you.")
		print("The natives are getting close!\n")

# Exit message
print("\nExiting Game. Goodbye.\n")