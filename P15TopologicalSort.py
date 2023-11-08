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
    for x in dependencies:
        parent, child = x[1], x[0]
        graph[parent], graph[child] = [], []
        inDegree[parent], inDegree[child] = 0, 0
    if len(graph) <= 0:
        return sorted_order

    # b. Build the graph
    k = 0
    for dependency in dependencies:
        k += 1
        parent, child = dependency[1], dependency[0]
        graph[parent].append(child)  # put the child into it's parent's list
        inDegree[child] += 1  # increment child's inDegree

    # c. Find all sources i.e., all n with 0 in-degrees
    sources = deque()
    l = 0
    for key in inDegree:
        l += 1
        if inDegree[key] == 0:
            sources.append(key)
        else:
            print("\t\t\tIn-degree of ", key, " is ", inDegree[key], " hence it's not a source", sep = "")

    # d. For each source, add it to the sorted_order and subtract one from all of its children's in-degrees
    # if a child's in-degree becomes zero, add it to the sources queue
    m = 0
    while sources:
        m += 1
        vertex = sources.popleft()
        sorted_order.append(vertex)
        n = 0
        for child in graph[vertex]:  # get the node's children to decrement their in-degrees
            n += 1
            inDegree[child] -= 1
            if inDegree[child] == 0:
                sources.append(child)

    # topological sort is not possible as the graph has a cycle
    if len(sorted_order) != len(graph):
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
