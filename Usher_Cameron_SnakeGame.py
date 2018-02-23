####Cameron Usher - Snake Game 2018.
####This game makes use to the PyGame package in Python and uses the Arrow keys to control the snake.
####This version of the snake game was modified from the tutorial posted by Syntec (on behalf of TheNewBoston.com)
####All modifications and changes I made are commented in-line below.

import pygame
import random
import time

# Starts pygame and clock
pygame.init()
clock = pygame.time.Clock()

# Define colors with rgb values
white = (0,0,0)
black = (255,255,255)
red = (244,36,36)
green = (28,239,42)

# Screen dimensions
display_width = 800
display_height  = 600

# Initialize game window and title
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Slither')

# Represents all objects
block_size = 10
# Frame rate (frames per second)
FPS = 30

# Draws the entire snake
def snake(block_size, snake_list):
	# Runs through each segment
	for segment in snake_list:
		# Segments consist of x and y coordinates
		lead_x, lead_y = segment
		# Draw each segment at a given location
		pygame.draw.rect(gameDisplay, green, [lead_x, lead_y, block_size, block_size])

# Initialize font
font = pygame.font.Font(None, 25)

# Convert the text string into a rectangle
def text_objects(text, color):
	text_surface = font.render(text, True, color)
	return text_surface, text_surface.get_rect()

# Prints text onto the screen
def message_to_screen(msg, color, y_displace=0):
	text_surface, text_rect = text_objects(msg, color)
	# Center the text object
	text_rect.center = (display_width/2), (display_height/2) + y_displace
	gameDisplay.blit(text_surface, text_rect)

# Runs the snake game
def gameLoop():
	gameExit = False
	gameOver = False

	# Current position of a snake block
	lead_x = display_width/2
	lead_y = display_height/2
	# Rate of change of movement, x and y indicate direction
	lead_x_change = 0
	lead_y_change = 0
	# Store each segment in a list
	snake_list = []
	snake_length = 1
	# Randomly generate position of an apple
	apple_x = round(random.randrange(0, display_width - block_size)/10.0)*10.0
	apple_y = round(random.randrange(0, display_height - block_size)/10.0)*10.0

	# Loop to run the current game or exit the current game
	while not gameExit:
		# Prompt user to start new game or exit
		while gameOver == True:
			# End game screen asking user what to do next
			gameDisplay.fill(white)
			text_play_again = "Press C to play again or Q to quit!"
			text_score = "You ate " + str(snake_length-1) + " apples!"
			message_to_screen("Game Over!", red, y_displace=-50)
			message_to_screen(text_play_again, black)
			message_to_screen(text_score, green, y_displace=50)
			pygame.display.update()
			# Ask for user input
			for event in pygame.event.get():
				# Pressing x on window
				if event.type == pygame.QUIT:
					gameExit = True
					gameOver = False
				# Running user commands from prompts
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameExit = True
						gameOver = False
					if event.key == pygame.K_c:
						gameLoop()

		# Get all events entered by the user
		for event in pygame.event.get():
			# Pressing the x button
			if event.type == pygame.QUIT:
				gameExit = True
			# Keydown defines the motion of a key only being pressed
			if event.type == pygame.KEYDOWN:
				# Change x velocity only when not previously moving right
				if event.key == pygame.K_LEFT and lead_x_change <= 0:
					# negative x motion indicates left movement
					lead_x_change = -block_size
					# Reset y motion to prevent diagonal motion
					lead_y_change = 0
				elif event.key == pygame.K_RIGHT and lead_x_change >= 0:
					lead_x_change = block_size
					lead_y_change = 0
				elif event.key == pygame.K_UP and lead_y_change <= 0:
					lead_x_change = 0
					lead_y_change = -block_size
				elif event.key == pygame.K_DOWN and lead_y_change >= 0:
					lead_x_change = 0
					lead_y_change = block_size

		# End the game when users move outside of screen dimensions
		if not 0 < lead_x <= display_width or not 0 < lead_y <= display_height:
			gameOver = True

		# Apply changes to position
		lead_x += lead_x_change
		lead_y += lead_y_change
		# Paint the background
		gameDisplay.fill(white)
		# Draw apple at the calculated random location
		pygame.draw.rect(gameDisplay, red, [apple_x, apple_y, block_size, block_size])
		# Create snake segment as list of x and y coordinates
		snake_segment = [lead_x, lead_y]
		snake_list.append(snake_segment)

		# When the length of the snake exceeds the limit defined, erase segment
		if len(snake_list) > snake_length:
			del snake_list[0]

		# Check for collision against itself
		for each in snake_list[:-1]:
			if each == snake_segment:
				gameOver = True
		# Once segment is added, snake() draws the segment list on the screen
		snake(block_size, snake_list)
		# This updates the screen and displays any changes
		pygame.display.update()

		# Test for collision with an apple
		if lead_x == apple_x and lead_y == apple_y:
			# At collision, generate new apple location to be drawn on next loop iteration
			apple_x = round(random.randrange(0, display_width - block_size)/10.0)*10.0
			apple_y = round(random.randrange(0, display_height - block_size)/10.0)*10.0
			# Grow the snake by one segment
			snake_length += 1

		# Sets boundaries for the while loop 
		clock.tick(FPS)
	# Quits the game and close the window
	pygame.quit()
	quit()

# Starts the loop
gameLoop()
