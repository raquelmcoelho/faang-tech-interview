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
        if DBG:
            print("\t\t", print_string_with_markers(expression, i), sep = "")
            print("\t\tCurrent character: '", c, "'", sep = "")
        i += 1
        # To store the consecutive digits that is 52 => 5 x 10 + 2 = 52
        if c.isdigit():
            temp = number
            number = number * 10 + int(c)
            if DBG:
                print("\t\tDetected digit, updating operand: ", temp, " * 10 + ", int(c), " = ", number, sep = "")
        # Evaluate the left expression and store the new sign value
        if c in "+-":
            temp = result
            if DBG:
                print("\t\tOperator encountered")
                print("\t\t\tUpdating result: ", result, " + ", number, " * ", sign_value, " ⟶ ", result + number * sign_value, sep = "")
                print("\t\t\tUpdating sign value to: ", -1 if c == '-' else 1, sep = "")
                print("\t\t\tResetting Operand: ", number, " ⟶ 0", sep = "")
            result += number * sign_value
            sign_value = -1 if c == '-' else 1
            number = 0
        # Push the result calculated till now and store the sign value
        elif c == '(':
            if DBG:
                print("\t\tDetected '(', push intermediate result, ", result, \
                        ", and sign value, ", sign_value, ", to the\n\t\toperations_stack: ", operations_stack, " ⟶ ", end = "", sep = "")
            operations_stack.append(result)
            operations_stack.append(sign_value)
            if DBG:
                print(operations_stack)
            result = 0
            sign_value = 1

        # Convert current number to positive or negative if we need
        # to perform an addition or a subtraction respectively
        # and add it to the previously calculated result
        elif c == ')':
            result += sign_value * number
            if DBG:
                print("\t\tCurrent result: ", result)
                print("\t\tDetected ')', we'll pop the sign value from the operations_stack")
                print("\t\t\t", operations_stack, sep = "", end = "")
            pop_sign_value = operations_stack.pop()
            if DBG:
                print(" ⟶ ", operations_stack, sep = "")
                print("\t\tSign value: ", pop_sign_value, sep = "")
            temp = result
            result *= pop_sign_value

            if DBG:
                print("\t\tUpdating result: ", temp, " * ", pop_sign_value, " = ", result, sep = "")
                print("\t\tPopping from the operations_stack to get the second value")
                print("\t\t\t", operations_stack, sep = "", end = "")
            second_value = operations_stack.pop()
            if DBG:
                print(" ⟶ ", operations_stack, sep = "")
                print("\t\tSecond value: ", second_value, sep = "")
                print("\t\tUpdating result: ", result, " + ", second_value, " = ", result + second_value, sep = "")
            result += second_value
            if DBG:
                print("\t\tFinal result value is ", result,
                      " and operations_stack is ", operations_stack, sep="")
            number = 0
        if DBG: print()

    if DBG:
        print("\tResult: ", result, " + ", number, " * ", sign_value, " = ",  result + number * sign_value, sep = "")
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
        DBG = True
        print(num, ".", "\tGiven Expression: ", i, sep="")
        if DBG:
            print("\n\t\tProcessing...")
        print("\tThe result is: ", calculator(i))
        num += 1
        print("-"*100, sep="")


if __name__ == "__main__":
    main()
