'''
https://www.educative.io/courses/grokking-coding-interview-patterns-python/gxWjRVqvQEj
Solution: Merge Sorted Array

Given two sorted integer arrays, nums1
nums1 and nums2, and the number of data elements in each array, m
m and n, implement a function that merges the second array into the first one. You have to modify nums1 in place.

Note: Assume that nums1 has a size equal to m + n, meaning it has enough space to hold additional elements from nums2.

Time complexity
The time complexity is O(n+m), where n and m are the counts of initialized elements in the two arrays.

Space complexity
The space complexity is O(1) because we only use the space required for three indices.

'''

def print_array_with_markers(arr, pValue):
    out = "["
    for i in range(len(arr)):
        if i in pValue:
            out += '«'
            out += str(arr[i]) + '»' + ", "
        else:
            out += str(arr[i]) + ", "
    out = out[0:len(out) - 2]
    out += "]"
    return out


def merge_sorted(nums1, m, nums2, n):
    p1 = m - 1  # set p1 to the last initialized element of nums1
    p2 = n - 1  # set p2 to the last element of nums2
    # if traversal of nums2 is complete, break out of the loop
    # traverse backwards over the nums1 array
    x = 0
    for p in range(n + m - 1, -1, -1):
        if p2 < 0:
            break
        x += 1
        # if p1 is not on the first element and the nums1 element is greater than nums2 element
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            # move the p1 pointer one element back
            p1 -= 1
        else:
            # set the nums1 element at index p = nums2 element at index p2
            nums1[p] = nums2[p2]
            # move the p2 pointer one element back
            p2 -= 1
    return nums1


# Driver code
def main():
    m = [9, 2, 3, 1, 8]
    n = [6, 1, 4, 2, 1]
    nums1 = [[23, 33, 35, 41, 44, 47, 56, 91, 105, 0, 0, 0, 0, 0, 0], [1, 2, 0], [1, 1, 1, 0, 0, 0, 0], [6, 0, 0], [12, 34, 45, 56, 67, 78, 89, 99, 0]]
    nums2 = [[32, 49, 50, 51, 61, 99], [7], [1, 2, 3, 4], [-99, -45], [100]]
    k = 1
    for i in range(len(m)):
        print(k, ".\tnums1: ", nums1[i], ", m: ", m[i], sep = "")
        print("\tnums2: ", nums2[i], ", n: ", n[i], sep = "")
        print("\n\tMerged list: ", merge_sorted(nums1[i], m[i], nums2[i], n[i]), sep = "")
        print("-"*100, "\n")
        k += 1


if __name__ == "__main__":
    main()
