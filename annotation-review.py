import random
def doIt(a:int) -> list:
	myList= []
	max = random.randrange(2,10,2)
	# print (max)

	for n in range (0,max):
		myList.append(a)

	return myList

print(doIt.__annotations__)

def doMore(x):
	lengthOFList = (len(x))
	# print(lengthOFList)
	x.insert(lengthOFList//2,"foo")
	music = iter(x)
	print(x)
	return music

testIt = doMore(doIt(2))

for n in testIt:
	print (n)
	assert n == 2
	
# end

