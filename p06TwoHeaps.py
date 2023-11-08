'''
https://www.educative.io/courses/grokking-coding-interview-patterns-python/3jmBWVEznrR
Solution: Maximize Capital

You need to develop a program for making automatic investment decisions for a busy investor. The investor has some start-up capital, c, to invest and a portfolio of projects in which they would like to invest in. The investor wants to maximize their cumulative capital as a result of this investment.

To help them with their decision, they have information on the capital requirement for each project and the profit it’s expected to yield. As a basic risk-mitigation measure, the investor would like to set a limit on the number of projects, k, they invest in. For example, if the value of k is 2, then find the two projects that respect their capital requirements and yield maximum profits. For example, if a project has a capital requirement of 3, and our current capital is 1, then the investor can’t invest in that project.

Time complexity
The time complexity to push the required capital values on to the min-heap is O(nlogn), where n represents the number of projects. The time complexity to select the projects with the maximum profits from the heaps is O(k logn), where k represents the number of selected projects. So, the total time complexity becomes O(n logn + k logn), that is, O((n+k)logn).

Space complexity
We are using two heaps, one to store capital requirements and one to store profits. In the worst case, where we meet the capital requirements of all the projects right from the start, we populate both heaps with n elements each. Hence, the space complexity of this solution is O(n).
'''

from heapq import heappush, heappop

def maximum_capital(c, k, capitals, profits):

    current_capital = c
    capitals_min_heap = []
    profits_max_heap = []

    # Insert all capitals values to a min-heap
    for x in range(0, len(capitals)):
        heappush(capitals_min_heap, (capitals[x], x))

    # Calculate capital of all the required number of projects
    # containing maximum profit
    for _ in range(k):

        # Select projects (in the range of the current capital)
        # then push them onto the max-heap
        while capitals_min_heap and capitals_min_heap[0][0] <= current_capital:
            c, i = heappop(capitals_min_heap)
            heappush(profits_max_heap, (-profits[i], i))
        
        # check if the max-hap is empty
        if not profits_max_heap:
            break

        # Select those projects from the max-heap that contain the maximum profit
        j = -heappop(profits_max_heap)[0]
        print(f"\t\tUpdated capital = {current_capital} + {j}")
        current_capital = current_capital + j

    return current_capital


def main():
    input = (
              (1, 2, [1, 2, 2, 3], [2, 4, 6, 8]),
              (2, 3, [1, 3, 4, 5, 6], [1, 2, 3, 4, 5]),
              (1, 3, [1, 2, 3, 4], [1, 3, 5, 7]),
              (7, 2, [6, 7, 8, 10], [4, 8, 12, 14]),
              (2, 4, [2, 3, 5, 6, 8, 12], [1, 2, 5, 6, 8, 9])
            )
    num = 1
    for i in input:
        print(f"{num}.\tProject capital requirements:  {i[2]}")
        print(f"\tProject expected profits:      {i[3]}")
        print(f"\tNumber of projects:            {i[1]}")
        print(f"\tStart-up capital:              {i[0]}")
        print("\n\t\tProcessing: ")
        print("\n\tMaximum capital earned: ",
              maximum_capital(i[0], i[1], i[2], i[3]))
        print("-" * 100, "\n")
        num += 1


if __name__ == "__main__":
    main()
          
 
 
