'''
https://www.educative.io/courses/grokking-coding-interview-patterns-python/7nmg2E0DJ8y
Solution: Palindrome Permutation

For a given string, find whether or not a permutation of this string is a palindrome. You should return TRUE if such a permutation is possible and FALSE if it isn’t possible.

Time complexity
We have to iterate over a string with n characters. We also need to iterate over the hash map, which can have a size of n if all the characters in the string are distinct. Therefore, the time complexity is O(n).

Space complexity
The hash map can grow up to n if all the characters in the string are distinct. However, the number of distinct characters is bounded and so is the space complexity. So, the space complexity is O(1).
'''

def print_array_with_markers(arr, pValue):
    out = arr[:pValue] + '«' + arr[pValue] + '»' + arr[pValue+1:]
    return out


def permute_palindrome(st):
    # Create a hashmap to keep track of the characters and their occurrences
    print("\n\tPopulating the hashmap")
    frequencies = {}
    index = 0
    for i in st:
        print("\t\t", print_array_with_markers(st, index), sep="")
        index += 1
        print("\t\tCharacter: ", i, sep="")
        print("\t\tHashmap: ", frequencies, sep="")
        if i in frequencies:
            print("\t\t\t", i, " is already present in the hashmap", sep="")
            print("\t\t\tUpdating its frequency  ⟶ ", sep="", end="")
            frequencies[i] += 1
            print(frequencies, "\n", sep="")
        else:
            print("\t\t\t", i, " is not present in the hashmap", sep="")
            print("\t\t\tSetting its frequency = 1  ⟶ ", sep="", end="")
            frequencies[i] = 1
            print(frequencies, "\n", sep="")
    # Traverse the hashmap and update the count by 1, whenever a
    # character with odd number of occurences is found.
    count = 0
    print("\n\tCounting the characters with odd frequencies")
    print("\t\tHash map: ", frequencies)
    print("\t\tCount = ", count, sep="")
    for ch in frequencies.keys():
        print("\t\tFrequency of '", ch, "' = ", frequencies[ch], sep="")
        if frequencies[ch] % 2:
            print("\t\t\tIncrementing count: ", count, " + 1 = ", count + 1, sep="")
            count += 1
        else:
            print("\t\t\tFrequency is not odd, moving to the next character\n")

    # If the count is smaller than or equal to 1 then the permutation exists,
    # otherwise does not
    print("\n\tCount: ", count, sep="")
    if count <= 1:
        print("\tCount is <= 1, return TRUE")
        return True
    else:
        print("\tCount > 1, returning FALSE")
        return False


# Driver Code
def main():
    str_array = ["baefeab", "abc", "xzz", "jjadd", "kllk"]
    for i in range(len(str_array)):
        print(i + 1, ".\tInput string: ", str_array[i], sep="")
        result = permute_palindrome(str_array[i])
        if result:
            print("\n\tInput string has permutations that are palindromes")
        else:
            print("\n\tInput string does not have a permutation that's a palindrome")
        print("-"*100)


if __name__ == "__main__":
    main()