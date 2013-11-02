from pygame import *	# Why this instead of just import pygame?

ballpic = image.load('ball.png')

done = False

ballx = 0		# ball_x would be easier to read
bally = 0
ballxmove = 1		# velocity
ballymove = 1

init()
screen = display.set_mode((640,480))		# Is there an autodetect native resolution function?
display.set_caption('Balls in my mouth')

while done == False:
	screen.fill(0)		# Fill screen with black (color 0)
	screen.blit(ballpic, (ballx, bally))		# Does blit insert pic at center or at bottom-left corner?
	display.update()

	time.delay(1)		# Slow it down!

	ballx += ballxmove		# Update ball position
	bally += ballymove

	if ballx > 600:		# Ball reached screen edges?
		ballxmove = -1
	if ballx < 0:
		ballxmove = 1
	if bally > 440:
		ballymove = -1
	if bally < 0:
		ballymove = 1

	for e in event.get():	# Check for ESC pressed
		if e.type == KEYUP:
			if e.key == K_ESCAPE:
				done = True
