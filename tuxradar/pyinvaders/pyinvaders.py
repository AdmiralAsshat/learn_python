from pygame import *
import random

class Sprite:
	def __init__(self, xpos, ypos, filename):
		self.x = xpos
		self.y = ypos
		self.bitmap = image.load(filename)
		self.bitmap.set_colorkey((0,0,0))
	def set_position(self, xpos, ypos):
		self.x = xpos
		self.y = ypos
	def render(self):
		screen.blit(self.bitmap, (self.x, self.y))

def Intersect(s1_x, s1_y, s2_x, s2_y):
	if (s1_x > s2_x - 32) and (s1_x < s2_x + 32) and (s1_y > s2_y - 32) and (s1_y < s2_y + 32):
		return 1
	else:
		return 0

init()
screen = display.set_mode((640,480))
key.set_repeat(1, 1)
display.set_caption('PyInvaders')
backdrop = image.load('data/backdrop.bmp')

enemies = []

x = 0

for count in range(10):
	enemies.append(Sprite(50 * x + 50, 50, 'data/baddie.bmp'))
	x += 1

hero = Sprite(20, 400, 'data/hero.bmp')
ourmissile = Sprite(0, 480, 'data/heromissile.bmp')
enemymissile = Sprite(0, 480, 'data/baddiemissile.bmp')

quit = 0
enemyspeed = 3

while quit == 0:
	screen.blit(backdrop, (0, 0))

	for count in range(len(enemies)):
		enemies[count].x += enemyspeed
		enemies[count].render()

	if enemies[len(enemies)-1].x > 590:
			enemyspeed = -3
			for count in range(len(enemies)):
				enemies[count].y += 5

	if enemies[0].x < 10:
		enemyspeed = 3
		for count in range(len(enemies)):
			enemies[count].y += 5

	if ourmissile.y < 479 and ourmissile.y > 0:
		ourmissile.render()
		ourmissile.y -= 5

	if enemymissile.y >= 480 and len(enemies) > 0:
		enemymissile.x = enemies[random.randint(0, len(enemies) -1)].x
		enemymissile.y = enemies[0].y

	if Intersect(hero.x, hero.y, enemymissile.x, enemymissile.y):
		quit = 1

	for count in range(0, len(enemies)):
		if Intersect(ourmissile.x, ourmissile.y, enemies[count].x, enemies[count].y):
			del enemies[count]
			break

	if len(enemies) == 0:
		quit = 1

	for ourevent in event.get():
		if ourevent.type == QUIT:
			quit = 1
		if ourevent.type == KEYDOWN:
			if ourevent.key == K_RIGHT and hero.x < 590:
				hero.x += 5
			if ourevent.key == K_LEFT and hero.x > 10:
				hero.x -= 5
			if ourevent.key == K_SPACE:
				ourmissile.x = hero.x
				ourmissile.y = hero.y

	enemymissile.render()
	enemymissile.y += 5

	hero.render()

	display.update()
	time.delay(5)
