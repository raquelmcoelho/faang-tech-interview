'''
https://www.educative.io/courses/grokking-coding-interview-patterns-python/qZnwmQO8ADp
Solution: Happy Number

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return TRUE if n is a happy number, and FALSE if not.

Time complexity
The time complexity for the solution shown above is O(logn). If no cycle exists, the fast pointer will reach 1 and the slow pointer will reach halfway to 1. However, since there were two pointers instead of one, we know that in the worst-case scenario, the cost was O(2×logn).

Space complexity
The memory complexity for the solution shown above is O(1)as we don't need any extra space because we are only manipulating pointers.

'''

def is_happy_number(n):

    # Helper function that calculates the sum of digits.
    def sum_digits(number):
        total_sum = 0
        while number > 0:
            number, digit = divmod(number, 10)
            total_sum += digit ** 2
        print("\t\tSquare sum of digits: ", total_sum)
        return total_sum

    slow_pointer = n  # The slow pointer value
    fast_pointer = sum_digits(n)  # The fast pointer value
    while fast_pointer != 1 and slow_pointer != fast_pointer:  # Terminating condition
        # Incrementing the slow pointer by 1 iteration
        slow_pointer = sum_digits(slow_pointer)
        # Incrementing the fast pointer by 2 iterations
        fast_pointer = sum_digits(sum_digits(fast_pointer))
    # If 1 is found then it returns True, otherwise False
    if(fast_pointer == 1):
        return True
    return False


def main():
    inputs = [171, 5, 19, 25, 7]
    for i in range(len(inputs)):
        print(i+1, ".\tInput Number: ", inputs[i], sep="")
        print("\tIs it a happy number? ", is_happy_number(inputs[i]))
        print("-" * 100)


if __name__ == '__main__':
    main()
