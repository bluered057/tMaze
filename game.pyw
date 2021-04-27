import pygame, sys, random, json
from pygame.locals import *

def title():
	global screenx, screeny, screen, fps, clock

	screenx = 720
	screeny = 720
	text_color = (255,255,255)
	high_color = (255,255,255)
	back_color = (255,255,255)
	fps = 60

	screen = pygame.display.set_mode((screenx, screeny))
	pygame.display.set_caption('tMaze')

	clock = pygame.time.Clock()

def main():
	speed = 5
	pressed_up = False
	pressed_down = False
	pressed_left = False
	pressed_right = False
	ded_num = 0
	died = False

	with open('gamestate', 'r') as f:
		current_map_number = int(json.loads(json.load(f))[0])
	map_dict = sv_load(current_map_number)

	player = pygame.rect.Rect(map_dict['spawn'][0], map_dict['spawn'][1], screenx/map_dict['width'] - screenx/map_dict['width']/4, screenx/map_dict['height'] - screenx/map_dict['height']/4)
	player.topleft = (map_dict['spawn'][0] + 5, map_dict['spawn'][1] + 5)

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			elif event.type == KEYDOWN:
				if event.key == K_w:
					pressed_up = True
				elif event.key == K_s:
					pressed_down = True
				elif event.key == K_a:
					pressed_left = True
				elif event.key == K_d:
					pressed_right = True

			elif event.type == KEYUP:
				if event.key == K_w:
					pressed_up = False
				elif event.key == K_s:
					pressed_down = False
				elif event.key == K_a:
					pressed_left = False
				elif event.key == K_d:
					pressed_right = False

		if ((player.right > screenx or player.left < 0) or (player.bottom > screeny or player.top < 0)):
			player = death(player, map_dict['spawn'])
			died = True
 
		if not died:
			if pressed_up:
				player.y += -speed
			if pressed_down:
				player.y += speed
			if pressed_left:
				player.x += -speed
			if pressed_right:
				player.x += speed

		screen.fill(map_dict['color1'])
		yarnar = mp_draw(map_dict, player, died)
		if yarnar:
			current_map_number += 1
			if current_map_number > 3:
				win()
			map_dict = sv_load(current_map_number)
			sv_save(current_map_number)
		pygame.draw.rect(screen, map_dict['color3'], player)

		pygame.display.update()
		if died:
			ded_num += 1
			print('Died.  ' + str(ded_num) + str(1000 + random.randint(100, 999)))
			pygame.time.wait(5)
			died = False
		clock.tick(fps)



def win():
	pass

def mp_draw(map_dict, player, died):
	width = screenx/10
	# print(map_dict)
	for enum1, row in enumerate(map_dict['structure']):
		for enum2, item in enumerate(row):
			if item == 0:
				pygame.draw.rect(screen, map_dict['color1'], (enum2*width, enum1*width, width, width))
			elif item == 1:
				pygame.draw.rect(screen, map_dict['color2'], (enum2*width, enum1*width, width, width))
				if player.colliderect((enum2*width, enum1*width, width, width)):
					# player = death(player, map_dict['spawn'])
					died = True
			elif item == 2:
				pygame.draw.rect(screen, map_dict['color3'], (enum2*width, enum1*width, width, width))
				if player.colliderect((enum2*width, enum1*width, width, width)):
					return True
	return False

def sv_load(current_map_number):
	with open(f'maps/{str(current_map_number)}.mapp', 'r') as f:
		map_dict = json.loads(json.load(f))
		return map_dict

def sv_save(current_map_number):
	with open('gamestate', 'w') as f:
		json.dump(json.dumps([str(current_map_number)]), f)

def death(player, spawn_point):
	player.topleft = (spawn_point[0] + 5, spawn_point[1] + 5)
	return player

if __name__ == '__main__':
	while True:
		title()
		main()
		win()