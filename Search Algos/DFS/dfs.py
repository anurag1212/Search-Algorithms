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


#print words

def fill_graph():
	for v in range(4,ll+4,3):
		if(graph1.has_key(words[v])==False):
			graph1[words[v]]=[words[v+1]]
		elif(graph1.has_key(words[v])==True):
			graph1[words[v]] = graph1.get(words[v], ()) + [words[v+1]]
	for node in graph1.keys():
	    for node1 in graph1[node]:
	        if not graph1.has_key(node1):
	            graph1[node1]=[node1]

fill_graph()
print graph1

def dfs_path(graph, start, goal):
    paths = []
    stack = [(start, [start])]

    while stack:
        (vertex, path) = stack.pop(0)
        vertices = graph1[vertex]
        for x in path:
            if x in vertices:
                vertices.remove(x)
        for next_vertex in vertices:
            #print list(vertices)
            new_path = path + [next_vertex]
            if next_vertex == goal:
                paths.append(new_path)
            else:
                stack.insert(0, (next_vertex, new_path))
    return paths[-1]

print dfs_path(graph1, start, goal)
path = dfs_path(graph1, start, goal)

output = open("ou1.txt","w")
for i in range(0,len(path)):
	output.write(path[i]+" "+str(i)+"\n")