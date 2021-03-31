import pygame, sys, random, json
from pygame.locals import *

def title():
	global screenx, screeny, screen, base_color_light, base_color_medium, base_color_dark, fps, clock

	screenx = 720
	screeny = 720
	base_color_light  = (155,155,155)
	base_color_medium = (113,113,113)
	base_color_dark   = ( 53, 53, 53)
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
	died = False

	with open('gamestate', 'r') as f:
		current_map_number = json.loads(json.load(f))[0]
	map_dict = sv_load(current_map_number)

	player = pygame.rect.Rect(5, 5, screenx/10 - 20, screenx/10 - 20)

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
			player = death(player, map_dict['map_spawn'])
			died = True
 
		if pressed_up:
			player.y += -speed
		if pressed_down:
			player.y += speed
		if pressed_left:
			player.x += -speed
		if pressed_right:
			player.x += speed

		screen.fill(base_color_light)
		yarnar = mp_draw(map_dict, player, died)
		if yarnar:
			current_map_number += 1
			map_dict = sv_load(current_map_number)
			sv_save(current_map_number)
		pygame.draw.rect(screen, base_color_dark, player)

		pygame.display.update()
		if died:
			# print('Died.  ' + str(random.randint(100, 999)))
			pygame.time.wait(500)
			died = False
		clock.tick(fps)



def win():
	pass

def mp_draw(map_dict, player, died):
	width = screenx/10
	for enum2, row in enumerate(map_dict['map_strc']):
		for enum1, item in enumerate(row):
			if item == 0:
				pygame.draw.rect(screen, base_color_light, (enum2*width, enum1*width, width, width))
			elif item == 1:
				pygame.draw.rect(screen, base_color_medium, (enum2*width, enum1*width, width, width))
				if player.colliderect((enum2*width, enum1*width, width, width)):
					player = death(player, map_dict['map_spawn'])
					died = True
			elif item == 2:
				pygame.draw.rect(screen, base_color_dark, (enum2*width, enum1*width, width, width))
				if player.colliderect((enum2*width, enum1*width, width, width)):
					return True
	return False

def sv_load(current_map_number):
	with open(f'maps/{current_map_number}.mapp', 'r') as f:
		map_dict = json.loads(json.load(f))
		return map_dict

def sv_save(current_map_number):
	with open('gamestate', 'w') as f:
		json.dump(json.dumps([current_map_number]))

def death(player, spawn_point):
	player.topleft = (spawn_point[0] + 10, spawn_point[1] + 10)
	return player

if __name__ == '__main__':
	while True:
		title()
		main()
		win()