'''
https://www.educative.io/courses/grokking-coding-interview-patterns-python/qVENW88509y
Solution: Compilation Order

There are a total of n classes labeled with the English alphabet (A, B, C, and so on). Some classes are dependent on other classes for compilation. For example, if class B extends class A, then B has a dependency on A. Therefore, A must be compiled before B.

Given a list of the dependency pairs, find the order in which the classes should be compiled.

Time complexity
The time complexity of the above algorithm is O(V+E), where V is the total number of vertices and E is the total number of edges in the graph.

Space complexity
The space complexity is O(V) since we are creating a deque data structure that will have O(V) elements in the worst case. We are also maintaining a hash table with the in-degree of the vertices. Its size is O(V) as well.
'''

from collections import deque


def find_compilation_order(dependencies):
    sorted_order = []
    # a. Initialize the graph and inDegree
    graph = {}
    inDegree = {}
    print("\tInitializing the graph and inDegree")
    for x in dependencies:
        parent, child = x[1], x[0]
        graph[parent], graph[child] = [], []
        inDegree[parent], inDegree[child] = 0, 0
    print("\t\tGraph: ", graph, sep = "")
    print("\t\tinDegree: ", inDegree, "\n", sep = "")
    if len(graph) <= 0:
        print("\tThere are no vertices")
        print("\t\tReturning the sorted order: ", sorted_order, sep = "")
        return sorted_order

    print("\tBuilding the graph and populating inDegree")
    # b. Build the graph
    k = 0
    for dependency in dependencies:
        print("\t\tLoop index: ", k, sep = "")
        k += 1
        parent, child = dependency[1], dependency[0]
        graph[parent].append(child)  # put the child into it's parent's list
        inDegree[child] += 1  # increment child's inDegree
        print("\t\t\tDependency pair: ", dependency, " ⟶ parent: ", parent, ", child: ", child, sep = "")
        print("\t\t\tAppending the child to the parent's list in the graph:")
        print("\t\t\t\tGraph: ", graph, sep = "")
        print("\t\t\tIncrementing indegree of the child ⟶ ", inDegree)
    print()

    # c. Find all sources i.e., all n with 0 in-degrees
    print("\n\tFinding all sources")
    sources = deque()
    l = 0
    for key in inDegree:
        print("\t\tLoop index: ", l, sep = "")
        l += 1
        if inDegree[key] == 0:
            sources.append(key)
            print("\t\t\tIn-degree of ", key, " is 0, hence it's a source", sep = "")
            print("\t\t\tSources: ", sources, sep = "")
        else:
            print("\t\t\tIn-degree of ", key, " is ", inDegree[key], " hence it's not a source", sep = "")
    print()

    # d. For each source, add it to the sorted_order and subtract one from all of its children's in-degrees
    # if a child's in-degree becomes zero, add it to the sources queue
    print("\n\tRemoving the sources from the graph")
    m = 0
    while sources:
        print("\t\tLoop index: ", m, sep = "")
        m += 1
        print("\t\tGetting the source by popping from the queue")
        print("\t\t\tSources: ", sources, " ⟶ ", end = "", sep = "")
        vertex = sources.popleft()
        print(sources)
        print("\t\t\tVertex: ", vertex)
        print("\t\t\tAppending to the sorted order list: ", sorted_order, " ⟶ ", end = "", sep = "")
        sorted_order.append(vertex)
        print(sorted_order)
        print("\t\t\tUpdating the in-degrees of the children")
        print("\t\t\t\tSource: ", vertex, ", children: ", graph[vertex], sep = "")
        n = 0
        for child in graph[vertex]:  # get the node's children to decrement their in-degrees
            print("\t\t\t\tInner loop index: ", n)
            n += 1
            print("\t\t\t\t\tChild: ", child, sep = "")
            print("\t\t\t\t\tDecrementing in-degree of ", child, ": ", inDegree[child], " ⟶ ", inDegree[child] - 1, sep = "")
            inDegree[child] -= 1
            if inDegree[child] == 0:
                print("\t\t\t\t\tSince in-degree of ", child, " = 0, it's now a source.", sep = "")
                print("\t\t\t\t\tAdding it to the sources queue: ", sources, " ⟶ ", end = "", sep = "")
                sources.append(child)
                print(sources)

    # topological sort is not possible as the graph has a cycle
    if len(sorted_order) != len(graph):
        print("\n\tLength of the sorted order list = ", len(sorted_order), sep = "")
        print("\tLength of the graph = ", len(graph), sep = "")
        print("\t\tSince the lengths are not equal, there's a cycle in the graph.")
        return []
    return sorted_order


# Driver code
def main():
    dependencies = [[['B', 'A'], ['C', 'A'], ['D', 'C'], ['E', 'D'], ['E', 'B']],
        [['B', 'A'], ['C', 'A'], ['D', 'B'], ['E', 'B'], ['E', 'D'], ['E', 'C'], ['F', 'D'], ['F', 'E'], ['F', 'C']],
        [['A', 'B'], ['B', 'A']],
        [['B', 'C'], ['C', 'A'], ['A', 'F']],
        [['C', 'C']]]
    for i in range(len(dependencies)):
        print(i + 1, ".\tdependencies: ", dependencies[i], sep = "")
        print("\tCompilation Order: ", find_compilation_order(dependencies[i]), sep = "")
        print("-"*100, "\n", sep ="")


if __name__ == "__main__":
    main()
