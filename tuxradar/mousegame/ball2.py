from pygame import *
import random

ballpic = image.load('ball.png')
ballpic.set_colorkey((0,0,0))		# Black

numballs = 10
delay = 5
collision_detection = 0

done = False

balls = []		# Blank dict

for count in range(numballs):
	balls.append(dict)
	balls[count] = {'x': 320, 'y': 0, 'xmove': random.randint(-4,4), 'ymove': random.randint(1, 4)}

init()
screen = display.set_mode((640, 480))
display.set_caption('Ball game')
event.set_grab(1)


while done == False:
	screen.fill(0)

	for count in range(numballs):
		screen.blit(ballpic, (balls[count]['x'], balls[count]['y']))

	# Wait a few seconds before turning on collision to let the balls spread out
	if (time.get_ticks()/1000) > 3:
		collision_detection = 1

	display.update()

	time.delay(delay)

	for count in range(numballs):
		balls[count]['x'] += balls[count]['xmove']
		balls[count]['y'] += balls[count]['ymove']

	for count in range(numballs):
		if balls[count]['x'] > 620:
			balls[count]['xmove'] = random.randint(-2, 0)
		if balls[count]['x'] < -10:
			balls[count]['xmove'] = random.randint(0, 2)
		if balls[count]['y'] > 470:
			balls[count]['ymove'] = random.randint(-2, 0)
		if balls[count]['y'] < -10:
			balls[count]['ymove'] = random.randint(0, 2)

	for e in event.get():
		if e.type == KEYUP:
			if e.key == K_ESCAPE:
				done = True
	
	if collision_detection == 1:
		for ball1 in range(numballs):
			for ball2 in range(ball1, len(balls)):
			#((x-x1)^2 + (y-y1)^2) < 256
				sidex = (balls[ball1]['x'] - balls[ball2]['x'])
				sidey = (balls[ball1]['y'] - balls[ball2]['y'])
				if ((sidex * sidex) + (sidey * sidey)) < 1024:
					# We have a collision
					tempx = balls[ball1]['xmove']
					tempy = balls[ball1]['ymove']
					balls[ball1]['xmove'] = balls[ball2]['xmove']
					balls[ball1]['ymove'] = balls[ball2]['ymove']
					balls[ball2]['xmove'] = tempx
					balls[ball2]['ymove'] = tempy
					
	if screen.get_at((mouse.get_pos())) == (255, 255, 255, 255):
		if collision_detection == 1:
			done = True
	
print "You lasted for", time.get_ticks()/1000, "seconds!"
