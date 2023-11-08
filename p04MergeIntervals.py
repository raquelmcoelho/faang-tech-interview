'''
https://www.educative.io/courses/grokking-coding-interview-patterns-python/RLQVvyjr0gR
Solution: Merge Intervals

We’re given an array of closed intervals as input where each interval has a start and end timestamp. The input array is sorted by starting timestamps. Merge the overlapping intervals and return a new output array.

Time complexity
The time complexity of this solution is O(n), where n is the number of intervals provided in the input.
Space complexity
The space complexity of this solution is O(1), as, apart from the input and output arrays, only a fixed amount of space is being consumed by the solution.

'''
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.closed = True  # by default, the interval is closed
    # set the flag for closed/open

    def set_closed(self, closed):
        self.closed = closed

    def __str__(self):
        return "[" + str(self.start) + ", " + str(self.end) + "]" \
            if self.closed else \
                "(" + str(self.start) + ", " + str(self.end) + ")"

def merge_intervals(v):
    # If the list is empty
    if not v:
        return None

    result = []

    # Adding pair in the result list
    result.append(Interval(v[0].start, v[0].end))

    for i in range(1, len(v)):
        # Getting the recent added interval in the result list
        last_added_interval = result[len(result) - 1]
        # Getting and initializing input pair
        cur_start = v[i].start
        cur_end = v[i].end
        print("\t\t\tCurrent input interval:",
              "[", cur_start, ",", cur_end, "]")
        # Getting the ending timestamp of the previous interval
        prev_end = last_added_interval.end
        print("\t\t\tLast output interval:", "[", last_added_interval.start, ",", last_added_interval.end, "]")
        # Overlapping condition
        if prev_end >= cur_start:
            last_added_interval.end = max(cur_end, prev_end)
            print("\t\t\tOverlapping condition true. Updating last output interval...")
            print("\t\t\tUpdated last output interval:", "[", last_added_interval.start, ",", last_added_interval.end, "]", "\n")
        # No overlapping
        else:
            print("\t\t\tOverlapping condition false. Adding input interval to output list...")
            result.append(Interval(cur_start, cur_end))
        print("\t\t{:<4}{:<10}{:<4}{:<9}{:<4}{:<9}{:<4}{:<12}{:<5}".format( \
            "|", "cur_start", "|", "cur_end", "|", "prev_end", "|", "Overlapping", "|"))
        print("\t\t", "-"*54)
        print("\t\t{:<4}{:<10}{:<4}{:<9}{:<4}{:<9}{:<4}{:<12}{:<5}".format( \
            "|", cur_start, "|", cur_end, "|", prev_end, "|", bool(prev_end >= cur_start), "|"))
        print("\n")
    return result

# Printing list of intervals


def interval_list_to_str(lst):
    result_str = ""
    for i in range(len(lst)):
        result_str += str(lst[i]) + ", "
    return "[" + result_str[:-2] + "]"


def main():
    v1 = [Interval(1, 5), Interval(3, 7), Interval(4, 6)]
    v2 = [Interval(1, 5), Interval(4, 6), Interval(6, 8), Interval(11, 15)]
    v3 = [Interval(3, 7), Interval(6, 8), Interval(10, 12), Interval(11, 15)]
    v4 = [Interval(1, 5)]
    v6 = [Interval(1, 9), Interval(4, 4), Interval(3, 8)]
    v7 = [Interval(1, 2), Interval(3, 4), Interval(8, 8)]
    v8 = [Interval(1, 5), Interval(1, 3)]
    v9 = [Interval(1, 5), Interval(6, 9)]
    v10 = [Interval(0, 0), Interval(1, 18), Interval(1, 3)]

    v_list = [v1, v2, v3, v4, v6, v7, v8, v9, v10]

    for i in range(len(v_list)):
        print(i + 1, ". Intervals to merge: ", interval_list_to_str(v_list[i]), sep="")
        result = merge_intervals(v_list[i])
        print("   Merged intervals:\t", interval_list_to_str(result))
        print("-"*100)


if __name__ == '__main__':
    main()
