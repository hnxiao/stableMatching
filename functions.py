from classes import *
import random

def manIsFreeAndNotProposedToAll(bachelors):
	for bachelor in bachelors:
		if bachelor.partner == -1 and not bachelor.hasProposedToAll(len(bachelors)):
			return bachelor.name
	return -1

def getPersonById(people, id):
	for person in people:
		if person.name == id:
			return person

def randomizeBachelors(bachelors, numBachelors):
	for x in range(0, numBachelors):
		preferenceList1 = range(0, numBachelors)
		random.shuffle(preferenceList1)
		newBachelor = Bachelor(x, preferenceList1)
		bachelors.append(newBachelor)

def randomizeBachelorettes(bachelorettes, numBachelorettes):
	for x in range(0, numBachelorettes):
		preferenceList2 = range(0, numBachelorettes)
		random.shuffle(preferenceList2)
		newBachelorette = Bachelorette(x, preferenceList2)
		bachelorettes.append(newBachelorette)

def doGaleShapley(bachelors, bachelorettes):
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
			# if w prefers this m over her current fiance
			if workingBachelorette.prefers(workingBachelorId, workingBachelorette.partner):
				divorcedBachelorId = workingBachelorette.partner
				divorcedBachelor = getPersonById(bachelors, divorcedBachelorId)
				divorcedBachelor.partner = -1
				workingBachelor.engage(workingBacheloretteId)
				workingBachelorette.engage(workingBachelorId)
			# else m stays free
			else:
				workingBachelor.proposed.append(workingBacheloretteId)
		workingBachelorId = manIsFreeAndNotProposedToAll(bachelors)

def printMarriages(bachelors, bachelorettes):
	for bachelor in bachelors:
		bachelorette = getPersonById(bachelorettes, bachelor.partner)
		print "Bachelor", bachelor.name, "marries Bachelorette", bachelorette.name
		print "Husband",
		bachelor.printPreferenceList()
		print "Wife",
		bachelorette.printPreferenceList()
		print ""