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


#valid and invalid inputs to test and their respective tests commented out below.

validInput1 = [1,1,1]
validInput2 = [1,1,1]
invalidInput1 =  [1,2,3]
invalidInput2 = [1,2]

#print(dot(validInput1,validInput2))
#print(dot(invalalidInput1,invalidInput2))





def vecSubtract(vector03,vector04):
	'''
	This functions takes two vectors as arguments and returns a new vector with the respective subraction. We
	first create an empty list, then check for dimensions of inputs and if they checkout, execute subraction 
	and append element's subraction onto empty list in order to create new list with subraction finished.

	'''
	newVec = []
	if len(vector03) != len(vector04):
		print("invalid input")

	else:
		for i in range(len(vector03)):
			sum = vector03[i] - vector04[i]
			newVec.append(sum)
	return newVec



#valid and invalid inputs to test and their respective tests commented out below.

validInput3 = [3,4,5]
validInput4 = [1,1,1]
invalidInput3 = [2,2,2]
invalidInput4 = [1,1]

#print(vecSubtract(validInput3,validInput4))
#print(vecSubtract(invalidInput3,invalidInput4))



def scalarVecMulti(scalar01,vector05):
	'''
	This functions takes a scalar and a vector as arguments and returns a new vector with the respective
	multiplication executed. The if-else statement checks for the scalar and vector to bbe either integers
	or lists, if they are then we proceed to execute the multiplication by appending to an empty list the
	result of the executed multiplication between the scalar and each individual element in the vector.

	'''
	newVec = []
	if type(scalar01) != int or type(vector05) != list:
		print("invalid input")
	else:
		for i in range(len(vector05)):
			mult = vector05[i]*scalar01
			newVec.append(mult)

		return newVec


validInput5 = 2
validInput6 = [1,2,3]
invalidInput5 = [1,1,1]
invalidInput6 = 3

#valid and invalid inputs to test and their respective tests commented out below.

#print(scalarVecMulti(validInput5,validInput6))
#print(scalarVecMulti(invalidInput5,invalidInput6))

























