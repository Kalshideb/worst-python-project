import fileinput
import sys
import time
import random
import math
import re
import os
#vars
gamestatus = 1
weapons = {'Bat': 4, 'Fists': 1}
enemies = {'Rat': (2,5,0,7), 'Skeleton': (3,3,0,5), 'Skeleton Archer': (5,2,0,7), 'Bandit': (4,4,1,12)}
dungeonenemies = ['Rat','Skeleton','Skeleton Archer']

#check for game status
def gamestatuscheck():
	type('Checking game status\n')
	if gamestatus == 0:
		sys.exit("Game is down for now")
	elif gamestatus == 1:
        	type('Game is up!\n')
	
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
def intcheck(x):
	try:
		int(x)
		return True
	except ValueError:
		return False

#encounter, remember to add speech check which is stored in enemies[NAME][2] or something like that    bool type
def encounter(mobs):
	
        print "You encouter a",
	for x in mobs[:-1]:
		print x + ',',
	print "and a " + mobs[len(mobs) - 1] + '.'      

	
	#speech check here


	#if fail init combat
	combat(mobs)
		
#encounter random enemys from an array, array should consist of mobs found in specific area
def randencounter(mobs):
	num = random.randint(1,4)
	x = len(mobs) - 1
	i = 0
	ranmobs = []
	while i < num:
		ranmobs.append(mobs[random.randint(0,x)])
		i += 1
	
	encounter(ranmobs)	



#if speech check fails or is not chosen combat starts
def combat(mobs):
        type("Combat start!\n")
	alivemobs = len(mobs)
	#init combat while loop


#uncomment for debugging
#intcheck('s')
#intcheck('1')
#encounter(dungeonenemies)
#randencounter(dungeonenemies)
#encounter(["Rat","Rat","Skeleton"])
#type("Swiggity Swag\n")
