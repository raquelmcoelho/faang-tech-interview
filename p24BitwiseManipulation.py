'''
https://www.educative.io/courses/grokking-coding-interview-patterns-python/q2MzjQlVm0p
Solution: Find the Difference

Given two strings, find the index of the extra character that is present in only one of the strings.

Time complexity
The time complexity of the above solution is O(n), where n is the length of the string.

Space complexity
The space complexity of the above solution is O(1) because it does not use any extra space.
'''

def print_string_with_markers(strn, pValue):
    out = strn[:pValue] + '«' + strn[pValue] + '»' + strn[pValue+1:]
    return out


def extra_character_index(first_string, second_string):

    # Initialize the result variable to store the result
    result = 0
    # Store the length of first_string in first_string_length variable
    first_string_length = len(first_string)
    # Store length of second_string in second_string_length variable
    second_string_length = len(second_string)

    if first_string_length == second_string_length:
        return None
    # Traverse string 1 till the end and perform xor with the result
    for i in range(first_string_length):
        # Perform the xor operation with the result
        result = result ^ (ord)(first_string[i])
        
    # Traverse string 2 till the end and perform xor with the result
    for j in range(second_string_length):
        # Perform the xor operation with the result
        result = result ^ (ord)(second_string[j])

    # Returning the result based on the condition
    if len(first_string) > len(second_string):
        index = first_string.index((chr)(result))
        return first_string.index((chr)(result))
    else:
        index = second_string.index((chr)(result))
        return second_string.index((chr)(result))

def main():
    # given string
    string1_list = ["wxyz", "cbda", "jlkmn", "courae", "", "xyz", "hello"]
    string2_list = ["zwxgy", "abc", "klmn", "couearg", "", "xyz", "helo"]
    for i in range(len(string1_list)):

        print(i+1, ".\tString 1 = ",
              string1_list[i], "\n\t", "String 2 = ", string2_list[i], sep="")
        print("at index ", extra_character_index(string1_list[i], string2_list[i]), sep = "")
        print("-"*100)


if __name__ == '__main__':
    main()
