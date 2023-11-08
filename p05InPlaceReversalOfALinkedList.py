'''
https://www.educative.io/courses/grokking-coding-interview-patterns-python/NELnLMDjKvD
Solution: Reverse Linked List

Given the head of a singly linked list, reverse the linked list and return its updated head.

Time complexity
The time complexity of this solution is linear, O(n), because we can reverse the linked list in a single pass, where n is the number of nodes in a linked list.

Space complexity
The space complexity of this solution is constant, O(1), because no extra memory is required for the iterative solution.
'''

# Template for the linked list
class LinkedList:
    # __init__ will be used to make a LinkedList type object.
    def __init__(self):
        self.head = None

    # insert_node_at_head method will insert a LinkedListNode at head
    # of a linked list.
    def insert_node_at_head(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node

    # create_linked_list method will create the linked list using the
    # given integer array with the help of InsertAthead method.
    def create_linked_list(self, lst):
        for x in reversed(lst):
            new_node = LinkedListNode(x)
            self.insert_node_at_head(new_node)
    
    # __str__(self) method will display the elements of linked list.
    def __str__(self):
        result = ""
        temp = self.head
        while temp:
            result += str(temp.data)
            temp = temp.next
            if temp:
                result += ", "
        result += ""
        return result


# Template for linked list node class
class LinkedListNode:
    # __init__ will be used to make a LinkedListNode type object.
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

      
# Template for printing the linked list with forward arrows
def print_list_with_forward_arrow(linked_list_node):
    temp = linked_list_node
    while temp:
        print(temp.data, end=" ")  # print node value
        
        temp = temp.next
        if temp:
            print("→", end=" ")
        else:
            # if this is the last node, print null at the end
            print("→ null", end=" ")


def reverse(head):
    # no need to reverse if head is None
    # or there is only 1 node.
    if not head or not head.next:
        return head

    # Initializing 'list_to_do' marker
    list_to_do = head.next

    # Initializing 'reversed_list' marker which is already pointed at head
    reversed_list = head
    reversed_list.next = None
    print("\n\nBefore iterations:")
    print("\treversed list:  ", end='')
    print_list_with_forward_arrow(reversed_list)

    print("\n\tlist to do:     ", end='')
    print_list_with_forward_arrow(list_to_do)

    print("\n\nLoop iterations:", end='')
    i = 0  # used for printing purposes
    # Reversing the list
    while list_to_do:
        print("\n\tIteration ", i + 1, ":", sep='', end='')

        # Advance list_to_do
        temp = list_to_do
        list_to_do = list_to_do.next

        print("\n\t\ttemp:              ", end='')
        print_list_with_forward_arrow(temp)

        print("\n\t\tlist to do:        ", end='')
        print_list_with_forward_arrow(list_to_do)

        # Set the current node (temp) as the head of the reversed list
        temp.next = reversed_list
        reversed_list = temp

        print("\n\t\treversed list:     ", end='')
        print_list_with_forward_arrow(reversed_list)
        i += 1

    return reversed_list


def main():
    input_list = [1, 2, 3, 4, 5, 6, 7, 8]
    input_linked_list = LinkedList()
    input_linked_list.create_linked_list(input_list)

    print("The original linked list:  ", end='')
    print_list_with_forward_arrow(input_linked_list.head)
    result = reverse(input_linked_list.head)
    print("\n\nThe reversed linked list:  ", sep='', end='')
    print_list_with_forward_arrow(result)


if __name__ == '__main__':
    main()
