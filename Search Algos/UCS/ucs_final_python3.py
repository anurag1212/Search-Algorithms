from collections import OrderedDict

words=[]

for line in open('input.txt'):
	words.extend(line.split())

#print (words)

algo=words[0]
start=words[1]
goal=words[2]
live_lines=int(words[3])
ll=live_lines*3
graph1={}

def search(graph, start, end):
    if start not in graph:
        raise TypeError(str(start) + ' not found in graph !')
        return
    if end not in graph:
        raise TypeError(str(end) + ' not found in graph !')
        return
    #queue = Q.PriorityQueue()
    queue = list()
    queue.append((0, [start]))
    while queue:
        node = queue.pop()
        current = node[1][len(node[1]) - 1]
        if end in node[1]:
            #print("Path found: " + str(node[1]) + ", Cost = " + str(node[0]))
            return node[1]
            break
        if current in graph:
            cost = node[0]
            #print current,'-',graph[current]
            
            list1=list(graph[current])
            list1.reverse()
            for neighbor in list1:
                temp = node[1][:]
                temp.append(neighbor)
                queue.append((cost + graph[current][neighbor], temp))
        
def fill_graph():
	for v in range(4,ll+4,3):
		if words[v] not in graph1:
			graph1[words[v]]=[words[v+1],words[v+2]]
		elif words[v] in graph1:
			graph1[words[v]] = graph1.get(words[v], ()) + [words[v+1],words[v+2]]

def readGraph():
    graph = OrderedDict()
    for x in graph1:
        line = ''.join(x)
        for y in graph1[x]:
            line=line+" "
            y=''.join(y)
            line=line+y
            #print line
            tokens = line.split()
            node = tokens[0]
            graph[node] = OrderedDict()
        
            for i in range(1, len(tokens) - 1, 2):
                # print(node, tokens[i], tokens[i + 1])
                # graph.addEdge(node, tokens[i], int(tokens[i + 1]))
                graph[node][tokens[i]] = int(tokens[i + 1])
    graph[goal]={}
    graph[goal][goal]=0
    return graph

def main():
    fill_graph()
    graph = readGraph()
    path = search(graph, start, goal)
    outfile=open('ou1.txt','w')
    cost=0
    print(path[0]+' '+str(cost))
    for i in range(1,len(path)):
        cost=cost+int(graph[path[i-1]][path[i]])
        #print('\n')
        print(path[i]+' '+str(cost))

if __name__ == "__main__":
    main()