from collections import deque
from collections import OrderedDict
import Queue as Q

tan=[]

for line in open('input.txt'):
	tan.extend(line.split())

algo=tan[0]
start=tan[1]
dest=tan[2]
live_lines=int(tan[3])
ll=live_lines*3
sl=ll+4
sunday_lines=int(tan[sl])
#sl=int(sunday_lines)
graph1={}
graph2={}
sun={}
for i in range(sl+1,sl+1+sunday_lines*2,2):
    sun[tan[i]]=int(tan[i+1])

#print sun

def a_search(graph,start,dest):

    unexplored = [] #UNEXPLORED LIST
    unexplored.append(start) #INITIALIZE UNEXPLORED LIST
        
    fromset = {} #FOR PATH
    visited = [] #VISITED
    
    g = {} #GSCORES
    g[start] = 0 #INITIALIZE G
    
    f = {} #FSCORES
    f[start] = g[start] + sundayDistance(start,dest) #INITIALIZE F
    
    while unexplored:
        front = least(unexplored,f)
        if front == dest:
                node = dest    
                path = deque()
                path.appendleft(node)
                while node in fromset:
                        node = fromset[node]
                        path.appendleft(node)
                return path

        unexplored.remove(front)
        visited.append(front)
        if adjacentVertices(graph,front) is not None:
            for adj in adjacentVertices(graph,front):
                g1 = g[front] + distance(graph,front,adj)
                if adj in visited:
                        if g1 >= g[adj]:
                            continue
                elif adj not in visited:
                        if(adj in unexplored)== False:
                            unexplored.append(adj)
                        fromset[adj] = front
                        g[adj] = g1
                        f[adj] = g[adj] + sundayDistance(adj,dest)
                        
                elif g1 < g[adj]:
                        if(adj in unexplored)== False:
                            unexplored.append(adj)
                        fromset[adj] = front
                        g[adj] = g1
                        f[adj] = g[adj] + sundayDistance(adj,dest)
        else:
            pass
    return 0

def fill_graph_a():
	for v in range(4,ll+4,3):
		if tan[v] not in graph1:
			graph1[tan[v]]=[tan[v+1],tan[v+2]]
		elif tan[v] in graph1:
			graph1[tan[v]] = graph1.get(tan[v], ()) + [tan[v+1],tan[v+2]]

def fill_graph_d():
	for v in range(4,ll+4,3):
		if(graph1.has_key(tan[v])==False):
			graph1[tan[v]]=[tan[v+1]]
		elif(graph1.has_key(tan[v])==True):
			graph1[tan[v]] = graph1.get(tan[v], ()) + [tan[v+1]]
	for node in graph1.keys():
	    for node1 in graph1[node]:
	        if not graph1.has_key(node1):
	            graph1[node1]=[node1]

def fill_graph_u():
	for v in range(4,ll+4,3):
		if tan[v] not in graph1:
			graph1[tan[v]]=[tan[v+1],tan[v+2]]
		elif tan[v] in graph1:
			graph1[tan[v]] = graph1.get(tan[v], ()) + [tan[v+1],tan[v+2]]

def fill_graph_b():
	for v in range(4,ll+4,3):
		if(graph1.has_key(tan[v])==False):
			graph1[tan[v]]=[tan[v+1]]
		elif(graph1.has_key(tan[v])==True):
			graph1[tan[v]] = graph1.get(tan[v], ()) + [tan[v+1]]

def dfs_recursive(graph, explorer, dest, done):
    if explorer == dest:
        return [explorer]
    if explorer in graph:
        for side in graph[explorer]:
            if side not in done:
                done.append(side)
                move = dfs_recursive(graph, side, dest, done)
                if move:
                      move.insert(0, explorer)
                      return move


def readGraph_u():
    graph = OrderedDict()
    for x in graph1:
        line = ''.join(x)
        for y in graph1[x]:
            line=line+" "
            y=''.join(y)
            line=line+y
            print line
            tokens = line.split()
            node = tokens[0]
            print node
            graph[node] = OrderedDict()
            for i in range(1, len(tokens) - 1, 2):
                graph[node][tokens[i]] = int(tokens[i + 1])
    graph[dest]={}
    graph[dest][dest]=0
    return graph

def search_u(u_list, graph, start, dest):
    while u_list:
        node = u_list.get() #NODE[1] HAS LIST PATH, NODE[0] HAS DISTANCE TRAVELED
        print node
        current = node[1][len(node[1]) - 1] #CURRENTLY EXPANDED NODE
        print current
        if dest in node[1]: #IF dest FOUND IN PATH, RETURN PATH
            print node[1]
            return node[1]
            break
        if current in graph: #CHECK IF CURRENT NODE HAS NEIGHBORS
            cost = node[0]
            print cost
            list1=list(graph[current]) #REVERSES THE ADJ LIST
            list1.reverse()            #FOR CORRECT PATH
            for adj in list1:
                temp = node[1][:] #TAKES ENTIRE PATH(I.E. NODE[1]) INTO TEMP
                temp.append(adj) #ADDS NEIGBOR TO PATH
                u_list.put((cost + graph[current][adj], temp)) #ADDS NEW COST AND PATH TO QUEUE

def bfs(frontier, graph, start, dest):
        while frontier:
                path = frontier.pop(0)
                node = path[-1] #LAST ELEMENT OF PATH IS NODE
                print node
                if node == dest:
                        print path
                        return path
                for side in graph.get(node, []):
                        appended_path = list(path)
                        appended_path.append(side)
                        frontier.append(appended_path)

def distance(graph, current,adj):
    list1=graph[current]
    if adj in list1:
        return int(list1[adj])
    else:
        return 999999

def sundayDistance(start,dest):
    return int(sun[start])

def adjacentVertices(graph,current):
    if current in graph:
        list1=graph[current]
        return list1
    else:
        return None
    
def make_path(previouslyVisited,dest):
    node = dest    
    path = deque()
    
    path.appendleft(node)
    while node in previouslyVisited:
        node = previouslyVisited[node]
        path.appendleft(node)
    return path
    
def least(open,f):
    leastNode = None
    least = float("inf")
    
    for node in open:
        if f[node] < least:
            least = f[node]
            leastNode = node
    return leastNode



algo=str(algo)
if algo=="DFS":
	fill_graph_d()
	visited=list()
	visited.append(start)
	path = dfs_recursive(graph1, start, dest, visited)
	#path=dfs_path(graph1,start,dest)
	print path
	output = open("output.txt","w")
	for i in range(0,len(path)):
		output.write(path[i]+" "+str(i)+"\n")

if algo=="A*":
	fill_graph_a()
	graph = readGraph_u()
	path = a_search(graph, start, dest)
	print path
	cost=0
	outfile=open('output.txt','w')
	outfile.write(path[0]+' '+str(cost))
	#print graph
	for i in range(1,len(path)):
		cost=cost+int(graph[path[i-1]][path[i]])
		outfile.write('\n')
		outfile.write(path[i]+' '+str(cost))

if algo=="UCS":
	u_list = Q.PriorityQueue()
	u_list.put((0, [start]))
	fill_graph_u()
	graph = readGraph_u()
	path = search_u(u_list,graph, start, dest)
	outfile=open('output.txt','w')
	cost=0
	outfile.write(path[0]+' '+str(cost))
	for i in range(1,len(path)):
		cost=cost+int(graph[path[i-1]][path[i]])
		outfile.write('\n')
		outfile.write(path[i]+' '+str(cost))
		
if algo=="BFS":
	frontier = []
	frontier.append([start])
	fill_graph_b()
	path = bfs(frontier, graph1, start, dest)
	output = open("output.txt","w")
	for i in range(0,len(path)):
		output.write(path[i]+" "+str(i)+"\n")
