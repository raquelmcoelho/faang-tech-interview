'''
https://www.educative.io/courses/grokking-coding-interview-patterns-python/q25BJG18g6y
Solution: Subsets

Given a set of integers, find all possible subsets within the set.

Time complexity
The time complexity of this solution is exponential, 
O(2^n ⋅ n), where n is the number of integers in the given set.

Space complexity
The space complexity of this solution is O(n^2).

'''

def dict_to_lst(subset):
        result = []
        if subset == []:
            return [[]]
        for dic in subset:
            result.append(list(dic))
        return result

def get_bit(num, bit):
    # shifts the first operand the specified number of bits to the left
    temp = (1 << bit)

    # if a specific bit in the binary number is set, then return 1 else return 0
    temp = temp & num
    if temp == 0:
        return 0
    return 1

def find_all_subsets(v):
    sets = []
    
    if not v:
        return [[]]
    else:
        # finds number of subsets by taking power of length of input array
        subsets_count = 2 ** len(v)
        for i in range(0, subsets_count):
            # Set is created to store each subset
            st = set()
            for j in range(0, len(v)):
                if get_bit(i, j) == 1 and v[j] not in st:
                    st.add(v[j])
            print("\tCurrent generated subset:", st)
            # for first iteration subset list will always have an empty list
            if i == 0:
                sets.append([])
            else:
                sets.append(st)
            print("\tSubsets list:", sets, "\n")
    return dict_to_lst(sets)

def main():
    v = [[], [2, 5, 7], [1, 2], [1, 2, 3, 4], [7, 3, 1, 5]]

    for i in range(len(v)):
        print(i + 1, ". Set: ", v[i], sep='')
        subsets = find_all_subsets(v[i])
        print("\n   Subsets:", subsets)
        print("-"*100)


if __name__ == '__main__':
    main()
