import random

#part 1 - create the list of the gameboard
columns = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
gameboard = []
hidden = []
visible = []
spots = []
for i in range(len(columns)):
	print(columns[i], " ", end="")
print()
for row in range(10):
	print(row,end="")
	for i in range(10):
		gameboard.append("|__")
		print(gameboard[i],end="")
	print()


#creates the hidden gameboard
#for i in range(len(columns)):
	#print(columns[i], " ", end="")
#print()
for row in range(10):
	#print(row,end="")
	for i in range(10):
		hidden.append("|__")
		#print(hidden[i],end="")
	#print()

#creates the visible gameboard
#for i in range(len(columns)):
	#print(columns[i], " ", end="")
#print()
for row in range(10):
	#print(row,end="")
	for i in range(10):
		visible.append("|__")
		#print(visible[i],end="")
	#print()

#part 2-ask the user for the game mode
mode = input("will you be playing in hidden or visible mode? ")
if mode == "hidden mode":
	#code that hides the mines
	mines = []
	while len(mines) < 10: 
		mine = random.randrange(100)
		while mine in mines:
			mine = random.randrange(100)
		mines.append(mine)
		hidden[mine] = "|_X"
		print(mine)

	#draws the new hidden gameboard with the numbers around the mines
	for i in range(len(hidden)):
		if "X" in hidden[i]:
			if (i - 9)%10 != 0:	
				if "X" not in hidden[i+1]:
					if "1" in hidden[i+1]:
						hidden[i+1] = "|_2"
					elif "2" in hidden[i+1]:
						hidden[i+1] = "|_3"
					elif "3" in hidden[i+1]:
						hidden[i+1] = "|_4"
					elif "4" in hidden[i+1]:
						hidden[i+1] = "|_5"
					elif "5" in hidden[i+1]:
						hidden[i+1] = "|_6"
					elif "6" in hidden[i+1]:
						hidden[i+1] = "|_7"
					elif "7" in hidden[i+1]:
						hidden[i+1] = "|_8"
					else:
						hidden[i+1] = "|_1"
			if i%10 != 0:
				if "X" not in hidden[i-1]:
					if "1" in hidden[i-1]:
						hidden[i-1] = "|_2"
					elif "2" in hidden[i-1]:
						hidden[i-1] = "|_3"
					elif "3" in hidden[i-1]:
						hidden[i-1] = "|_4"
					elif "4" in hidden[i-1]:
						hidden[i-1] = "|_5"
					elif "5" in hidden[i-1]:
						hidden[i-1] = "|_6"
					elif "6" in hidden[i-1]:
						hidden[i-1] = "|_7"
					elif "7" in hidden[i-1]:
						hidden[i-1] = "|_8"
					else:
						hidden[i-1] = "|_1"
			if i%10 != 0 and i > 10:
				if "X" not in hidden[i-11]:
					if "1" in hidden[i-11]:
						hidden[i-11] = "|_2"
					elif "2" in hidden[i-11]:
						hidden[i-11] = "|_3"
					elif "3" in hidden[i-11]:
						hidden[i-11] = "|_4"
					elif "4" in hidden[i-11]:
						hidden[i-11] = "|_5"
					elif "5" in hidden[i-11]:
						hidden[i-11] = "|_6"
					elif "6" in hidden[i-11]:
						hidden[i-11] = "|_7"
					elif "7" in hidden[i-11]:
						hidden[i-11] = "|_8"
					else:
						hidden[i-11] = "|_1"

			if i > 9:
				if "X" not in hidden[i-10]:
					if "1" in hidden[i-10]:
						hidden[i-10] = "|_2"
					elif "2" in hidden[i-10]:
						hidden[i-10] = "|_3"
					elif "3" in hidden[i-10]:
						hidden[i-10] = "|_4"
					elif "4" in hidden[i-10]:
						hidden[i-10] = "|_5"
					elif "5" in hidden[i-10]:
						hidden[i-10] = "|_6"
					elif "6" in hidden[i-10]:
						hidden[i-10] = "|_7"
					elif "7" in hidden[i-10]:
						hidden[i-10] = "|_8"
					else:
						hidden[i-10] = "|_1"
			if (i - 9)%10 != 0 and i > 8:
				if "X" not in hidden[i-9]:
					if "1" in hidden[i-9]:
						hidden[i-9] = "|_2"
					elif "2" in hidden[i-9]:
						hidden[i-9] = "|_3"
					elif "3" in hidden[i-9]:
						hidden[i-9] = "|_4"
					elif "4" in hidden[i-9]:
						hidden[i-9] = "|_5"
					elif "5" in hidden[i-9]:
						hidden[i-9] = "|_6"
					elif "6" in hidden[i-9]:
						hidden[i-9] = "|_7"
					elif "7" in hidden[i-9]:
						hidden[i-9] = "|_8"
					else:
						hidden[i-9] = "|_1"
		
			if (i - 9)%10 != 0 and i < 89:
				if "X" not in hidden[i+11]:
					if "1" in hidden[i+11]:
						hidden[i+11] = "|_2"
					elif "2" in hidden[i+11]:
						hidden[i+11] = "|_3"
					elif "3" in hidden[i+11]:
						hidden[i+11] = "|_4"
					elif "4" in hidden[i+11]:
						hidden[i+11] = "|_5"
					elif "5" in hidden[i+11]:
						hidden[i+11] = "|_6"
					elif "6" in hidden[i+11]:
						hidden[i+11] = "|_7"
					elif "7" in hidden[i+11]:
						hidden[i+11] = "|_8"
					else:
						hidden[i+11] = "|_1"
			if i < 90:
				if "X" not in hidden[i+10]:
					if "1" in hidden[i+10]:
						hidden[i+10] = "|_2"
					elif "2" in hidden[i+10]:
						hidden[i-1] = "|_3"
					elif "3" in hidden[i+10]:
						hidden[i+10] = "|_4"
					elif "4" in hidden[i+10]:
						hidden[i+10] = "|_5"
					elif "5" in hidden[i+10]:
						hidden[i+10] = "|_6"
					elif "6" in hidden[i+10]:
						hidden[i+10] = "|_7"
					elif "7" in hidden[i+10]:
						hidden[i+10] = "|_8"
					else:
						hidden[i+10] = "|_1"
			if i%10 != 0 and i < 91:
				if "X" not in hidden[i+9]:
					if "1" in hidden[i+9]:
						hidden[i+9] = "|_2"
					elif "2" in hidden[i+9]:
						hidden[i+9] = "|_3"
					elif "3" in hidden[i+9]:
						hidden[i+9] = "|_4"
					elif "4" in hidden[i+9]:
						hidden[i+9] = "|_5"
					elif "5" in hidden[i+9]:
						hidden[i+9] = "|_6"
					elif "6" in hidden[i+9]:
						hidden[i+9] = "|_7"
					elif "7" in hidden[i+9]:
						hidden[i+9] = "|_8"
					else:
						hidden[i+9] = "|_1"






	for i in range(len(columns)):
		print(columns[i], " ", end="")
	print()
	for row in range(10):
		print(row,end="")
		print(gameboard[0+10*row],end="")
		print(gameboard[1+10*row],end="")
		print(gameboard[2+10*row],end="")
		print(gameboard[3+10*row],end="")
		print(gameboard[4+10*row],end="")
		print(gameboard[5+10*row],end="")
		print(gameboard[6+10*row],end="")
		print(gameboard[7+10*row],end="")
		print(gameboard[8+10*row],end="")
		print(gameboard[9+10*row],end="")
		print()
		
	#game loop
	while "|_X" in hidden:
		question = input("do you want to guess a location or a mine? ")
		if question == "mine":
			flag = int(input("Where do you want to place a flag? "))
			if flag in spots:
				gameboard[flag] = "|__"
			elif flag not in spots:
				gameboard[flag] = "|_F"
			spots.append(flag)

			for i in range(len(columns)):
				print(columns[i], " ", end="")
			print()
			for row in range(10):
				print(row,end="")
				print(gameboard[0+10*row],end="")
				print(gameboard[1+10*row],end="")
				print(gameboard[2+10*row],end="")
				print(gameboard[3+10*row],end="")
				print(gameboard[4+10*row],end="")
				print(gameboard[5+10*row],end="")
				print(gameboard[6+10*row],end="")
				print(gameboard[7+10*row],end="")
				print(gameboard[8+10*row],end="")
				print(gameboard[9+10*row],end="")
				print()

		elif question == "location":
			location = int(input("What location do you want to reveal?"))
			if "1" in hidden[location] or "2" in hidden[location] or "3" in hidden[location] or "4" in hidden[location] or "5" in hidden[location] or "6" in hidden[location] or "7" in hidden[location] or "8" in hidden[location]:
					gameboard[location] = hidden[location]
			for i in range(len(gameboard)):
				if "|_1" != hidden[location] or "|_2" != hidden[location] or "|_3" != hidden[location] or "|_4" != hidden[location] or "|_5" != hidden[location] or "|_6" != hidden[location] or "|_7" != hidden[location] or "|_8" != hidden[location]:
					gameboard[location] = "|_R"
					if "X" in hidden[location]:
						print("Game over, you blew up!")
						for i in range(len(columns)):
							print(columns[i], " ", end="")
						print()
						for row in range(10):
							print(row,end="")
							print(hidden[0+10*row],end="")
							print(hidden[1+10*row],end="")
							print(hidden[2+10*row],end="")
							print(hidden[3+10*row],end="")
							print(hidden[4+10*row],end="")
							print(hidden[5+10*row],end="")
							print(hidden[6+10*row],end="")
							print(hidden[7+10*row],end="")
							print(hidden[8+10*row],end="")
							print(hidden[9+10*row],end="")
							print()
					break
				else:
				#elif "|_1" == hidden[location] or "|_2" == hidden[location] or "|_3" == hidden[location] or "|_4" == hidden[location] or "|_5" == hidden[location] or "|_6" == hidden[location] or "|_7" == hidden[location] or "|_8" == hidden[location]:
					gameboard[location] = hidden[location]

			for i in range(len(columns)):
				print(columns[i], " ", end="")
			print()
			for row in range(10):
				print(row,end="")
				print(gameboard[0+10*row],end="")
				print(gameboard[1+10*row],end="")
				print(gameboard[2+10*row],end="")
				print(gameboard[3+10*row],end="")
				print(gameboard[4+10*row],end="")
				print(gameboard[5+10*row],end="")
				print(gameboard[6+10*row],end="")
				print(gameboard[7+10*row],end="")
				print(gameboard[8+10*row],end="")
				print(gameboard[9+10*row],end="")
				print()

		reveal = input("do you think you found all the mines? ")
		if reveal == "yes":
			for i in range(len(columns)):
				print(columns[i], " ", end="")
			print()
			for row in range(10):
				print(row,end="")
				print(hidden[0+10*row],end="")
				print(hidden[1+10*row],end="")
				print(hidden[2+10*row],end="")
				print(hidden[3+10*row],end="")
				print(hidden[4+10*row],end="")
				print(hidden[5+10*row],end="")
				print(hidden[6+10*row],end="")
				print(hidden[7+10*row],end="")
				print(hidden[8+10*row],end="")
				print(hidden[9+10*row],end="")
				print()
			break

	
		
elif mode == "visible mode":
	#code that makes the mines and numbers visible
	#randomly place the mines in the game board
	mines = []
	while len(mines) < 10: 
		mine = random.randrange(100)
		while mine in mines:
			mine = random.randrange(100)
		mines.append(mine)
		visible[mine] = "|_X"
		gameboard[mine] = "|_X"

	#draws the new gameboard with the mines
	for i in range(len(columns)):
		print(columns[i], " ", end="")
	print()
	for row in range(10):
		print(row,end="")
		print(gameboard[0+10*row],end="")
		print(gameboard[1+10*row],end="")
		print(gameboard[2+10*row],end="")
		print(gameboard[3+10*row],end="")
		print(gameboard[4+10*row],end="")
		print(gameboard[5+10*row],end="")
		print(gameboard[6+10*row],end="")
		print(gameboard[7+10*row],end="")
		print(gameboard[8+10*row],end="")
		print(gameboard[9+10*row],end="")
		print()
	
	#draws the new gameboard with the numbers around the mines
	for i in range(len(gameboard)):
		if "|_X" == gameboard[i]:
			if (i - 9)%10 != 0:	
				if "X" not in gameboard[i+1]:
					if "1" in gameboard[i+1]:
						gameboard[i+1] = "|_2"
					elif "2" in gameboard[i+1]:
						gameboard[i+1] = "|_3"
					elif "3" in gameboard[i+1]:
						gameboard[i+1] = "|_4"
					elif "4" in gameboard[i+1]:
						gameboard[i+1] = "|_5"
					elif "5" in gameboard[i+1]:
						gameboard[i+1] = "|_6"
					elif "6" in gameboard[i+1]:
						gameboard[i+1] = "|_7"
					elif "7" in gameboard[i+1]:
						gameboard[i+1] = "|_8"
					else:
						gameboard[i+1] = "|_1"
			if i%10 != 0:
				if "X" not in gameboard[i-1]:
					if "1" in gameboard[i-1]:
						gameboard[i-1] = "|_2"
					elif "2" in gameboard[i-1]:
						gameboard[i-1] = "|_3"
					elif "3" in gameboard[i-1]:
						gameboard[i-1] = "|_4"
					elif "4" in gameboard[i-1]:
						gameboard[i-1] = "|_5"
					elif "5" in gameboard[i-1]:
						gameboard[i-1] = "|_6"
					elif "6" in gameboard[i-1]:
						gameboard[i-1] = "|_7"
					elif "7" in gameboard[i-1]:
						gameboard[i-1] = "|_8"
					else:
						gameboard[i-1] = "|_1"
			if i%10 != 0 and i > 10:
				if "X" not in gameboard[i-11]:
					if "1" in gameboard[i-11]:
						gameboard[i-11] = "|_2"
					elif "2" in gameboard[i-11]:
						gameboard[i-11] = "|_3"
					elif "3" in gameboard[i-11]:
						gameboard[i-11] = "|_4"
					elif "4" in gameboard[i-11]:
						gameboard[i-11] = "|_5"
					elif "5" in gameboard[i-11]:
						gameboard[i-11] = "|_6"
					elif "6" in gameboard[i-11]:
						gameboard[i-11] = "|_7"
					elif "7" in gameboard[i-11]:
						gameboard[i-11] = "|_8"
					else:
						gameboard[i-11] = "|_1"

			if i > 9:
				if "X" not in gameboard[i-10]:
					if "1" in gameboard[i-10]:
						gameboard[i-10] = "|_2"
					elif "2" in gameboard[i-10]:
						gameboard[i-10] = "|_3"
					elif "3" in gameboard[i-10]:
						gameboard[i-10] = "|_4"
					elif "4" in gameboard[i-10]:
						gameboard[i-10] = "|_5"
					elif "5" in gameboard[i-10]:
						gameboard[i-10] = "|_6"
					elif "6" in gameboard[i-10]:
						gameboard[i-10] = "|_7"
					elif "7" in gameboard[i-10]:
						gameboard[i-10] = "|_8"
					else:
						gameboard[i-10] = "|_1"
			if (i - 9)%10 != 0 and i > 8:
				if "X" not in gameboard[i-9]:
					if "1" in gameboard[i-9]:
						gameboard[i-9] = "|_2"
					elif "2" in gameboard[i-9]:
						gameboard[i-9] = "|_3"
					elif "3" in gameboard[i-9]:
						gameboard[i-9] = "|_4"
					elif "4" in gameboard[i-9]:
						gameboard[i-9] = "|_5"
					elif "5" in gameboard[i-9]:
						gameboard[i-9] = "|_6"
					elif "6" in gameboard[i-9]:
						gameboard[i-9] = "|_7"
					elif "7" in gameboard[i-9]:
						gameboard[i-9] = "|_8"
					else:
						gameboard[i-9] = "|_1"
		
			if (i - 9)%10 != 0 and i < 89:
				if "X" not in gameboard[i+11]:
					if "1" in gameboard[i+11]:
						gameboard[i+11] = "|_2"
					elif "2" in gameboard[i+11]:
						gameboard[i+11] = "|_3"
					elif "3" in gameboard[i+11]:
						gameboard[i+11] = "|_4"
					elif "4" in gameboard[i+11]:
						gameboard[i+11] = "|_5"
					elif "5" in gameboard[i+11]:
						gameboard[i+11] = "|_6"
					elif "6" in gameboard[i+11]:
						gameboard[i+11] = "|_7"
					elif "7" in gameboard[i+11]:
						gameboard[i+11] = "|_8"
					else:
						gameboard[i+11] = "|_1"
			if i < 90:
				if "X" not in gameboard[i+10]:
					if "1" in gameboard[i+10]:
						gameboard[i+10] = "|_2"
					elif "2" in gameboard[i+10]:
						gameboard[i-1] = "|_3"
					elif "3" in gameboard[i+10]:
						gameboard[i+10] = "|_4"
					elif "4" in gameboard[i+10]:
						gameboard[i+10] = "|_5"
					elif "5" in gameboard[i+10]:
						gameboard[i+10] = "|_6"
					elif "6" in gameboard[i+10]:
						gameboard[i+10] = "|_7"
					elif "7" in gameboard[i+10]:
						gameboard[i+10] = "|_8"
					else:
						gameboard[i+10] = "|_1"
			if i%10 != 0 and i < 91:
				if "X" not in gameboard[i+9]:
					if "1" in gameboard[i+9]:
						gameboard[i+9] = "|_2"
					elif "2" in gameboard[i+9]:
						gameboard[i+9] = "|_3"
					elif "3" in gameboard[i+9]:
						gameboard[i+9] = "|_4"
					elif "4" in gameboard[i+9]:
						gameboard[i+9] = "|_5"
					elif "5" in gameboard[i+9]:
						gameboard[i+9] = "|_6"
					elif "6" in gameboard[i+9]:
						gameboard[i+9] = "|_7"
					elif "7" in gameboard[i+9]:
						gameboard[i+9] = "|_8"
					else:
						gameboard[i+9] = "|_1"

	for i in range(len(columns)):
		print(columns[i], " ", end="")
	print()
	for row in range(10):
		print(row,end="")
		print(gameboard[0+10*row],end="")
		print(gameboard[1+10*row],end="")
		print(gameboard[2+10*row],end="")
		print(gameboard[3+10*row],end="")
		print(gameboard[4+10*row],end="")
		print(gameboard[5+10*row],end="")
		print(gameboard[6+10*row],end="")
		print(gameboard[7+10*row],end="")
		print(gameboard[8+10*row],end="")
		print(gameboard[9+10*row],end="")
		print()


	#game loop
	while "|_X" in gameboard:
		question = input("do you want to guess a location or a mine? ")
		if question == "mine":
			flag = int(input("Where do you want to place a flag? "))
			if flag in spots:
				gameboard[flag] = "|__"
			elif flag not in spots:
				gameboard[flag] = "|_F"
			spots.append(flag)

			for i in range(len(columns)):
				print(columns[i], " ", end="")
			print()
			for row in range(10):
				print(row,end="")
				print(gameboard[0+10*row],end="")
				print(gameboard[1+10*row],end="")
				print(gameboard[2+10*row],end="")
				print(gameboard[3+10*row],end="")
				print(gameboard[4+10*row],end="")
				print(gameboard[5+10*row],end="")
				print(gameboard[6+10*row],end="")
				print(gameboard[7+10*row],end="")
				print(gameboard[8+10*row],end="")
				print(gameboard[9+10*row],end="")
				print()


		elif question == "location":
			location = int(input("What location do you want to reveal?"))
			#gameboard[location] = "|_R"
			for i in range(len(gameboard)):
				if "|_1" != gameboard[location] or "|_2" != gameboard[location] or "|_3" != gameboard[location] or "|_4" != gameboard[location] or "|_5" != gameboard[location] or "|_6" != gameboard[location] or "|_7" != gameboard[location] or "|_8" != gameboard[location]:
					if "X" in gameboard[location]:
						print("Game over, you blew up!")
						for i in range(len(columns)):
							print(columns[i], " ", end="")
						print()
						for row in range(10):
							print(row,end="")
							print(visible[0+10*row],end="")
							print(visible[1+10*row],end="")
							print(visible[2+10*row],end="")
							print(visible[3+10*row],end="")
							print(visible[4+10*row],end="")
							print(visible[5+10*row],end="")
							print(visible[6+10*row],end="")
							print(visible[7+10*row],end="")
							print(visible[8+10*row],end="")
							print(visible[9+10*row],end="")
							print()
					break
				elif "|_1" == gameboard[location] or "|_2" == gameboard[location] or "|_3" == gameboard[location] or "|_4" == gameboard[location] or "|_5" == gameboard[location] or "|_6" == gameboard[location] or "|_7" == gameboard[location] or "|_8" == gameboard[location]:
					gameboard[location] = visible[location]
				else:
					gameboard[location] = "|_R"




			for i in range(len(columns)):
				print(columns[i], " ", end="")
			print()
			for row in range(10):
				print(row,end="")
				print(gameboard[0+10*row],end="")
				print(gameboard[1+10*row],end="")
				print(gameboard[2+10*row],end="")
				print(gameboard[3+10*row],end="")
				print(gameboard[4+10*row],end="")
				print(gameboard[5+10*row],end="")
				print(gameboard[6+10*row],end="")
				print(gameboard[7+10*row],end="")
				print(gameboard[8+10*row],end="")
				print(gameboard[9+10*row],end="")
				print()

		reveal = input("do you think you found all the mines? ")
		if reveal == "yes":
			for i in range(len(columns)):
				print(columns[i], " ", end="")
			print()
			for row in range(10):
				print(row,end="")
				print(gameboard[0+10*row],end="")
				print(gameboard[1+10*row],end="")
				print(gameboard[2+10*row],end="")
				print(gameboard[3+10*row],end="")
				print(gameboard[4+10*row],end="")
				print(gameboard[5+10*row],end="")
				print(gameboard[6+10*row],end="")
				print(gameboard[7+10*row],end="")
				print(gameboard[8+10*row],end="")
				print(gameboard[9+10*row],end="")
				print()
			break

	