'''
https://www.educative.io/courses/grokking-coding-interview-patterns-python/qApXVMWDm97
Solution: Snapshot Array

In this challenge, you have to implement a Snapshot Array with the following properties:

Init (length): This is the constructor and it initializes the data structure to hold the specified number of indexes. Initially, the value at each index is 0.

Set Value (idx, val): This property sets the value at a given index idx to value val.

Snapshot(): This method takes no parameters and returns the Snap ID. Snap ID is the number of times that the snapshot function was called, less 1, as we start the count at 0. The first time this function is called, it saves a snapshot and returns 0. The n^{th} time it is called, after saving the snapshot, it returns n-1.

Get Value (idx, Snap ID) method returns the value at the index in the snapshot with the given Snap ID.

Suppose that we have three nodes whose values we wish to track in the snapshot array. Initially, the value of all the nodes will be 0. After calling the Set Value (1, 4) function, the value of node 1 will change to 4. If we take a snapshot at this point, the current values of all the nodes will be saved with Snap ID 0. Now, if we call Set Value (1, 7), the current value for node 1 will change to 7. Now, if we call the Get Value (1, 0) function, we will get the value of node 1 from snapshot 0, that is, 4.

Time complexity
Let n be the number of nodes and m be the number of snapshots. We will have O(n) time complexity for the constructor, O(1) time complexity for the Get Value (idx, Snap ID) function, O(1) time complexity for the Set Value(idx, val) function, and O(1) time complexity for the Snapshot() function.

Space complexity
To solve the problem given above, we will use O(n∗m) space, where n will be the number of nodes and m will be the number of saved states.
'''

class SnapshotArray:
    # Constructor
    def __init__(self, length):
        self.snapid = 0
        self.node_value = dict()
        self.node_value[0] = dict()
        self.ncount = length

    # Function set_value sets the value at a given index idx to val.
    def set_value(self, idx, val):
        if idx < self.ncount:
            self.node_value[self.snapid][idx] = val

    # This function takes no parameters and returns the snapid.
    # snapid is the number of times that the snapshot() function was called minus 1.
    def snapshot(self):
        self.node_value[self.snapid + 1] = (self.node_value[self.snapid]).copy()
        self.snapid += 1
        return self.snapid - 1

    # Function get_value returns the value at the index idx with the given snapid.
    def get_value(self, idx, snapid):
        if snapid < self.snapid and snapid >= 0 and idx < self.ncount:
            return self.node_value[snapid][idx] if idx in self.node_value[snapid] else 0
        else:
            return None

    def __str__(self):
        return str(self.node_value)

def main():
    num_nodes = [3, 5, 5, 3, 2]
    node_values = [
        [[0, 5], [0, 1], [2, 3], [1, 10]],
        [[4, 1],  [2, 21]],
        [[4, 12], [2, 61]],
        [[0, 15], [0, 5], [2, 13], [1, 100]],
        [[0, 32], [0, 6], [1, 2]]
    ]
    values_to_get = [
        [[0, 0], [0, 1], [1, 0]],
        [[4, 1], [2, 1], [3, 1]],
        [[4, 1], [2, 1], [3, 1]],
        [[0, 1], [1, 1]],
        [[0, 0]]
    ]

    for i in range(len(num_nodes)):
        print(i + 1, ".\tInitializing a data structure with ", num_nodes[i], " nodes", sep = "")
        snapshot_arr = SnapshotArray(num_nodes[i])
        for j in node_values[i]:
            print("\t\tSetting the value of node ", j[0], " to ", j[1], sep = "")
            snapshot_arr.set_value(j[0], j[1])
            print("\t\tDictionary: ", snapshot_arr)
            print("\t\tSnap id:", snapshot_arr.snapshot(), "\n", sep = "")
        for x in values_to_get[i]:
            print("\t\tNode value at index ", x[0], " with snapID: ", x[1], \
                    " is: ", snapshot_arr.get_value(x[0], x[1]), sep = "")
        print("\n", "-"*100, sep = "")


if __name__ == '__main__':
    main()
