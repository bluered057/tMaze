import json

map_basic = [
	[0,0,0,0,0,0,1,0,0,0],
	[0,1,1,1,1,0,1,0,1,1],
	[0,1,0,0,1,0,1,0,1,0],
	[0,1,0,1,1,0,1,0,1,0],
	[0,1,0,0,0,0,1,0,1,0],
	[0,1,1,1,1,0,0,0,0,0],
	[0,1,0,2,1,0,1,1,1,1],
	[0,1,0,1,1,0,1,0,0,0],
	[0,1,0,0,1,0,1,1,1,0],
	[1,1,1,0,0,0,0,0,0,0]
]

map_spawn = (504,144)
map_color1 = (200,200,200)
map_color2 = (150,150,150)
map_color3 = (100,100,100)
width = 10
height = 10
write_info = {'spawn':map_spawn, 'structure':map_basic, 'color1':map_color1, 'color2':map_color2, 'color3':map_color3, 'width':width, 'height':height}

with open('1.mapp', 'w') as f:
	json.dump(json.dumps(write_info), f)

empty_map_basic = [
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0]
]





