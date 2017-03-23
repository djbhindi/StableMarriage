# A class which represents a pref object (male or female), taking in a preference list (or none)
class pref:
	def __init__(self, *args):
		self.name = args[0]
		self.prefList = []
		self.currentSuitor = None # Always none for a man
		self.male = False # Keeps track of male or female; used in later functions
		self.accepted = False

		for i in range(1, len(args)):
			if not type(args[i])==pref:
				print("Illegal argument(s).")
				break
			else:
				self.prefList.append(args[i].name)

			# Check male based on the convetion 1,2... = men; A,B... = women
			if self.name.isdigit():
				self.male = True

	# Add a preference to the end of the preference list
	def addPref(self, *args):
		for i in range(len(args)):
			if not type(args[i])==pref:
				print("Illegal argument(s).")
				break
			else:
				self.prefList.append(args[i].name)

	# Find the index of the placement of another person on one's preference list
	def findIndex(self, pref):
		for i in range(len(self.prefList)):
			if self.prefList[i] == pref.name:
				return i
		print("Pref Name wasn't found.")
		return -1

	# For a woman: pick between two men based on their indices; reject the beta male
	def pickPref(self, pref1, pref2):
		if self.findIndex(pref1) > self.findIndex(pref2):
			pref1.reject()
			return pref2
		else:
			pref2.reject()
			return pref1

	# Does nothing for men; for women, look through all the men in the list given and pick the best.
	# Reject all other suitors and assign the best to the 'currentSuitor' variable
	def runAlgoStep(self, suitorList):
		if not self.male: 
			if len(suitorList) == 0:
				return
			if self.currentSuitor is None:
				self.currentSuitor = suitorList[0]

			for suitor in suitorList:
				self.currentSuitor = self.pickPref(suitor, self.currentSuitor)
			self.currentSuitor.accept()
			#print(self.currentSuitor.name + " is accepted: " + str(self.currentSuitor.accepted))

	# Method for males: remove the topmost preference (who just rejected you). 
	# Also, set accepted to false (in case you were previously accepted and just got bumped off.)
	def reject(self):
		self.prefList.pop(0)
		self.accepted = False

	def accept(self):
		self.accepted = True

	def checkSuitor(self):
		if not self.male and self.currentSuitor is None:
			return False
		else:
			return True

# Run the actual algorithm
def runAlgorithm(num, maleList, femList):
	alphabet = [chr(i) for i in range(65, 91)]
	g = globals()
	l = locals()

	# Lists that keep track of al the suitors for every woman
	for i in range(num):
		l[alphabet[i]+"list"]  = []

	checkFinished = False

	while checkFinished is False:
		# First, assign each man to his preference's suitor list
		for man in maleList:
			if not man.accepted:
				luckyGirl = man.prefList[0]
				l[luckyGirl+"list"].append(man)

		# Each woman goes through her list, picking the best suitor or sticking with what she has
		for woman in femList:
			woman.runAlgoStep(l[woman.name+"list"])

		# Reset the lists to none, as the men will move around based on the last step
		for i in range(num):
			l = locals()
			l[alphabet[i]+"list"]  = []

		checkFinished = True

		# Keep running the algorithm if any men or women are unassigned
		for woman in femList:
			if not woman.checkSuitor():
				checkFinished = False
		for man in maleList:
			if not man.accepted:
				checkFinished = False

# Self explanatory
def printResult(women):
	for woman in women:
		print(woman.name + " is with " + woman.currentSuitor.name + ".")
