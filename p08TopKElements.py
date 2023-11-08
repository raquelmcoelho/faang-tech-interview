'''
https://www.educative.io/courses/grokking-coding-interview-patterns-python/xoW1VrXA3mJ
Solution: Kth Largest Element in a Stream

Given an infinite stream of integers, nums, design a class to find the k^{th} largest element in a stream.

Note: It is the k^{th} largest element in the sorted order, not the k^{th} distinct element.

The class should have the following functions, inputs, and return values:

Init(): It takes an array of integers and an integer k and initializes the class object.
Add(value): It takes one integer value, appends it to the stream, and calls the Return kth largest() function.
Return kth largest(): It returns an integer value that represents the k^{th} largest element in the stream.

Time complexity
The time complexity of this solution is O(nlog(n)+mlog(k)), where k is the size of the Heap, n is the length of the input stream, and m is the number of calls to the function add.

Space complexity
The space complexity of this solution is O(k).
'''

import heapq


def print_heap_with_markers(arr, pValue):
    out = "["
    for i in range(len(arr)):
        if pValue == i:
            out += '«'
            out += str(arr[i]) + '»' + ", "
        else:
            out += str(arr[i]) + ", "
    out = out[0:len(out) - 2]
    out += "]"
    return out


class KthLargest:
    # constructor to initialize heap and add values in it
    def __init__(self, k, nums):
        print("\tInitializing the heap")
        self.k = k
        self.top_k_heap = nums
        heapq.heapify(self.top_k_heap)
        print("\t\tk = ", self.k)
        print("\t\tHeap: ", self.top_k_heap)
        while len(self.top_k_heap) > k:
            print("\t\tLength of the heap = ", len(self.top_k_heap), ", which is greater than k = ", k, sep = "")
            print("\t\t\tPopping from the heap: ", self.top_k_heap, " ⟶ ", end = "")
            heapq.heappop(self.top_k_heap)
            print(self.top_k_heap)

    # adds element in the heap
    def add(self, val):
        print("\t\tAdding ", val, " to the heap: ", self.top_k_heap, " ⟶ ", end = "", sep = "")
        heapq.heappush(self.top_k_heap, val)
        print(self.top_k_heap)
        if len(self.top_k_heap) > self.k:
            print("\t\tHeap size = ", len(self.top_k_heap), sep = "")
            print("\t\tk = ", self.k, sep = "")
            print("\t\tSince heap size > k, popping from the heap: ", print_heap_with_markers(self.top_k_heap, 0), " ⟶ ", end = "", sep = "")
            heapq.heappop(self.top_k_heap)
            print(self.top_k_heap, "\n", sep = "")
        return self.return_Kth_largest()

    # returns kth largest element from heap
    def return_Kth_largest(self):
        print("\tHeap: ", print_heap_with_markers(self.top_k_heap, 0))
        return self.top_k_heap[0]


def main():
    nums = [3, 6, 9, 10]
    temp = [3, 6, 9, 10]
    print("Initial stream: ", nums, sep = "")
    KLargest = KthLargest(3, nums)
    val = [4, 7, 10, 8, 15]
    print()
    for i in range(len(val)):
        print("\tAdding a new number ", val[i], " to the stream", sep = "")
        temp.append(val[i])
        print("\t\tNumber stream: ", temp, sep = "")
        print("\tKth largest element in the stream: ", KLargest.add(val[i]))
        print("-"*100)


if __name__ == "__main__":
    main()
