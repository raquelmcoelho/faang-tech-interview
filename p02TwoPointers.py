'''
https://www.educative.io/courses/grokking-coding-interview-patterns-python/7DyPRrN5OG8
Solution: Valid Palindrome

Write a function that takes a string s as input and checks whether it’s a palindrome or not.

Note: A phrase, word or sequence is a palindrome that reads the same backwards as forwards.
 
Time complexity
The time complexity is O(n) where n is the number of characters present in the string.

Space complexity
The space complexity is O(1) because we use constant space to store two indices.
'''

def is_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:  # If the elements at index l and index r are not equal,
            return False    # then the symmetry is broken, the string is not a palindrome
        left = left + 1  # Heading towards the right
        right = right - 1  # Heading towards the left
    # We reached the middle of the string without finding a mismatch, so it is a palindrome.
    return True


# Driver Code
def main():

    test_cases = ["RACEACAR", "A", "ABCDEFGFEDCBA",
                  "ABC", "ABCBA", "ABBA", "RACEACAR"]
    for i in range(len(test_cases)):
        print("Test Case #", i + 1)
        print("-" * 100)
        print("\tThe input string is '", test_cases[i], "' and the length of the string is ", len(test_cases[i]), ".", sep='')
        print("\nIs it a palindrome?.....", is_palindrome(test_cases[i]))
        print("-" * 100)


if __name__ == '__main__':
    main()
