import sys
import time

# main game variables
gCurrentScene = 1
gMain = True
gSceneMissleDoorOpen = [False]

# default player powerups
pBeams = ["power"]

# missle values
pHasMissles = False # they don't at the start
pMisslesUpgrades = 1
pMisslesMax = 5*pMisslesUpgrades
pMissles = 5


"""
pGetInput:
Main input routine 
"""
def pGetInput() :
	global pInput # needs to be glabal to be easy to manage
	
	pInputBreak = True

	while pInputBreak :
		pInput = input("> ").lower()

		if pInput == "stats" :
			print("Your Beams:")
			for x in pBeams :
				print("-", x.title())
			if pHasMissles :
				print("Missles:", pMissles)
		elif pInput == "exit" :
			print("See you next mission!")
			sys.exit()
		else :
			try :
				pInput = int(pInput)
			except :
				print("error")
				continue
			else :
				print("\n------------------------------------------------------------")
				return pInput

"""
Main loop
"""

text = """
Welcome to Metroid: The Text Adventure Game!

You are the interstellar bounty hunter Samus Aran, who has
been sent by the Galactic Federation to investigate planet
Axius 77. They've found presense of Space Pirate activity
and they're suspicious of their behaviour. They've noted
that an unknown powerful species lurks on the planet,
however, but their scans and research could not determine
what it could be, or what threat it could pose to you.
They advise you to be careful, and tread lightly.
"""

# kinda hacky but idk
# this prints the intro text character by character
for char in text :
	sys.stdout.write(char)
	sys.stdout.flush()
	time.sleep(.05)
	if "\n" in char :
		time.sleep(1)

time.sleep(2)

input("\nPress enter to continue. ")

print("------------------------------------------------------------")

gJustEnteredScene = True

while True :
	# scene 1
	if gCurrentScene == 1:
		if gJustEnteredScene == True :
			print("""
You've landed your ship in a crater on Axius 77. The purple
grass and blue sky don't feel so inviting. In the crater,
there's two hexagonal doors to your left and right.
 			""")
		
		# text to show if the player hasn't unlocked the door
			if gSceneMissleDoorOpen[0] == False :
				print("The door on your left is locked.")
			
			gJustEnteredScene = False
		
		# player choices
		print("\nYour choices are:")
		print("1: Enter the door on your right.")
		if gSceneMissleDoorOpen[0] == False :
			print("2: Try the door on your left.")
		else :
			print("2: Enter the door on your left.")
		
		# scene specific inputs
		match pGetInput() :
			case 1 :
				gJustEnteredScene = True
				gCurrentScene = 2
			case 2 :
				if pHasMissles == True and pMissles > 0 :
					if gSceneMissleDoorOpen[0] == False :
						gSceneMissleDoorOpen[0] = True
						pMissles -= 1
						print("You unlocked the door by firing a missle at it.")
						print("You now have", pMissles, "missles left.")
					gJustEnteredScene = True
					gCurrentScene = 3
					
				elif pMissles == 0 :
					print("\nYou do not have any missles to open the door.")
				else :
					print("\nYou can't seem to open this door. An explosive weapon could\nopen the door.\n")
			case _ :
				print("Invalid input. Try again.")

	if gCurrentScene == 2 :
		if gJustEnteredScene == True :
			if pHasMissles == False :
				print("""
You take the door to your right. Among the clean blue
metalic dome interior, a Missle Launcher attachment is in
the center of the room. You take it and apply it to your
arm cannon.

You unlocked the Missle Launcher! Among being strong to
enemies, it may also unlock certain doors!""")
				pHasMissles = True # player obtains the missle launcher
			
			else :
				print("""
You take the door to your right. This is the room where you
obtained the Missle Launcher attachment. The room is small,
and is covered in a clean, blue metalic surface.""")
			
		# player choices
		print("\nYour choices are:")
		print("1: Leave the room.")
		
		# scene specific inputs
		match pGetInput() :
			case 1 :
				gJustEnteredScene = True
				gCurrentScene = 1
			case _ :
				print("Invalid input. Try again.")

	if gCurrentScene == 3 :
		print("\n\n\nThis is it of the small demo.\nI could easily expand on it if I want to but this is just a rough base.\nThanks for playing!")
		sys.exit()