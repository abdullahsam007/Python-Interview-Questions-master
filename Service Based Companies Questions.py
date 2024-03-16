# Linked list

# 1) Reverse a linkedlist

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
        
        
        

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

# Example Usage
linked_list = LinkedList()
linked_list.push(1)
linked_list.push(2)
linked_list.push(3)
linked_list.push(4)

print("Original Linked List:")
linked_list.print_list()

linked_list.reverse()

print("\nReversed Linked List:")
linked_list.print_list()

    
    
    
    
# 2) Mid point in linked list

# class ListNode:
#     def __init__(self, value, None):
#         self.value = value
#         self.next = None

# def find_middle_node(head):
#     slow = fast = head

#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next

#     return slow

# # Example usage:
# # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
# head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# middle_node1 = find_middle_node(head1)
# print("Middle Node:", middle_node1.value)  # Output: 3

# # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6
# head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
# middle_node2 = find_middle_node(head2)
# print("Middle Node:", middle_node2.value)  # Output: 4


# 3) Add two linked lists








    
    
    
    

