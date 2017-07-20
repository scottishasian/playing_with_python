from sys import exit



def the_end():
	print "As you can see this room is a dead end."
	print "Here we present you with a simple test."
	print "On a scale of 1 to 10, how cool am I?"
	
	try:
		next = float(raw_input("> "))
	except ValueError:
		dead("You are an awful person, goodbye.")
		
	if next > 7:
		print "Oh well, thank you, I do try. You are free to go"
		exit(0)
	else:
		dead("Well that isn't too nice. Away to the pits with you!")
	
		
def top_middle_room():
	print "Almost near the end, I think."
	print "Please try and open the door."
	
	next = raw_input("> ")
	
	if next == "Open door" and key == 1:
		print "You opened the door, well done, on you go."
		#Won't read that key is +1 if the key was chosen in the previous room.
	elif next == "sing sweet caroline":
		print "That worked... somehow..."
		the_end()
		
	else:
		dead("You can't open the door without a key. Oh well, turning on the gas.")
		
def top_right_room():
	print "Now time for a quiz."
	
	questions = {
		"What is the capital of Paris?": ['a. Paris is the capital of France you fool!', 'b. What is a Paris', 'c. I don\'t know.', 'a'],
		"What colour is red?": ['a. Blue', 'b. Red', 'c. An apple', 'b']
	}
		
	score = 0
	
	for question_number, question in questions:
		print ("Question", question_number + 1)
		print question
		for options in questions[question][:-1]:
			print (options)
		user_choice = input("Please choose now: ")
		if user_choice == questions[question][-1]:
			print ("Correct!")
			score += 1
		else:
			print ("Wrong!")
			
	if score == 2:
		top_middle_room()
	else:
		dead("Not enough points")
		
		#currently broken

		
def top_left_room():
	key = 0
	print "Well that was quite the entrance!"
	print "Almost there, in this room there are three items. You may take one."
	print "Please choose now."
	print "Would you like item 1. a chunky plastic key?"
	print "Or item 2. a knife with a spoon duct taped to it?"
	print "Or item 3. a picture of Neil Diamond"
	
	next = raw_input("> ")
	
	if next == "1":
		print "Interesting choice, please proceed to the next room."
		key += 1
		top_middle_room()
		
	elif next == "2":
		print "A fine choice, you never know when you will need a knifey spooney. Please head to the next room."
		top_middle_room()
		
	elif next == "3":
		print "Sweet...caroline! Well on you go to the next room."
		top_middle_room()
		
	else:
		dead("You don't want one of the fine gifts I am offering? How rude!")
	
	
def centre_right_room():
	print "Congratulations in making it this far."
	print "At Xper Co, we believe in making sure out candidates remain healthy."
	print "Please help yourself to some of the food in this room."
	print "How many dishes would you like?"
	
	try:
		next = float(raw_input("> "))
		
	except ValueError:
		dead("Oh dear, you have chosen not to eat, looks like you have starved to death.")
		
	if (next) < 10:
		print "That is a healthy attitude, you don't want to eat too much. On your way now."
		top_right_room()
		
	else:
		dead("You want HOW much? You greedy bastard! Fine, you will have all the food now.. Sealing doors.")

def centre_left_room():
	print "At Xper Co, we love literary classics, such as Alice in Wonderland. So please thank Lewis Carrol"
	print "for this next test."
	print "On the table in front of you, there are three edible items, please choose one."
	print "One of the items will help you proceed."
	print "The first item is a cupcake that says 'Eat me'."
	print "The second item is a bottle that says 'Drink me'."
	print "The last item is a cloth that has 'chloroform' scored out and 'sniff me' hastily written in."
	
	next = raw_input("> ")
	
	if next == "eat cupcake":
		print "You chose to '%s '." % next
		print "The cupcake is rather bland tasting, but it gives you an odd headrush. You notice your hands turning green."
		print "You feel yourself growing taller, you hear your trousers and shirt rip."
		print "In a confused rage, you run at the wall."
		top_left_room()
		
	elif next == "drink the bottle":
		print "You chose to '%s '." % next
		dead("Entry 4: Subject drank the liquid and proceeded to shrink at an exponential rate. We can not detect subject in the room anymore.")
	
	elif next == "sniff cloth":
		print "You proceed to '%s '." % next
		print "You sniff the cloth.. everything goes a bit fuzzy...spinning...then black."
		start()
		
	else:
		dead("Unfortunately you have not chosen anything. We shall now release the Queen of Hearts.")

def right_room():
	print "This is the right room"
	print "Being the right room, it was the right choice to make."
	print "Please proceed and claim your prize."
	print "Do you choose prize A. A brand new car!"
	print "Or prize B. A wonderous glowing orb that looks like it is made of liquid."
	print "Or is it prize C. you desire, a 200 year gym pass."
	print "Please choose now."
	
	next = raw_input("> ")
	
	if next == "a":
		print "Please, feel free to test drive it now!"
		
		again = raw_input("> ")
		
		if again == "turn on car":
			dead("Oh, I am sorry, that was the wrong prize and this is the wrong room. Goodbye.")
		
		elif again == "do nothing":
			print "That was a good choice. Please head to the next room now, on you trot."
			centre_right_room()
		
		else:
			dead("That was an odd thing to do to a car. Goodbye")
			
	elif next == "b":
		print "Go on, touch it."
		start()
		
		
	elif next == "c":
		print "Please proceed this way to your new personal trainer."
		left_room()
		
	else:
		dead("Oh, you don't want a prize?")


def left_room():
	print "Welcome to the left room."
	print "Here we will test your ability to manouvere past our guard to access the next room."
	print "The door guard for this scenario is a powerful seal."
	print "Please specify how you will approach this situation based on these three options."
	print "A. Fight the guard"
	print "B. Give it the conveniently placed bucket of fresh fish that is next to you."
	print "C. Seduce the guard"
	powerful_seal = False
	
	while True:
		next = raw_input("> ")
	
		if next == "a":
			dead("You have managed to lightly bruise the guard, but as a seal that benches 150kg, it crushes you.")
			
		elif next == "b" and not powerful_seal:
			print "The seal takes your gift and proceeds to eat, you can now move to the door."
			powerful_seal = True
			
		elif next == "b" and powerful_seal:
			dead("'Nah mate, already eaten, time to die'")
			
		elif next == "open door" and powerful_seal:
			centre_left_room()
			
		elif next == "c":
			dead("You try to seduce the seal, but it is a seal and you fail.")
		
		else:
			dead("You do nothing and the seal throws its weights at you.")

def centre_room():
	print "Welcome to the central room."
	print "Please move to the plate in the centre of the room."
	print "Would you kindly ignore the cake in the corner of the room, it is mine."
	
	next = raw_input("> ")
	
	if next == "move to the plate":
		print "Well done, now please press either the red of blue buttons on the plate."
		
		again = raw_input(">")
		
		if again == "press red" or "red":
			right_room()
		elif again == "press blue" or "blue":
			dead("Engaging death ray, targeting central plate.")
		else:
			dead("That is not what was asked of you. Goodbye.")
			
	elif next == "eat cake":
		dead("That was my cake, how dare you! Engaging termination protocol!")
		#Having an "or" clause at this point allows the user to press any key to engage it,
		# thus over-writing the else function.
			
	else:
		dead("You have chosen to do nothing. Goodbye.")

def dead(why):
	print why, "Thank you for providing us with test data."
	exit(0)

def start():
	print "Good morning, welcome to the Xper Co testing facility."
	print "You have three doors to choose from; the middle door, the left door or the right door."
	print "Which door do you choose?"
	
	next = raw_input("> ")
	
	if next == "left":
		left_room()
	
	elif next == "right":
		right_room()
	
	elif next == "middle":
		centre_room()
	
	else:
		dead("You chose no door, so we had to terminate you.")
		
start()