import random
import math


def orderbyfitness(pop, target):
	for i in pop:
		i[2] = math.hypot(target[0]-i[0][0], target[1]-i[0][1])
		if i[3]:
			i[2] += 0.25 * i[2]
	pop = sorted(pop, key=lambda x: x[2])
	return pop


def createnewgeneration(srtdpop, imrtltypct, bestlist, target, startloc):
	bestlist.append(math.hypot(target[0]-srtdpop[0][0][0], target[1]-srtdpop[0][0][1]))
	mvmtlen = len(srtdpop[0][1])
	popsize = len(srtdpop)
	mapval=10/popsize
	newpop = []
	for i in range(int(round(imrtltypct*popsize))): newpop.append(srtdpop[i])
	biasedmap = [2 ** (random.uniform(0, 10) - 7) for i in range((popsize - len(newpop))*mvmtlen)]
	for i in range(popsize-len(newpop)):
		mvs = []
		for ii in range(mvmtlen):
			if random.randint(1,5) == random.randint(1,5):
				popnum = random.randint(1,8)
			else:
				popnum = int(round(biasedmap[i*ii]/mapval))
			mvs.append(srtdpop[popnum][1][ii])
		newpop.append([list(startloc),mvs,None,False])
	for i in newpop:
		i[0] = list(startloc)
	return newpop, bestlist
