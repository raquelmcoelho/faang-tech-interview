'''
https://www.educative.io/courses/grokking-coding-interview-patterns-python/q2jRXVoA2G3
Solution: Redundant Connection

We’re given a graph that is actually a tree with n nodes labeled from 1 to n, plus one additional edge. The additional edge connects two different vertices and is not a duplicate of an existing edge.

The graph is represented as an array called edges of length n where edges[i] = [a, b] indicates that there is an edge between nodes a and b in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple candidates for removal, return the edge that occurs last in edges.

Time complexity
The time complexity for the solution is O(n) where n is the number of vertices (and also the number of edges).

Space Complexity
The space complexity is O(n) where n is the number of vertices.

'''

class UnionFind:

    def __init__(self, n):
        self.parent = []
        self.rank = rank = [1] * (n + 1)
        for i in range(n + 1):
            self.parent.append(i)

    def find_parent(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find_parent(self.parent[x])
        return self.parent[x]

    # returns false if both vertices have the same parent, otherwise, updates the parent and rank lists by making a connection based on the passed edge
    # true will be returned if no cycle exits in the graph
    def union(self, v1, v2):
        print("\n\tChecking if the vertices have the same parent")
        print("\t\tEdge: [", v1, ", ", v2, "]", sep = "")
        print("\t\tFirst vertex: ", v1, sep = "")
        print("\t\tSecond vertex: ", v2, sep = "")
        #finds the root parents of both v1 and v2
        p1, p2 = self.find_parent(v1), self.find_parent(v2)
        print("\t\t\tParent of the first vertex: ", p1, sep = "")
        print("\t\t\tParent of the second vertex: ", p2, sep = "")
        #if both parents are the same, a cycle exists and v1,v2 is the redundant edge
        if p1 == p2:
            print("\t\tSince both vertices have the same parent, this is a redundant edge")
            return False
        #updates the parent and rank lists otherwise 
        elif self.rank[p1] > self.rank[p2]:
            print("\t\tThe vertices don't have the same parent, updating parent and rank lists")
            print("\t\t\tParent list: ", self.parent, " ⟶ ", sep = "", end = "")
            self.parent[p2] = p1
            print(self.parent)
            print("\t\t\tRank list: ", self.rank, " ⟶ ", sep = "", end = "")
            self.rank[p1] = self.rank[p1] + self.rank[p2]
            print(self.rank)
        else:
            print("\t\tThe vertices don't have the same parent, updating parent and rank lists")
            print("\t\t\tParent list: ", self.parent, " ⟶ ", sep = "", end = "")
            self.parent[p1] = p2
            print(self.parent)
            print("\t\t\tRank list: ", self.rank, " ⟶ ", sep = "", end = "")
            self.rank[p2] = self.rank[p2] + self.rank[p1]
            print(self.rank)
        
        return True

def redundant_connection(edges):
	
	print("\tDeclaring the parent and rank lists")
	#declares the parent and rank list with lengths based on the edges list
	graph = UnionFind(len(edges))
	print("\t\tParent: ", graph.parent, sep = "")
	print("\t\tRank: ", graph.rank, sep = "")
	
	# traverses the edges of the graph to check for the redundant edge
	for v1, v2 in edges:
		if not graph.union(v1, v2):
			return [v1, v2]

def main():
	edges = [
		[[1, 2], [1, 3], [2, 3]], 
		[[1, 2], [2, 3], [1, 3]], 
		[[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]], 
		[[1, 2], [1, 3], [1, 4], [3, 4], [2, 4]], 
		[[1, 2], [1, 3], [1, 4], [1,5], [2, 3], [2, 4], [2, 5]]
	]

	for i in range(len(edges)):
		print(i+1, ".\tEdges: ", edges[i], sep = "")
		print("\n\tThe redundant connection in the graph is: ", redundant_connection(edges[i]), sep = "")
		print("-" * 100)

if __name__ == '__main__':
	main()
