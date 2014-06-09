from classes import *
import random

def manIsFreeAndNotProposedToAll(bachelors, numPairs):
	for bachelor in bachelors:
		if bachelor.partner == -1 and not bachelor.hasProposedToAll(numPairs):
			return bachelor.name
	return -1

def getPersonById(people, id):
	for person in people:
		if person.name == id:
			return person


if __name__ == "__main__":
	# variable number of Bachelor/ettes
	numPairs = 10

	bachelors = []
	bachelorettes = []

	# randomize bachelor/ette preferences
	for x in range(0, numPairs):
		preferenceList1 = range(0, numPairs)
		random.shuffle(preferenceList1)
		newBachelor = Bachelor(x, preferenceList1)
		bachelors.append(newBachelor)

		preferenceList2 = range(0, numPairs)
		random.shuffle(preferenceList2)
		newBachelorette = Bachelorette(x, preferenceList2)
		bachelorettes.append(newBachelorette)


	# Gale-Shapley algorithm

	# Initially all Bachelors and Bachelorettes are free
	# while there is a man m who is free and hasn't proposed to every woman
	workingBachelorId = 0
	while workingBachelorId > -1:
		#choose such a man m
		workingBachelor = getPersonById(bachelors, workingBachelorId)
		# Let w be the highest-ranked w to which m has not yet proposed
		workingBacheloretteId = workingBachelor.getHighestNotYetProposed()
		workingBachelorette = getPersonById(bachelorettes, workingBacheloretteId)
		# if w is free, then m, w get engaged
		if workingBachelorette.partner == -1:
			workingBachelor.engage(workingBacheloretteId)
			workingBachelorette.engage(workingBachelorId)
		else:
			if workingBachelorette.prefers(workingBachelorId, workingBachelorette.partner):
				divorcedBachelorId = workingBachelorette.partner
				divorcedBachelor = getPersonById(bachelors, divorcedBachelorId)
				divorcedBachelor.partner = -1
				workingBachelor.engage(workingBacheloretteId)
				workingBachelorette.engage(workingBachelorId)
			else:
				workingBachelor.proposed.append(workingBacheloretteId)
		workingBachelorId = manIsFreeAndNotProposedToAll(bachelors, numPairs)

	for bachelor in bachelors:
		bachelor.printPreferenceList()
		print bachelor.partner