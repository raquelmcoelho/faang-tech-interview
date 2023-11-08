'''
https://www.educative.io/courses/grokking-coding-interview-patterns-python/7npqY4X9qBy
Solution: 0/1 Knapsack

Suppose you have the list of weights and corresponding values for n items. You have a knapsack that can carry a specific amount of weight at a time called capacity.

You need to find the maximum profit of items using the sum of values of the items you can carry in a knapsack. The sum of the weights of the items should be less than or equal to the knapsack’s capacity.

If any combination can’t make the given knapsack capacity of weights, then return 0.

Time complexity
The time complexity of this problem is O(n.w), where n is the size of the weights and w is the given capacity of the knapsack.

Space complexity
The space complexity of this solution is O(w), where w is the given capacity of the knapsack because we used a 1-D array of capacity size.

'''

def find_max_knapsack_profit(capacity, weights, values):
    # Store values length to use it later in the code
    values_length = len(values)
    # Check if the constraints are fulfilled for the given problem
    # Check if the given capacity is no smaller than or equal to zero
    # Check if the length of values is not equal to zero, if zero we will
    # return 0
    # Check if the length of weights is not equal to the length of the values,
    # if false we will return 0
    if capacity <= 0 or values_length == 0 or len(weights) != values_length:
        return 0
    # Initialize array named profits of size (capacity + 1) and
    # fill the array with 0
    
    profits = [0] * (capacity + 1)

    print("-"*95, sep="")
    print("{:<8}{:<2}{:<12}{:<2}{:<12}{:<2}{:<12}{:<2}{:<20}{:<2}{:<15}".format("i", "|", "values[i]", "|", "weights[i]", "|", "c", "|", "Initial profit[c]",  "|", "Current profit[c]"), sep="")
    print("-"*95, sep="")
    # Iterate in values and weights list using i as an iterator where
    # values and weights list have same lengths
    for i in range(values_length):
        # Find the profit for each capacity starting from Cn to C0
        for c in range(capacity, -1, -1):
            # Check if the weight[i] is smaller than or equal to capacity
            # in range Cn - C0
            if weights[i] <= c:
                # Saving the profit for printing purposes
                init_profit = profits[c]
                # Calculate the new profit using the previous profit and
                # values[i]
                new_profit = profits[c - weights[i]] + values[i]
                # Set profits[c] value equal to the maximum of profits[c]
                # and new calculated profit
                profits[c] = max(profits[c], new_profit)
                print("{:<8}{:<2}{:<12}{:<2}{:<12}{:<2}{:<12}{:<2}{:<20}{:<2}{:<15}".format(i, "|", values[i], "|", weights[i], "|",  c, "|", init_profit,  "|", profits[c]), sep="")
    return profits[capacity]


# Driver code
def main():

    weights = [1, 2, 3, 5]
    values = [1, 5, 4, 8]
    capacity = 6

    print("We have the following list of values and weights for the capacity ", capacity, ": ", sep="")
    print("-"*30, sep="")
    print("{:<10}{:<5}{:<5}".format("Weights", "|", "Values"))
    print("-"*30)
    for i in range(len(values)):
        print("{:<10}{:<5}{:<5}".format(weights[i], "|", values[i]))
    print("\nLet's look at the following table for all iterations:\n")
    result = find_max_knapsack_profit(capacity, weights, values)
    print("\n\nThe maximum profit found: ", result, sep="")


if __name__ == '__main__':
    main()
