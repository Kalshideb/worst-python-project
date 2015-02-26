import sys
import time
import random
import math
#vars
weapons = {'Bat': 4, 'Fists': 1}

enemies = {'Rat': (2,5,0,7), 'Skeleton': (3,3,0,5), 'Skeleton Archer': (5,2,0,7), 'Bandit': (4,4,1,12)}
dungeonenemies = ['Rat','Skeleton','Skeleton Archer']



#This function makes text appear as if typed
def type(text):
	for char in text:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(0.05)


#for when you have a need for speed B^)
def typefast(text):
	for char in text:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(0.015)


#check for int
def isint(x):
	try:
		int(x)
		return True
	except ValueError:
		return False



#encounter, remember to add speech check which is stored in enemies[NAME][2]  bool type
def encounter(mobs):
	
        print "You encouter a",
	for x in mobs[:-1]:
		print x + ',',
	print "and a " + mobs[len(mobs) - 1] + '.'      

	return mobs

	#speech check here
	
#encounter random enemys from an array,
def randincounter(mobs):
	num = random.randint(1,3)
	x = len(mobs) - 1
	print "You encounter a",
	i = 0
	while i < num:
		print mobs[random.randint(0,x)] + ',',
		i += 1
	print "and a " + mobs[random.randint(0,x)] + '.'
	return mobs

	#speech check here



#if speech check fails or is not chosen combat starts
def combat(mobs):
        type("Combat start!")



#uncomment for debugging

#encounter(dungeonenemies)
#randincounter(dungeonenemies)
#encounter(["Rat","Rat","Skeleton"])
#type("Swiggity Swag\n")
