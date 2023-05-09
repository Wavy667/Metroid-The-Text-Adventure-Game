import sys
import random
import time
import colorama

global gMain

gCurrentScene = 1
gMain = True
pBeams = ["power"]

"""
pGetInput:
Main input routine 
"""
def pGetInput() :
	global pInput
	
	pInputBreak = True

	while pInputBreak :
		pInput = input("> ").lower()
		
		if pInput == "stats" :
			print("Your beams:")
			for x in pBeams :
				print(x.title())
		elif pInput == "exit" :
			print("See you next mission!")
			sys.exit()
		else :
			return pInput

"""
Main loop
"""
while True :
	# scene 1
	if gCurrentScene == 1:
		print("""
 test scene
 	""")
		gSceneActions = ["left", "right"]
		
		pGetInput()

		print("You typed", pInput)

		# Scene specific inputs
		match pInput :
			case "left" :
				gCurrentScene = 2
			case "right" :
				gCurrentScene = 2
			