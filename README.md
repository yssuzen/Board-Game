# Board Game

The program aims to simulate a two-player board game with a simple design. The board consists of 81 squares (9x9), and each player starts at the opposite sides of the board. The game has a dice, which generates a random number between 1 and 10. The players take turns rolling the dice and moving on the board accordingly. The first player needs to reach the last row of the board, while the second player needs to reach the first row.

The code has two main functions that simulate the movement of the players. The move_update_1 function updates the position of the first player on the board. It takes the current location of the player and calculates where it will be placed after rolling the dice. The move_update_2 function updates the position of the second player on the board.

The dice_movement1 and dice_movement2 functions simulate the movement of the players on the board based on the dice result. They take the dice value and the current position of the player as inputs and return the new position of the player after the move. Each dice value corresponds to a certain movement on the board, such as moving up, down, right, or left. If a player rolls a 2, they can make a double move and move four squares instead of two. The game also has some rules, such as a player cannot move out of the board or move to a square where another player is currently located.

The code uses the Pygame module to create a visual representation of the game. It draws a blue rectangle for the first player and a pink rectangle for the second player. The pygame.draw.rect function is used to draw the rectangles on the board. The pygame.display.update function updates the display, and the pygame.time.delay function adds a delay between the movements of the players.
