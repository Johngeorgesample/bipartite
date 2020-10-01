print('WARNING: USE COMA (,) SEPERATED LISTS ONLY')
nodeInput = input('Enter all vertices in graph: ')
nodeList = nodeInput.split(',')
redList = []
blueList = []
intersect = []
isBipartite = True

print(nodeList)

for counter, i in enumerate(nodeList, 0):
	if(nodeList[counter] != nodeList[-1]):
		edgeAnswer = input("Is " + nodeList[counter] + " connected to " + nodeList[counter+1] + "? ")
		if(edgeAnswer=='y' and nodeList[counter] not in blueList):
			redList.append(nodeList[counter])
			blueList.append(nodeList[counter+1])

		elif(edgeAnswer=='y' and nodeList[counter] in blueList): #br
			redList.append(nodeList[counter+1])

		elif(edgeAnswer=='y' and nodeList[counter] in redList): #rb
			blueList.append(nodeList[counter+1])

		elif(edgeAnswer=='n' and nodeList[counter] in blueList): #bb
			blueList.append(nodeList[counter+1])

		elif(edgeAnswer=='n' and nodeList[counter] in redList): #rr
			redList.append(nodeList[counter+1])

for redNode, i in enumerate(redList, 0):
	if(redList[redNode] != redList[-1] and redList[redNode] != redList[redNode+1]):
		redEdgeAnswer = input("Is " + redList[redNode] + " connected to " + redList[redNode+1] + "? ")
		if(redEdgeAnswer=='y'):
			isBipartite = False


for blueNode, i in enumerate(blueList, 0):
	if(blueList[blueNode] != blueList[-1] and blueList[blueNode] != blueList[blueNode+1]):
		blueEdgeAnswer = input("Is " + blueList[blueNode] + " connected to " + blueList[blueNode+1] + "? ")
		if(blueEdgeAnswer=='y'):
			isBipartite = False

if(isBipartite):
	print("Is bipartite")
else:
	print("Not bipartite")
