import random
import os
import time
import math
import sys

fapcounter	 = 1
shaftlength = 7
ballsack = "8"
tip = "D"
Hand = "MM"
Padding = 1
shaftchar = "="
goonumber = random.randint(50, 100)
speedint = .5
endureint = 0

def invalid():
	print("INVALID CHOICE!")
	menu()

def invalidset():
	print("INVALID CHOICE!")
	menu()

def settings():
	time.sleep(.5)
	clear()
	for key in settingsoptions.keys():
		print(settingsoptions[key] [0])

	ans = input("\nMake a choice: ")
	clear()
	settingsoptions.get(ans.lower().replace(" ",""),[None,invalidset]) [1] ()

def endurance():
	global endureint
	clear()
	print("Endurance: "+str(endureint))
	try:
		endureint = int(input("\nInput endurance value (0-100): "))
	except:
		clear()
		print("ONLY INPUT NUMBER!")
		time.sleep(1.5)
		endurance()
	if endureint > 100:
		endureint = 100
	elif endureint < 0:
		endureint+ 0
	goonumber = random.randint(50,100) + endureint
	clear()
	print("Set new endurance!")
	time.sleep(1.5)
	settings()

def length():
	global shaftlength
	clear()
	print("Length: "+str(shaftlength))
	try:
		lengthint = int(input("\nInput length value (7-100): "))
	except:
		clear()
		print("ONLY INPUT NUMBER!")
		time.sleep(1.5)
		length()
	if lengthint > 100:
		lengthint = 100
	elif lengthint < 7:
		lengthint = 7
	shaftlength = lengthint
	clear()
	print("\nSet new length!")
	time.sleep(1.5)
	settings()

def speed():
	global speedint
	clear()
	print("Speed: "+str(speedint))
	try:
		speedint = float(input("\nInput speed value (0.05-1): "))
	except:
		clear()
		print("ONLY INPUT NUMBER!")
		time.sleep(1.5)
		speed()
	if speedint > 1:
		speedint = 1
	elif speedint < 0.05:
		speedint = 0.05
	clear()
	print("\nSet new speed!")
	time.sleep(1.5)
	settings()

def back():
	clear()
	menu()

def quickchoice():
	choice = input("\nGo again?[Y/N] ")
	if choice.lower() == "y":
		clear()
		fap()
	elif choice.lower() == "n":
		menu()
	else: 
		clear()
		quickchoice()


def calculatefapposition(i):
	fapdistance = shaftlength - len(Hand) - Padding * 2
	return abs(i % (fapdistance * 2) - fapdistance) + len(Hand) + Padding

def fap():
	while True:
		global fapcounter
		global goonumber
		fapcounter+=1
		fappos = calculatefapposition(fapcounter)
		shaft = Hand.rjust(fappos, shaftchar).ljust(shaftlength, shaftchar)
		result = str(ballsack + shaft + tip)
		print(result)
		if fapcounter == goonumber:
			time.sleep(1)
			goo = ["-", "--", "---", "---_", "--__", "-___", "____"]
			for i in goo:
				clear()
				print(result+i)
				time.sleep(.15)
			time.sleep(1.5)
			goonumber = random.randint(50, 100) + fapcounter + endureint
			break
		time.sleep(speedint/shaftlength)
		clear()
	quickchoice()

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def exit():
	sys.exit()

options = {
	"fap":("Fap",fap),
	"settings":("Settings",settings),
	"exit":("Exit",exit)
}
settingsoptions = {
	"endurance":("Endurance",endurance),
	"length":("Length",length),
	"speed":("Speed",speed),
	"back":("Back",back)
}

def menu():
	time.sleep(.5)
	clear()
	for key in options.keys():
		print(options[key] [0])

	ans = input("\nMake a choice: ")
	clear()
	options.get(ans.lower().replace(" ",""),[None,invalid]) [1] ()


menu()
# while True:
# 	clear()
# 	fap()
# 	time.sleep(speedint)
