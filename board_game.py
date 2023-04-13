import pygame
import random

#It is for first player's movement.The player is placed at the last row for the first time. The function calculates where it will be placed after the dice.
def move_update_1(player1_loc):
	
	if player1_loc < 63:
		if player1_loc % 9 == 0:
			row = 9
			col = player1_loc // 9
		else: 
			row = player1_loc % 9
			col = (player1_loc // 9)+1
		pygame.draw.rect(window, (0,177,255), ((row*dim)-35 , (col*dim)-35, 20, 20))
		pygame.display.update()
		pygame.time.delay(2000)
	else:
		row = 5
		col = 1	
		pygame.draw.rect(window, (0,177,255), ((row*dim)-35 , (col*dim)-35, 20, 20))
		pygame.display.update()
		pygame.time.delay(500)
	
#It is for second player's movement. it is placed the beggining of the row for the first time. The function calculates where it will be placed after the dice.		
def move_update_2(player2_loc):
	if player2_loc > 9:
		if player2_loc % 9 == 0:
			row = 9
			col = player2_loc // 9
		else:
			row = player2_loc %9
			col = (player2_loc // 9)+1
		pygame.draw.rect(window, (255,0,177), ((row*dim)-35 , (col*dim)-35, 20,20))				
		pygame.display.update()
		pygame.time.delay(500)
	else:
		row = 5
		col = 1	
		pygame.draw.rect(window, (255,0,177), ((row*dim)-35 , (col*dim)-35, 20, 20))
		pygame.display.update()
		pygame.time.delay(500)	

#This function calculates first player's movement accordig to result of dice. 		
def dice_movement1(dice1,player_place1):

	
	#Player cannot move and return 0
	if dice1 == 1:
		print('Unfortunately, turn changed')
		return 0
	#Player can make double movement. It can go 4 squares up on the board and return -36	
	elif dice1 == 2:	
		print('Double move! Going for four squares up')	
		return -36
	#Player goes 1 square right and return 1	
	elif dice1 == 3:
		print('Going for one square right')
		return 1
	#Player goes 1 square left and return -1	
	elif dice1 == 4:
		print('Going for one square left')
		return -1
		
	elif dice1 == 5:
		#If the player located in the last 9 rows, it cannot go down on the board. Return 0
		if player_place1 > 63:
			print('Player cannot move')
			return 0
		#Otherwise, player can move for 1 square down and return 9	 	
		else:	
			print('Going for one square down')
			return 9
	#Player goes 2 square right and return 2		
	elif dice1 == 6:
		print('Going for two squares right')
		return 2
	#Player goes 2 square left and return -2	
	elif dice1 == 7:
		print('Going for two squares left')
		return -2
		
	elif dice1 == 8:
		#If the player located in the last 18 rows, it cannot go down on the board. Return 0
		if player_place1 > 54:
			print('Player cannot move')
			return 0
		#Otherwise, player can move for 2 square down and return 18		
		else:	
			print('Going for two squares down')
			return 18
			
	elif dice1 == 9:
		#If the player located in the first 18 rows, it cannot go up on the board. Return 0
		if player_place1 <  18:
			print('Player cannot move')
			return 0
		#Otherwise, player can move for 2 square up and return -18	
		else:	
			print('Going for two square up')
			return -18	
	else:
		#If the player located in the first 27 rows, it cannot go up on the board. Return 0
		if player_place1 < 27:
			print('Player cannot move')
			return 0
		#Otherwise, player can move for 3 square up and return -27	
		else:	
			print('Going for three squares up')
			return -27		
			
#This function calculates second player's movement accordig to result of dice. 			
def dice_movement2(dice2,player_place2):

	
	#Player cannot move and return 0
	if dice2 == 1:
		print('Unfortunately, turn changed')
		return 0
	#Player can make double movement. It can go 4 squares down on the board and return 36	
	elif dice2 == 2:
		print('Double move! Going for four squares down')	
		return 36
	#Player goes 1 square right and return 1	
	elif dice2 == 3:
		print('Going for one square right')
		return 1
	#Player goes 1 square left and return -1	
	elif dice2 == 4:
		print('Going for one square left')
		return -1
		
	elif dice2 == 5:
		#If the player located in the first 9 rows, it cannot go up on the board. Return 0
		if player_place2 < 9:
			print('Player cannot move')
			return 0
		#Otherwise, player can move for 1 square up and return -9	
		else:	
			print('Going for one square up')
			return -9
	#Player goes 2 square right and return 2		
	elif dice2 == 6:
		print('Going for two squares right')
		return 2
	#Player goes 2 square left and return -2	
	elif dice2 == 7:
		print('Going for two squares left')
		return -2
	#Player goes 2 square down and return -18	
	elif dice2 == 8:
		print('Going for two squares down')
		return 18
		
	elif dice2 == 9:
		#If the player located in the first 18 rows, it cannot go down on the board. Return 0
		if player_place2 <  18:
			print('Player cannot move')
			return 0
		else:	
	        #Otherwise, player can move for 2 square up and return -18
			print('Going for two square up')
			return -18	
	else:
		#If the player located in the first 27 rows, it cannot go up on the board. Return 0
		if player_place2 < 27:
			print('Player cannot move')
			return 0
		#Otherwise, player can move for 3 square up and return -27	
		else:	
			print('Going for three squares up')
			return -27		


#For the first time, first player's location. The start point for player 1	
player1_place = 68

#For the first time, second player's location. The start point for player 2
player2_place = 5

#Explaining the game
print('Welcome to the game! There are two players in this game, and they are positioned opposite each other. There is a dice (ten sided). Each number has a rule for the game. First to reach the other side, it will win the game!')		

input('Enter to proceed: ')

#Creating an infinite loop
while True:
	#Board game's rows
	w = 9

	#Board game's column
	h = 9

	#each squares dimensions
	dim = 50

	#creating a window
	window = pygame.display.set_mode((450,400))

	#painting on window with white color
	window.fill((255,255,255))

	#Making board and there are 72 squares in it
	for r in range(w):
		for c in range(h):
			pygame.draw.rect(window, (0,0,0), (c*dim,r*dim,dim,dim), width=1)
	
	#First player playig	
	print('Player 1 is playing.')
	
	#First dice is resulted after random.randint() function for player 1
	dice1 = random.randint(1,10)
	
	#After the dice, The new location is changed for player 1
	player1_place += dice_movement1(dice1, player1_place)
	
	#If player 1 reaches first 9 squares, player 1 wins the game
	if player1_place < 10:
		print('Player 1 won the game!')
		break
	#Otherwise, the new location is updated on the board for player 1	
	else:
		move_update_1(player1_place)	
		
	print('***************************************************************************************************')
	
	#Player 2 turn
	print('Player 2 is playing!')
	
	#Second dice is resulted after random.randint() function for player 2
	dice2 = random.randint(1,10)
	
	#After the dice, The new location is changed for player 2
	player2_place += dice_movement2(dice2 , player2_place)
	
	#If player 2 reaches last 9 squares, player 2 wins the game
	if player2_place> 64:
		print('Player 2 won the game!')
		break
	#Otherwise, the new location is updated on the board for player 2	
	else:
		move_update_2(player2_place)
		
	print('*************************************************************************************************')
	
	input('Enter to proceed')

#Screen updating
pygame.display.update()

#Seeing the window for 2 sec
pygame.time.delay(2000)
