'''
https://www.educative.io/courses/grokking-coding-interview-patterns-python/YQN5MzGrp50
Solution: Missing Number

Given an array, nums, containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Time complexity
The time complexity of the above algorithm is O(n), where n is the number of elements in the input array.

Space complexity
The algorithm runs in constant space O(1).
'''

def print_array_with_markers(arr, iValue):
    out = "["
    for i in range(len(arr)):
        if i in iValue:
            out+='«'
            out+=str(arr[i]) + '»' + ", "
        else:
            out+=str(arr[i]) + ", "
    out = out[0:len(out) - 2]
    out += "]"
    return out

def find_missing_number(nums):
  len_nums = len(nums)
  index = 0
  ind = 0
  print("\n\tSorting the array")
  while index < len_nums:
    print("\t\tLoop iteration ", ind, ":", sep = "")
    ind+=1
    print("\t\t\t", print_array_with_markers(nums, [index]), sep = "")
    value = nums[index]
    print("\t\t\tindex = ", index, sep = "")
    print("\t\t\tvalue = ", value, sep = "")
    # check if value is at the incorrect position
    if value < len_nums and value != nums[value]:
      print("\t\t\tSwapping the value: ", value, " with the value on index ", value, ": ", nums[value], sep = "")
      print("\t\t\t\t", print_array_with_markers(nums, [index, value]), sep = "")
      # swap the value with its correct index
      nums[index], nums[value] = nums[value], nums[index]
      print("\t\t\t\tAfter swapping: ", print_array_with_markers(nums, [index, value]), sep = "")
    elif value >= len_nums:
      print("\t\t\tvalue > length of array, hence we skip it", sep = "")
      # move to the next loop
      index+=1
    else:
      # if the element is at the correct index, move one element forward
      print("\t\t\tThe value is at its correct index, hence we move one step forward", sep = "")
      # move to the next loop
      index += 1

  print("\n\tFinding the missing number")
  # find the first number missing from its index
  for x in range(len_nums):
    print("\t\tLoop iteration ", x, sep = "")
    print("\t\t\t", print_array_with_markers(nums, [x]), sep = "")
    if x != nums[x]:
      # index for the mismatched pair is the missing number
      print("\t\t\t", nums[x], " is not at the correct index: ", x, sep = "")
      return x
    print("\t\t\t", nums[x], " is at the correct index: ", x, sep = "")
  return len_nums

def main():
  inputnumbers = [[4, 0, 3, 1], 
    [8, 3, 5, 2, 4, 6, 0, 1], 
    [1, 2, 3, 4, 6, 7, 8, 9, 10, 11], 
    [0], 
    [1, 2, 3, 0, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23]
  ]
  i = 1
  for x in inputnumbers:
    print(i, ".\tnums: ", x, sep = "")
    print("\n\tMissing number: ", find_missing_number(x), sep = "")
    print("-"*100, "\n", sep = "")
    i+=1

if __name__ == "__main__":
    main()