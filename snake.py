import pygame, time, random
from pygame import mixer

pygame.init()

# Starting the mixer
mixer.init()
  
# Loading the song
mixer.music.load("coin.mp3")
  
# Setting the volume
mixer.music.set_volume(0.2)

pygame.display.set_caption('Snake!')
mainClock = pygame.time.Clock()

green = (50,205,50)
yellow = (255, 255, 0)
red = (255,0,0)
black = (0,0,0)

frameRate = 120

if pygame.get_init():
	print("Success")
else:
	print("Critical, exiting")
	exit()

def our_snake(snake_block, snake_list, foodx, foody):
	theCount = 1
	
	for x in snake_list:
		if theCount >= len(snake_List):
			snake = pygame.draw.rect(surface, green, [x[0], x[1], snake_block, snake_block])
			theCount += 1
		else:
			pygame.draw.rect(surface, red, [x[0], x[1], snake_block, snake_block])
			theCount += 1
		pygame.draw.rect(surface, yellow, [foodx, foody, snake_block, snake_block])

def spawnFood(foodx, foody, snake_list):
	bGood = True
	while bGood:
		foodx = random.randrange(0,surfaceSize[0]-25+1,25)
		foody = random.randrange(0,surfaceSize[1]-25+1,25)
		newlist = []
		newlist.append(foodx)
		newlist.append(foody)
		for x in snake_list:
			if x == newlist:
				bGood = True
				break
			else:
				bGood = False
	return foodx, foody
	
foodx = 0
foody = 0

surfaceSize = 600, 600

snake_block = 25

surface = pygame.display.set_mode(surfaceSize, pygame.RESIZABLE)
surface.fill((0, 0, 0))

snake_x_d = 0 
snake_y_d = 0

Length_of_snake = 3
snake = pygame.draw.rect(surface, green, pygame.Rect(snake_x_d, snake_y_d, snake_block, snake_block))
snake_List = []
snake_Head = []
snake_Head.append(snake.x)
snake_Head.append(snake.y)
snake_List.append(snake_Head)

snake_x = 0
snake_y = 25

movement_cooldown = 0.05
bCanPressKey = True
last_moved_time = 0

foodx, foody = spawnFood(foodx, foody, snake_List)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
			
		if bCanPressKey:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					if snake_y is not 25:
						snake_x = 0
						snake_y = -25
				if event.key == pygame.K_DOWN:
					if snake_y is not -25:
						snake_x = 0
						snake_y = 25
				if event.key == pygame.K_LEFT:
					if snake_x is not 25:
						snake_x = -25
						snake_y = 0
				if event.key == pygame.K_RIGHT:
					if snake_x is not -25:
						snake_x = 25
						snake_y = 0
				bCanPressKey = False
	
	for x in snake_List[:-1]:
		if x == snake_Head:
			exit()

	if snake.x >= surfaceSize[0] or snake.x < 0 or snake.y >= surfaceSize[1] or snake.y < 0:
		exit()
	
	if len(snake_List) > Length_of_snake:
		del snake_List[0]
	
	if snake.y == foody and snake.x == foodx:
		foodx, foody = spawnFood(foodx, foody, snake_List)
		# Start playing the song
		mixer.music.play()
		Length_of_snake += 1
	
	if time.time() - last_moved_time > movement_cooldown:
		snake.move_ip(snake_x, snake_y)
		surface.fill(black)
		our_snake(snake_block, snake_List, foodx, foody)
		
		snake_Head = []
		snake_Head.append(snake.x)
		snake_Head.append(snake.y)
		snake_List.append(snake_Head)
		
		last_moved_time = time.time()
		bCanPressKey = True

	pygame.display.flip()
	pygame.display.update()
	mainClock.tick(frameRate)
