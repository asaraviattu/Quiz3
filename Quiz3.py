def dot(vector01,vector02):
	'''
	This function takes two vectors as it's arguments and returns the dot product of them. First
	we identify whether or not the vectors are of same size, if they are continue if not we print 
	invalid input. If we continue then we execute the algorithm to find the dot product.

	'''

	sum = 0
	if len(vector01) != len(vector02):
		print("invalid input")

	else:
		for i in range(len(vector01)):
			sum += (vector01[i] * vector02[i])
		return sum



validInput1 = [1,1,1]
validInput2 = [1,1,1]
invalidInput1 =  [1,2,3]
invalidInput2 = [1,2]

print(dot(validInput1,validInput2))
print(dot(invalalidInput1,invalidInput2))


