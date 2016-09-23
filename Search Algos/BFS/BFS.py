#with open('input.txt') as f1:
#	data=f1.read()
#   	tan_list = data.splitlines()

#start=tan_list[1]
#goal=tan_list[2]
#live_lines=tan_list[3]

#import numpy as nu

words = []
#newList=[]
for line in open('i2.txt'):
	words.extend(line.split())

algo=words[0]
start=words[1]
goal=words[2]
live_lines=int(words[3])
ll=live_lines*3
graph1={}


#print (words)
#my_array = nu.asarray(words)
#print my_array


def fill_graph():
	for v in range(4,ll+4,3):
		if(graph1.has_key(words[v])==False):
			graph1[words[v]]=[words[v+1]]
		elif(graph1.has_key(words[v])==True):
			graph1[words[v]] = graph1.get(words[v], ()) + [words[v+1]]

fill_graph()
#print (graph1)

def bfs(graph, start, end):
    # maintain a queue of paths
	queue = []
    # push the first path into the queue
	queue.append([start])
	while queue:
        # get the first path from the queue
		path = queue.pop(0)
        # get the last node from the path
		node = path[-1]
        # path found
		if node == end:
            		return path
        # enumerate all adjacent nodes, construct a new path and push it into the queue
		for adjacent in graph.get(node, []):
			new_path = list(path)
			new_path.append(adjacent)
			queue.append(new_path)

#print (bfs(graph1, start, goal))
path = bfs(graph1, start, goal)

output = open("ou1.txt","wr+")
for i in range(0,len(path)):
	output.write(path[i]+" "+str(i)+"\n")