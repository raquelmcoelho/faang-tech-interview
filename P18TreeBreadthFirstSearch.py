'''
https://www.educative.io/courses/grokking-coding-interview-patterns-python/JPzNn45vAKo
Solution: Level Order Traversal of Binary Tree

Given the root of a binary tree, display the values of its nodes while performing a level order traversal. Print node values for all levels separated by the specified character, :.

Time complexity
The time complexity of this solution is linear, O(n), where n is the number of nodes because every node is visited and printed only once.

Space complexity
The space complexity of this solution is linear, O(n), since the algorithm instantiates queues that take up space of up to ⌈n/2⌉ nodes. This is because the maximum queue size occurs at the level of the leaf nodes of a balanced binary tree.
'''

from collections import deque

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

        # below data members used only for some of the problems
        self.next = None
        self.parent = None
        self.count = 0

    ##### adicional ####
    def printTree(self, level=0):
      if self == None:
        return
    
      if self.right is not None:
        self.right.printTree(level + 1)
    
      print((' ' * 4 * level) + '-> ' + str(self.data))
      
      if self.left is not None:
        self.left.printTree(level + 1)


class BinaryTree:
    def __init__(self, *args):
        if len(args) < 1:
            self.root = None
        elif isinstance(args[0], int):
            self.root = BinaryTreeNode(args[0])
        else:
            self.root = None
            for x in args[0]:
                self.insert(x)

    # for normal BT level by level insertion
    def insert_bt(self, key):
        temp_queue = []
        temp = self.root

        temp_queue.append(temp)

        while len(temp_queue):
            temp = temp_queue[0]
            temp_queue.pop(0)

            if not temp.left:
                temp.left = BinaryTreeNode(key)
                break
            else:
                temp_queue.append(temp.left)

            if not temp.right:
                temp.right = BinaryTreeNode(key)
                break
            else:
                temp_queue.append(temp.right)

    # for BST insertion
    def insert(self, node_data):
        new_node = BinaryTreeNode(node_data)
        if not self.root:
            self.root = new_node
        else:
            parent = None
            temp_pointer = self.root
            while temp_pointer:
                parent = temp_pointer
                if node_data <= temp_pointer.data:
                    temp_pointer = temp_pointer.left
                else:
                    temp_pointer = temp_pointer.right
            if node_data <= parent.data:
                parent.left = new_node
            else:
                parent.right = new_node

    def find_in_bst_rec(self, node, node_data):
        if not node:
            return None
        if node.data == node_data:
            return node
        elif node.data > node_data:
            return self.find_in_bst_rec(node.left, node_data)
        else:
            return self.find_in_bst_rec(node.right, node_data)

    def find_in_bst(self, node_data):
        return self.find_in_bst_rec(self.root, node_data)

    def populate_parents_rec(self, node, parent):
        if node:
            node.parent = parent
            self.populate_parents_rec(node.left, node)
            self.populate_parents_rec(node.right, node)

    def populate_parents(self):
        self.populate_parents_rec(self.root, None)

    def get_sub_tree_node_count(self, node):
        if not node:
            return 0
        else:
            return 1 + self.get_sub_tree_node_count(node.left) + self.get_sub_tree_node_count(node.right)

    def populate_count_rec(self, node):
        if node:
            node.count = self.get_sub_tree_node_count(node)
            self.populate_count_rec(node.left)
            self.populate_count_rec(node.right)

    def populate_count(self):
        self.populate_count_rec(self.root)

    def get_tree_deep_copy_rec(self, node):
        if node:
            new_node = BinaryTreeNode(node.data)
            new_node.left = self.get_tree_deep_copy_rec(node.left)
            new_node.right = self.get_tree_deep_copy_rec(node.right)
            return new_node
        else:
            return None

    def get_tree_deep_copy(self):
        if not self.root:
            return None
        else:
            tree_copy = BinaryTree()
            tree_copy.root = self.get_tree_deep_copy_rec(self.root)
            return tree_copy

    def find_in_BT_rec(self, node, node_data):
        if not node:
            return None

        if node.data == node_data:
            return node

        left_node = self.find_in_BT_rec(node.left, node_data)
        if left_node:
            return left_node

        right_node = self.find_in_BT_rec(node.right, node_data)
        return right_node

    def find_in_BT(self, node_data):
        return self.find_in_BT_rec(self.root, node_data)


def level_order_traversal(root):
    result = ""
    # We print None if the root is None
    if not root:
        result += ("None")
    else:
        # Initializing the current queue
        current_queue = deque()

        # Initializing the dummy node
        dummy_node = BinaryTreeNode(0)

        current_queue.append(root)
        current_queue.append(dummy_node)

        # Printing nodes in level-order until the current queue remains
        # empty
        while current_queue:
            # Dequeuing and printing the first element of queue
            temp = current_queue.popleft()
            result += str(temp.data)

            # Adding dequeued node's children to the next queue
            if temp.left:
                current_queue.append(temp.left)

            if temp.right:
                current_queue.append(temp.right)

            # When the dummyNode comes next in line, we print a new line and dequeue
            # it from the queue
            if current_queue[0] == dummy_node:
                current_queue.popleft()

                # If the queue is still not empty we add back the dummy node
                if current_queue:
                    result += " : "
                    current_queue.append(dummy_node)
            else:
                result += ", "
    return result


def main():
    # Creating a binary tree
    input1 = [100, 50, 200, 25, 75, 350]
    tree1 = BinaryTree(input1)

    # Creating a right degenerate binary tree
    input2 = sorted(input1)
    tree2 = BinaryTree(input2)

    # Creating a left degenerate binary tree
    input2.reverse()
    tree3 = BinaryTree(input2)

    # Creating a single node binary tree
    tree4 = BinaryTree(100)

    roots = [tree1.root, tree2.root, tree3.root, tree4.root, None]

    for i in range(len(roots)):
        print(i+1, ".\tBinary Tree:", sep = "")
        
        #display_tree(roots[i])
        if(roots[i] != None):
          roots[i].printTree()
        
        # Printing the in-order list using the method we just implemented
        print("\n\tLevel order traversal: ", sep = "", end = "")
        print(level_order_traversal(roots[i]))
        print("\n", "-"*100, "\n", sep = "")


if __name__ == '__main__':
    main()
