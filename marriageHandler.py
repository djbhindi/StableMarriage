from stableMarriage import *

# Handler: queries user for the setup of what they want.
def handler():
	num = False
	while not num:
		num = input("How many men/women do you want?\n")
		try:
   			num = int(num)
		except ValueError:
   			print("That's not an number!")
   			num = False
		if num > 26:
   			print("Only 26 couples currently supported; sorry!")
   			num = False
	
	g = globals()
	alphabet = [chr(i) for i in range(65, 91)]
	maleList, femList = [], []
	exampleString1 = ""
	exampleString2 = ""


	for i in range(num):
		g["M" + str(i+1)] = pref(str(i+1))
		g[alphabet[i]]  = pref(alphabet[i])

		maleList.append(g["M" + str(i+1)])
		femList.append(g[alphabet[i]])

		if exampleString1 == "":
			exampleString1 += str(i+1)
		else:
			exampleString1 += "," + str(i+1)
		if exampleString2 == "":
			exampleString2 += alphabet[i]
		else:
			exampleString2 += "," + alphabet[i]

	# Scan in women's choices
	for i in range(num):
		preferencesValid = False
		while not preferencesValid:
			print("Enter a preference list for Woman " + alphabet[i] + ". Example: " + exampleString1)
			prefInput = input()
			try:
				preferences = list(map(int, prefInput.split(',')))
			except ValueError:
				print("No strings/chars please! Only ints!")
				continue
			if len(preferences) == num and max(preferences) == num and min(preferences) > 0:
				preferencesValid = True
			else:
				print("Too many, too few, or invalid preferences (out of range, negative, etc.)")
			#print("Woman " + alphabet[i] + "'s preferences: " + str(preferences))
			
		for prefNum in preferences:
			g[alphabet[i]].addPref(g["M"+str(prefNum)])

	# Scan in men's choices
	for i in range(1, num+1):
		preferencesValid = False
		while not preferencesValid:
			print("Enter a preference list for Man " + str(i) + ". Example: " + exampleString2)
			prefInput = input()
			preferences = prefInput.split(',')
			#print("Woman " + alphabet[i] + "'s preferences: " + str(preferences))

			if len(preferences) == num and max(list(map(ord, preferences))) == 64+num and max(list(map(ord, preferences))) > 65:
				preferencesValid = True
			else:
				print("Too many, too few, or invalid preferences (out of range, non-char, etc.)")
		for prefChar in preferences:
			g["M" + str(i)].addPref(g[prefChar])

	# Run the algorithm
	runAlgorithm(num, maleList, femList)
	printResult(femList)

handler()
