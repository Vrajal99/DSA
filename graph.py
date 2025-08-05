from collections import defaultdict, deque

graph=defaultdict(list)

def addEdge(graph,u,v):
    graph[u].append(v)
    graph[v].append(u)

def generate_edges(graph):
    edges=[]
    for node in graph:

        for neigbour in graph[node]:
            edges.append((node, neigbour))
    return edges


addEdge(graph,'a','c')
addEdge(graph,'b','c')
addEdge(graph,'b','e')
addEdge(graph,'c','d')
addEdge(graph,'c','e')
addEdge(graph,'d','c')


print(generate_edges(graph))



def bfs(graph, V,start):
    vis={node:False for node in graph}
    q=deque()
    result=[]

    q.append(start)
    vis[start]=True

    while q:
        curr = q.popleft()
        result.append(curr)

        for neigh in graph[curr]:
            if vis[neigh] ==False:
                q.append(neigh)
                vis[neigh]=True
    return result

def dfs(node,graph,vis,res):

    vis[node]=True
    res.append(node)

    for neighbour in graph[node]:
        if not vis[neighbour]:
            dfs(neighbour,graph,vis,res)

    pass

def dfs_of_graph(graph,start):

    vis={node:False for node in graph}
    res=[]

    vis[start]=True
    dfs(start,graph,vis,res)
    return res

graph1=defaultdict(list)

addEdge(graph1,1,2)
addEdge(graph1,1,3)
addEdge(graph1,2,5)
addEdge(graph1,2,6)
addEdge(graph1,3,4)
addEdge(graph1,3,7)
addEdge(graph1,4,8)
addEdge(graph1,7,8)

print(dfs_of_graph(graph1,1))