from sys import exit
from random import randint

class Scene(object):

	def enter(self):
		print "This is an empty scene. Subclass it and implement  enter()."
		exit(1)
		
class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map
		
	def play(self):
		current_scene = self.scene_map.opening_scene()
		
		while True:
			print "\n", "-" * 20
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
			if not current_scene:
				print "Yay, the shift it over!"
				return 'Win'
				#exit(0)

class Death(Scene):

	quips = [
		"The customers' inane questions are too much for you, so you quit on the spot.",
		"The customer asks \' Do you come here often?\'. You die from shame on their behalf",
		"Hospitality is not for you, goodbye.",
		"Game over man."
	]
	
	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)
		
		
class Win(Scene):
	
	winner = [
		"These customers have nothing on you!",
		"You successfully managed to get both customers removed and sell nothing."
	]
	
	def enter(self):
		print Win.winner[randint(0, len(self.winner)-1)]
		exit(1)		
		
		# Does not currently activate.

class Fight(Scene):

	quotes = [
		"This isn't how I make this drink at home.",
		"I want to speak to your manager.",
		"What kind of place doesn't serve tennents?!",
		"Do you know who I am?!",
		"I will have you know, I used to work in bars!",
		"Do you have any vegan, gluten and cruelty free alcohol?",
		"Can you give me a free drink because it is my birthday?",
		"The drinks are better in Wetherspoons."
	]
	
	
	def enter(self):
		print "\n", "-" * 20
		print "You wake up behind the bar, across from you are two customers:"
		print "Customer 1"
		print "Customer 2"
		print "They are both waving money at you and clicking their fingers."
		
		health = 20
		customer1_hitpoints = 10
		customer2_hitpoints = 12
		customer1 = True
		customer2 = True
		
		
				#Need to work out how to move on after while loop complete.
		
		while health > 0 and (customer1 or customer2):
			#While loop runs whilst health > 0 and one of the customers remains.
			print "\n", "-" * 20
			your_attack = randint(4,12)
			customer1_attack = randint(1,4)
			customer2_attack = randint(3,6)
			if customer2_hitpoints == 0 and customer1_hitpoints == 0:
				return 'Win'
			
			attack = int(raw_input("Type 1 to attack Customer 1, 2 to attack Customer 2 >"))
			if attack == 1:
				if customer1:
					customer1_hitpoints = customer1_hitpoints - your_attack
					print "You refuse service to Customer 1, %d damage." % your_attack
					if customer1_hitpoints <= 0:
						customer1 = False
						print "Customer 1 is removed from the building."
				else:
					print "Customer 1 has already been removed and left an angry Trip Advisor review."
			elif attack == 2:
				if customer2:
					customer2_hitpoints = customer2_hitpoints - your_attack
					print "You tell customer 2 that they have had too much already, %d damage." % your_attack
					if customer2_hitpoints <= 0:
						customer2 = False
						print "Customer 2 falls over and throws up, they are promptly removed from the building."
				else:
					print "They have already left to get a late night burger."
			else:
				print "You do nothing, and are asked for a \'Cheeky Vimto\'."
				
			if customer1:
				health = health - customer1_attack
				print "Customer 1 tells you: "
				print Fight.quotes[randint(0, len(self.quotes)-1)] 
				print "It causes %d damage and you have d% health left." % (customer1_attack, health)
				if health <= 0:
					return 'death'
					break
					
			if customer2:
				health = health - customer2_attack
				print "Customer 2 says: "
				print Fight.quotes[randint(0, len(self.quotes)-1)] 
				print "It causes %d damage and you have %d health left." % (customer2_attack, health)
				if health <= 0:
					return 'death'
					break
					
			
			
					
		
				
class Map(object):

	scenes = {
		'fight' : Fight(),
		'death' : Death(),
		'Win' : Win()
	}
	
	def __init__(self, start_scene):
		self.start_scene = start_scene
		
	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name)
		
	def opening_scene(self):
		return self.next_scene(self.start_scene)
					
					
				

a_map = Map('fight')
a_game = Engine(a_map)
a_game.play()
					
					
					
					