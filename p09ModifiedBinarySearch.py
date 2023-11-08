'''
https://www.educative.io/courses/grokking-coding-interview-patterns-python/qVnp1mWMl1D
Solution: Search in Rotated Sorted Array

Given a sorted integer array, nums, and an integer value, target, the array is rotated by some arbitrary number. Search and return the index of target in this array. If the target does not exist, return -1.

Time complexity
The time complexity of both approaches is O(log(n)) since we divide the array into two halves at each step.

Space complexity
The space complexity of the iterative solution is O(1) since no new data structure is being created.
The space complexity of the recursive solution is O(logn), where n is the number of elements present in the array and logn is the maximum number of recursive calls needed to find the target.
'''

def binary_search(nums, low, high, target):

    if (low > high):
        return -1

    # Finding the mid using integer division
    mid = low + (high - low) // 2

    if nums[mid] == target:
        return mid

    # low to mid is sorted
    if nums[low] <= nums[mid]:
        if nums[low] <= target and target < nums[mid]:
            # target is within the sorted first half of the array
            return binary_search(nums, low, mid-1, target)
        else:
            # target is not within the sorted first half, so let’s examine the unsorted second half
            return binary_search(nums, mid+1, high, target)
    # mid to high is sorted
    else:
        if nums[mid] < target and target <= nums[high]:
            # target is within the sorted second half of the array
            return binary_search(nums, mid+1, high, target)
        else:
            # target is not within the sorted second half, so let’s examine the unsorted first half
            return binary_search(nums, low, mid-1, target)


def binary_search_rotated(nums, target):
    return binary_search(nums, 0, len(nums)-1, target)


def main():
    target_list = [3, 6, 3, 6]
    nums_list = [[6, 7, 1, 2, 3, 4, 5], [6, 7, 1, 2, 3, 4, 5],
                 [4, 5, 6, 1, 2, 3], [4, 5, 6, 1, 2, 3]]

    for i in range(len(target_list)):
        print((i + 1), ".\tRotated array: ", nums_list[i], "\n\ttarget", target_list[i], "found at index ", \
              binary_search_rotated(nums_list[i], target_list[i]))
        print("-" * 100)


if __name__ == '__main__':
    main()
