def HowManyIncreases(inputFilePath):
	increaseCounter = 0

	with open(inputFilePath, "r") as f:
		input = f.readlines()
		
		previousLine = "NA"

		for i in range(0, len(input)):
			if previousLine != "NA":
				if int(input[i]) > int(previousLine):
					increaseCounter += 1

			previousLine = int(input[i])

	return increaseCounter

print(HowManyIncreases("day-1/input.txt"))