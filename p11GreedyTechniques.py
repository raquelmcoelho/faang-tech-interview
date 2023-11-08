'''
https://www.educative.io/courses/grokking-coding-interview-patterns-python/qAqpMr72Gw0
Solution: Jump Game I

In a single-player jump game, the player starts at one end of a series of squares, with the goal of reaching the last square.

At each turn, the player can take up to s steps towards the last square, where s is the value of the current square.

For example, if the value of the current square is 3, the player can take either 3 steps, or 2 steps, or 1 step in the direction of the last square. The player cannot move in the opposite direction, that is, away from the last square.

You have been tasked with writing a function to validate whether a player can win a given game or not.

You’ve been provided with the nums integer array, representing the series of squares. The player starts at the first index and, following the rules of the game, tries to reach the last index.

If the player can reach the last index, your function returns TRUE; otherwise, it returns FALSE.

Time complexity
Since there are n elements in the array and we only visit each element once, the time complexity is O(n).

Space complexity
We don't use any additional data structures, so the space complexity is O(1).

'''

def print_array_with_markers(arr, p_value1 = -1, mrk1a = '«', mrk1b = '»', 
                            p_value2 = -1, mrk2a = '>', mrk2b = '<'):
    out = "["
    for i in range(len(arr)):
        if p_value1 == i:
            out += mrk1a
            out += str(arr[i]) + mrk1b + ", "
        elif p_value2 == i:
            out += mrk2a
            out += str(arr[i]) + mrk2b + ", "
        else:
            out += str(arr[i]) + ", "
    out = out[0:len(out) - 2]
    out += "]"
    return out


def jump_game(nums):
    print("\tSetting the last element in the array as our initial target:")
    target_num_index = len(nums) - 1
    print("\t"*2, print_array_with_markers(nums, target_num_index, '»', '«'), sep="")
    print("\tWorking backwards in the array:")
    for i in range(len(nums) - 2, -1, -1):
        print("\t"*2, "Loop iteration: ", len(nums) - i - 1, sep="")
        print("\t"*2, print_array_with_markers(nums, i, '«', '»', target_num_index, '»', '«'), sep="")
        if target_num_index == i:
            print("\t"*2, "Both the current and target indexes are the same.")
            print("\t"*2, "The target is reachable.\n")
        elif target_num_index <= i + nums[i]:
            print("\t"*2, "Since target index (", target_num_index, ") is within ",
                  nums[i], " jump(s) of current index (", i, "),\n", 
                  "\t"*2, "we can reach it from here.", sep="")
            print("\t"*3, "Updating target index to current index: ",
                  target_num_index, " → ", i, "\n", sep="")
            target_num_index = i
        else:
            print("\t"*2, "Jumping to the target is not possible from here.\n", 
                  "\t"*3, "Checking preceding indexes.\n", sep="")

    if target_num_index == 0:
        return True
    return False


def main():
    nums = [
        [3, 2, 2, 0, 1, 4],
        [2, 3, 1, 1, 9],
        [3, 2, 1, 0, 4],
        [0],
        [1],
        [4, 3, 2, 1, 0],
        [1, 1, 1, 1, 1],
        [4, 0, 0, 0, 1],
        [3, 3, 3, 3, 3],
        [1, 2, 3, 4, 5, 6, 7]
    ]

    for i in range(len(nums)):
        print(i + 1, ".\tInput array: ", nums[i], sep="")
        print("\tCan we reach the very last index? ",
              "Yes" if jump_game(nums[i]) else "No", sep="")
        print("-" * 100)


if __name__ == '__main__':
    main()
