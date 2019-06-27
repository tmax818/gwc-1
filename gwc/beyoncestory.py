start = '''
It's your first day on the job and Beyonce is getting ready for a red carpet.
You are her assistant and your goal is to make all the right choices so that you don't get FIRED!
'''

keepplaying = "yes"
print(start)

while keepplaying == "Yes" or keepplaying == "yes":
	userChoice = input("What are you getting Beyonce for breakfast? Type 1 for yogurt, granola, and strawberries. Type 2 for garbage. ")
	if userChoice == "1":
		print("She nods at you for choosing the healthy breakfast. ")
		print("Congrats. You have survived your first task. ")
		print("")
		keepplaying = "no"
	elif userChoice == "2":
		print("She glares at you disapprovingly and then has her team of lawyers send you a termination letter. ")
		print("You failed your first task, ")
		keepplaying = input("Would you like to try again? Type yes or no. ")
		if keepplaying == "no":
			quit()
	else:
		print("Please select one of the valid options: 1 or 2. ")
		keepplaying = input("Would you like to try again? Type yes or no. ")
		if keepplaying == "no":
			quit()

keepplaying = "yes"
while keepplaying == "Yes" or keepplaying == "yes":
	userChoice = input("She asks you to FaceTime her daughter. Who are you FaceTiming, Blue or Rumi? Type 1 for Blue. Type 2 for Rumi. ")
	if userChoice == "1":
		print("She FaceTimes Blue and is now in a good mood. ")
		print("Congrats. You have passed your second task. ")
		print("")
		keepplaying = "no"
	elif userChoice == "2":
		print("She says 'She’s only 2....' and then has her team of lawyers send you a termination letter. ")
		keepplaying = input("Would you like to try again? Type yes or no. ")
		if keepplaying == "no":
			quit()
	else:
		print("Please select one of the valid options: 1 or 2. ")
		keepplaying = input("Would you like to try again? Type yes or no. ")
		if keepplaying == "no":
			quit()

keepplaying = "yes"
while keepplaying == "Yes" or keepplaying == "yes":
	userChoice = input("Beyonce needs something to do while she waits for hair and makeup. What do you suggest? Type 1 for swimming. Type 2 for gossiping. Type 3 for painting. ")
	if userChoice == "1":
		print("She goes swimming and her hair is ruined by the chlorine. You are fired. ")
		keepplaying = input("Would you like to try again? Type yes or no. ")
		if keepplaying == "no":
			quit()
	elif userChoice == "2":
		print("She rolls her eyes and says, 'I am not petty like you clearly are.' She fires you and calls a new assistant. ")
		keepplaying = input("Would you like to try again? Type yes or no. ")
		if keepplaying == "no":
			quit()
	elif userChoice == "3":
		print("She begins to paint and is able to relax. ")
		print("Congrats. You have passed your third task. ")
		print("")
		keepplaying = "no"
	else:
		print("Please select one of the valid options: 1 or 2. ")
		keepplaying = input("Would you like to try again? Type yes or no. ")
		if keepplaying == "no":
			quit()

keepplaying = "yes"
while keepplaying == "Yes" or keepplaying == "yes":
	userChoice = input("She tells you to play one of her songs as she paints. Which song do you play? Hit 1 for Run the World (Girls). Hit 2 for If I Were a Boy. ")
	if userChoice == "1":
		print("She dances along. ")
		print("Congrats. You have passed your task. ")
		print("")
		keepplaying = "no"
	elif userChoice == "2":
		print("She starts crying and fires you on the spot. ")
		keepplaying = input("Would you like to try again? Type yes or no. ")
		if keepplaying == "no":
			quit()
	else:
		print("Please select one of the valid options: 1 or 2. ")
		keepplaying = input("Would you like to try again? Type yes or no. ")
		if keepplaying == "no":
			quit()

keepplaying = "yes"
while keepplaying == "Yes" or keepplaying == "yes":
	userChoice = input("She is running late for her event. Should she go to the hotel or get ready in the car? Type 1 for the hotel. Type 2 for the car. ")
	if userChoice == "1":
		print("She makes it to the hotel. ")
		print("Congrats. You have passed your task. ")
		print("")
		keepplaying = "no"
	elif userChoice == "2":
		print("She got carsick and threw up on her outfit. You get kicked out the car and fired. ")
		keepplaying = input("Would you like to try again? Type yes or no. ")
		if keepplaying == "no":
			quit()
	else:
		print("Please select one of the valid options: 1 or 2. ")
		keepplaying = input("Would you like to try again? Type yes or no. ")
		if keepplaying == "no":
			quit()

keepplaying = "yes"
while keepplaying == "Yes" or keepplaying == "yes":
	userChoice = input("The paparazzi have swarmed the hotel. Should she risk being spotted or run late and go to another hotel? Type 1 to risk being spotted. Type 2 to leave. ")
	if userChoice == "1":
		print("She was thankfully not spotted. ")
		print("Congrats. You have passed your task. ")
		print("")
		keepplaying = "no"
	elif userChoice == "2":
		print("You get stuck in traffic and she misses the event completely. You have been fired. ")
		keepplaying = input("Would you like to try again? Type yes or no. ")
		if keepplaying == "no":
			quit()
	else:
		print("Please select one of the valid options: 1 or 2. ")
		keepplaying = input("Would you like to try again? Type yes or no. ")
		if keepplaying == "no":
			quit()
