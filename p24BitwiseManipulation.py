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
    print("\n\tTraversing the first string")
    for i in range(first_string_length):
        print("\t\t", print_string_with_markers(first_string, i), sep="")
        print("\t\tCurrent character:", first_string[i])
        print("\t\tresult:", result)
        print("\t\tPerforming XOR operation")
        print("\t\t\tresult XOR ASCII(",
              first_string[i], ") = ", result, " XOR ", (ord)(first_string[i]), sep="")
        # Perform the xor operation with the result
        result = result ^ (ord)(first_string[i])
        print("\t\tresult:", result, "\n")

    # Traverse string 2 till the end and perform xor with the result
    print("\n\tTraversing the second string")
    for j in range(second_string_length):
        print("\t\t", print_string_with_markers(second_string, j), sep="")
        print("\t\tCurrent character:", second_string[j])
        print("\t\tresult:", result)
        print("\t\tPerforming XOR operation")
        print("\t\t\tresult XOR ASCII(",
              second_string[j], ") = ", result, " XOR ", (ord)(second_string[j]), sep="")
        # Perform the xor operation with the result
        result = result ^ (ord)(second_string[j])
        print("\t\tresult:", result, "\n")

    # Returning the result based on the condition
    print("\tResult is the ASCII value of the extra character")
    print("\t\tExtra character = char(", result, ") ⟶ ", (chr)(result), sep = "")
    print("\n\tString 1's length: ", len(first_string), sep = "")
    print("\tString 2's length: ", len(second_string), sep = "")
    if len(first_string) > len(second_string):
        index = first_string.index((chr)(result))
        print("\tSince String 1's length is greater than string 2's length,\n\tthe extra character is in string 1.")
        print("\t\t", print_string_with_markers(first_string, index), sep = "")
        print("\tExtra character is '", first_string[index], "' ", end = "", sep = "")
        return first_string.index((chr)(result))
    else:
        index = second_string.index((chr)(result))
        print("\tSince String 2's length is greater than string 1's length,\n\tthe extra character is in string 2.")
        print("\t\t", print_string_with_markers(second_string, second_string.index((chr)(result))), sep = "")
        print("\tExtra character is '", second_string[index], "' ", end = "", sep = "")
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
