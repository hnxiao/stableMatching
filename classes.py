class SinglePerson:
	def __init__(self, id, preferences):
		self.name = id
		self.preferences = preferences
		# -1 means that person is not currently engaged
		# any other number is the current person they are engaged with
		self.partner = -1
		self.proposed = []
	def printPreferenceList(self):
		print self.name, self.preferences
	def engage(self, partner):
		self.partner = partner
		self.proposed.append(partner)

class Bachelor(SinglePerson):
	def hasProposedToAll(self, size):
		return len(self.proposed) == size
	def hasProposedTo(self, prospectId):
		return prospectId in self.proposed
	def getHighestNotYetProposed(self):
		for i, val in enumerate(self.preferences):
			if val not in self.proposed:
				return val
		return -1

class Bachelorette(SinglePerson):
	# whether she prefers bachelor 1 to bachelor 2
	def prefers(self, bachelor1, bachelor2):
		return self.preferences.index(bachelor1) < self.preferences.index(bachelor2)