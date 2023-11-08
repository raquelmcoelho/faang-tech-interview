'''
https://www.educative.io/courses/grokking-coding-interview-patterns-python/N8jRyEng5vK
Solution: Basic Calculator

Given a string containing an arithmetic expression, implement a basic calculator that evaluates the expression string. The expression string can contain integer numeric values and should be able to handle the “+” and “-” operators, as well as “()” parentheses.

Time complexity
Since we are only traversing the string once, the time complexity of the algorithm above is O(n), where n is the length of the string.

Space complexity
The space complexity is O(n) in the worst case, where most of the expression is a series of nested sub-expressions.
'''

def print_string_with_markers(strn, pValue):
    out = strn[:pValue] + '«' + strn[pValue] + '»' + strn[pValue+1:]
    return out

def calculator(expression):
    # We'll use sign_value variable to represent the
    # positive or negative operator
    number = 0
    sign_value = 1
    result = 0
    operations_stack = []

    i = 0
    for c in expression:
        i += 1
        # To store the consecutive digits that is 52 => 5 x 10 + 2 = 52
        if c.isdigit():
            temp = number
            number = number * 10 + int(c)
        # Evaluate the left expression and store the new sign value
        if c in "+-":
            temp = result
            result += number * sign_value
            sign_value = -1 if c == '-' else 1
            number = 0
        # Push the result calculated till now and store the sign value
        elif c == '(':
            operations_stack.append(result)
            operations_stack.append(sign_value)
            result = 0
            sign_value = 1

        # Convert current number to positive or negative if we need
        # to perform an addition or a subtraction respectively
        # and add it to the previously calculated result
        elif c == ')':
            result += sign_value * number
            pop_sign_value = operations_stack.pop()
            result *= pop_sign_value

            second_value = operations_stack.pop()
            result += second_value
            
            number = 0
        
    return result + number * sign_value
    
# Driver code
def main():
    global DBG
    input = (
             "4 + (52 - 12) + 99",
             "(31 + 7) - (5 - 2)",
             "(12 - 9 + 4) + ( 7 - 5)",
             "8 - 5 + (19 - 11) + 6 + (10 + 3)",
             "56 - 44 - (27 - 17 - 1) + 7"
            )

    num = 1
    for i in input:
        # Set to False to supress line-by-line trace
        DBG = False
        print(num, ".", "\tGiven Expression: ", i, sep="")
        if DBG:
            print("\n\t\tProcessing...")
        print("\tThe result is: ", calculator(i))
        num += 1
        print("-"*100, sep="")


if __name__ == "__main__":
    main()
