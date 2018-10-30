# geneticDots
genetic pathfinding algorithm

Basics
Creates map of obstacles (blue rectangles), a starting location (green dot), and a target location (red dot).
A population of size "popsize" is created with a random list of "steps". these steps are integers which correspond to a direction of motion for one step.
The program simulates the population by running each step consecutively. 
A genetic algorithm then uses the results of the simulation (the distance of each dot to the target and whether a dot hit an obstacle, to reproduce a new population.
The genetic algorithm creates new individuals which have a chances of inheriting steps from the best dots from the previous generation, as well as a small chance of random steps (mutation).
It repeats this process until one dot reaches the target when it will replay that dot's path and show a matplotlib graph of the progress of the algorithm (best individual vs generation).
