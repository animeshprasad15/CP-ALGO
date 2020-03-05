# representing using adjacency list 

from collections import defaultdict
class graph(object):
	"""docstring for graph"""
	def __init__(self):
		self.adjl = defaultdict(list)

	def addedge(self,u,v): self.adjl[u].append(v) 

def dfs(graph, source, vis):
	gr = graph.adjl
	vis[source] = 1 
	print(source)
	for v in gr[source]:
		if not vis[v]:
			dfs(graph, v, vis)

def dfs_(graph, source):
	vis = [0]*len(graph.adjl)
	dfs(graph, source, vis)

g = graph()
g.addedge(0,1)
g.addedge(0,2)
g.addedge(1,2)
g.addedge(2,0)
g.addedge(2,3)
g.addedge(3,3)

dfs_(g,2)