import pygame
import matplotlib.pyplot as plt
from geneticalgorithm import *
import sys
print(sys.version)
pygame.init()
display_width = 600
display_height =600
white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
blue = (0,0,200)
green = (0,200,0)
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('geneticDots')
clock = pygame.time.Clock()
movekey = {1: (1, 1), 2: (1, 0), 3: (1, -1), 4: (0, -1), 5: (-1, -1), 6: (-1, 0), 7: (-1, 1), 8:(0, 1)}

################################################
obsticlenum = 20
popsize = 300
speed = 2000
# ^these variables may be changed with no change to anything else^


def setup(onum):
	startloc = (random.randint(50, 550), random.randint(50, 550))
	target = random.randint(50, 550), random.randint(50, 550)
	obsticlist = [(random.randint(10, 590), random.randint(25, 590), random.randint(25, 75), random.randint(25, 75)) for i in range(onum)]
	obsticalist =[]

	for i in obsticlist:
		obsticalist.append(pygame.draw.rect(gameDisplay,blue,i,0))

	for i in obsticalist:
		if startloc == target or pygame.Rect.collidepoint(i,target[0],target[1]) or pygame.Rect.collidepoint(i,startloc[0],startloc[1]):
			startloc, target, obsticlist, unused= setup(onum)

	dist = int(math.hypot(startloc[0]-target[0], startloc[1]-target[1]))
	stepcount = int(1.5*dist)
	return startloc, target, obsticlist, stepcount

def createinitpop(size, startloc, stepcount):
	pop = []
	for i in range(size): pop.append([list(startloc),[random.randint(1,8) for i in range(stepcount)],None, False])
	return pop


def movedots(pop, step):
	for i in pop:
		if not i[3]:
			i[0][0] += movekey[i[1][step]][0]
			i[0][1] += movekey[i[1][step]][1]
	return pop


def update(pop, generation, obsticlist, target, found, startloc):
	obsticalist = []
	exitsim = False
	pygame.draw.circle(gameDisplay, red, target, 3, 0)
	pygame.draw.circle(gameDisplay, green, startloc, 3, 0)
	for i in obsticlist:
		obsticalist.append(pygame.draw.rect(gameDisplay,blue,i,0))
	for i in pop:
		if found is not None: sprite = pygame.draw.rect(gameDisplay, black, tuple(i[0]+[1,1]), 0)
		else: sprite = pygame.draw.rect(gameDisplay, black, tuple(i[0]+[1,1]), 0)
		if i[0] == list(target):
			if found is None: found = list(i)
			else: exitsim = True
			break
		for ii in obsticalist:
			if pygame.Rect.colliderect(ii,sprite):
				i[3] = True
	tfont = pygame.font.SysFont('Comic Sans MS', 15)
	generations = 'Generation: ' + str(generation)
	textsurface = tfont.render(generations, False, black)
	gameDisplay.blit(textsurface, (10,10))

	return found, exitsim


def plotprog(generation, bestlist):
	plt.plot([i for i in range(1,generation)],bestlist)
	plt.xlabel('Generation')
	plt.ylabel('Best Individual Distance from Target')
	xint = []
	locs, labels = plt.xticks()
	for i in locs:
		xint.append(int(i))
	plt.xticks(xint)
	plt.show()

def quitsim():
	pygame.quit()
	quit()


def mainloop(speed):
	startloc, target, obsticlist, stepcount = setup(obsticlenum)
	bestlist = []
	generation = 1
	step = 0
	find = False
	pop = createinitpop(popsize, startloc, stepcount)
	exitsim = False
	found = None
	while not exitsim:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quitsim()
		if found is not None and not find:
			pop = []
			find = True
			found[0] = list(startloc)
			step = 0
			speed = 60
			pop.append(found)
		gameDisplay.fill(white)
		movedots(pop, step)
		found, exitsim= update(pop, generation, obsticlist,target, found,startloc)
		step +=1
		if step == stepcount and found is None:
			pop = orderbyfitness(pop, target)
			pop,bestlist = createnewgeneration(pop, 0.2,bestlist, target, startloc)
			step = 0
			generation += 1
		pygame.display.update()
		clock.tick(speed)
	if generation >=2:
		plotprog(generation,bestlist)

mainloop(speed)
