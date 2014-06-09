from classes import *
from functions import *



#variable number of Bachelor/ettes
numPairs = 100

"""
Runs a randomizer to generate random preferences, then
runs the stable matching algorithm on those preferences
"""
if __name__ == "__main__":
	bachelors = []
	bachelorettes = []
	randomizeBachelors(bachelors, numPairs)
	randomizeBachelorettes(bachelorettes, numPairs)
	doGaleShapley(bachelors, bachelorettes)
	printMarriages(bachelors, bachelorettes)