'''
https://www.educative.io/courses/grokking-coding-interview-patterns-python/RMkpmAllP9L
Solution: Find Maximum in Sliding Window

Given an integer array nums and a window of size w, find the current maximum value in the window as it slides through the entire array.

Note: If the window size is greater than the array size, we consider the entire array as a single window.

Time complexity
Hence, the overall time complexity of the solution, irrespective of the input, is 
O(w+n)

Space complexity
The space complexity of this solution is O(w), where w is the size of the input list.
'''

# Importing doubly ended queue
from collections import deque

def find_max_sliding_window(nums, window_size):
    result = []
    # Initializing doubly ended queue for storing indices
    window = deque()

    # Let’s now return an empty list if nums is empty
    if len(nums) == 0:
        return result

    # If window_size is greater than the array size,
    # set the window_size to nums.size()
    if window_size > len(nums):
        window_size = len(nums)
    
    # this variable is for the sole purpose of printing
    check = False

    # Find out first maximum in the first window
    print("Traversing to find maximum in the first window:")
    for i in range(window_size):
        # For every element, remove the previous smaller elements from window
        while window and nums[i] >= nums[window[-1]]:
            check = True
            print(f"\t\tnums[{i}] = {nums[i]} is greater than or equal to nums[window[-1]] = {nums[window[-1]]}")
            print("\t\tWindow before popping:", window)
            window.pop()
            print("\t\tWindow after popping:", window)

        # this is only for the purpose of printing
        if not check:
            if window:
                print(f"\t\tnums[{i}] = {nums[i]} is less than nums[window[-1]] = {nums[window[-1]]}")
            else:
                print(f"\t\tThe window is empty.")
        check = False

        # Add current element at the back of the queue
        # print(f"\tAppending {i} to the window deque")
        window.append(i)

    # Appending the largest element in the window to the result
    result.append(nums[window[0]])

    print("Traversing to find maximum in remaining windows:")
    for i in range(window_size, len(nums)):
        # remove all numbers that are smaller than current number
        # from the tail of list
        while window and nums[i] >= nums[window[-1]]:
            check = True
            print(f"\t\tnums[{i}] = {nums[i]} is greater than or equal to nums[window[-1]] = {nums[window[-1]]}")
            window.pop()
            print("\t\tWindow after popping:", window)
        
        # this is only for the purpose of printing
        if not check:
            if window:
                print(f"\t\tnums[{i}] = {nums[i]} is less than nums[window[-1]] = {nums[window[-1]]}")
            else:
                print(f"\t\tThe window is empty.")
        check = False

        # Remove first index from the window deque if
        # it doesn't fall in the current window anymore
        if window and window[0] <= (i - window_size):
            window.popleft()

        # Add current element at the back of the queue
        # print(f"\tAppending {i} to the window deque")
        window.append(i)
        result.append(nums[window[0]])

    return result


def main():
    target_list = [3, 3, 3, 3, 2, 4, 3, 2, 3, 18]
    nums_list = [
      [1, 5, 8, 15, 19, 19, 19, 17, 14, 13, 12, 12, 12, 14],
      '''
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                 [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
                 [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
                 [1, 5, 8, 10, 10, 10, 12, 14, 15, 19, 19, 19, 17, 14, 13, 12, 12, 12, 14, 18, 22, 26, 26, 26, 28, 29, 30],
                 [10, 6, 9, -3, 23, -1, 34, 56, 67, -1, -4, -8, -2, 9, 10, 34, 67],
                 [4, 5, 6, 1, 2, 3],
                 [9, 5, 3, 1, 6, 3],
                 [2, 4, 6, 8, 10, 12, 14, 16],
                 [-1, -1, -2, -4, -6, -7],
                 [4, 4, 4, 4, 4, 4]
                 '''
                 ]

    for i in range(len(nums_list)):
        print(i + 1, ". Original array:\t", nums_list[i], sep="")
        print("Window size:\t\t", target_list[i])
        print("\n Max:\t\t",
              find_max_sliding_window(nums_list[i], target_list[i]))
        print("-"*100)


if __name__ == '__main__':
    main()