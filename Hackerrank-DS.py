## Reverse an array
# Approach 1
# def RevArr(a):
#     return a.reverse()
    
# RevArr(1,2,3,4)

# Approach 2
# def RevArr(a):
#     return a[::-1]
# RevArr(1,2,3,4)

## LINKEDLIST (INSERT AT HEAD)

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class Linkedlist:
#     def __init__(self):
#         self.head = None
        
#     def insertatHead(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node
    
#     def printLL(self):
#         temp = self.head
#         while(temp != None):
#             print(temp.data)
            
#         temp = temp.next
        
# LL = Linkedlist()

# LL.insertatHead(3)
# LL.insertatHead(2)
# LL.insertatHead(1)

# LL.printLL()

## LINKEDLIST (INSERT AT TAIL)

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
        
# class Linkedlist:
#     def __init__(self):
#         self.head = None
        
#     def insert_at_tail(self, data):
#         new_node = Node(data)
#         new_node.next = None
#         if not self.head:
#             # If the list is empty, new node becomes both head and tail
#             self.head = new_node
#             self.tail = new_node
#             return
        
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
            
#     def print_ll(self):
#         temp = self.head
#         while(temp!=None):
#             print(temp.data)
#         temp = temp.next
        
# ll = Linkedlist()
# ll.insert_at_tail(3)
# ll.insert_at_tail(2)

# ll.print_ll()


# LINKEDLIST (Insert node at specific position)

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = next
    
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
        
#     def insert_at_position(self, data, position):
#         new_node = Node(data)
        
#         if position == 1:
#             new_node.next = self.head
#             self.head = new_node
            
#         temp = self.head
#         count = 1
        
#         while temp != None and temp < position - 1:
#             temp = temp.next 
#             count += 1
            
#         if temp == None:
#             print("position out of range")
#         else:
#             new_node.next = temp.next
#             temp.next = new_node
            
    
         
# LINKEDLIST (print in reverse)

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             return
#         current = self.head
#         while current.next:
#             current = current.next
#         current.next = new_node

#     def print_list(self):
#         current = self.head
#         while current:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")

#     def reversePrint(self, head):
#         if head is None:
#             return
#         self.reversePrint(head.next)
#         print(head.data, end=" -> ")

# # Example usage:
# linked_list = LinkedList()
# linked_list.append(1)
# linked_list.append(2)
# linked_list.append(3)
# linked_list.append(4)

# print("Original linked list:")
# linked_list.print_list()

# print("\nReversed linked list:")
# linked_list.reversePrint(linked_list.head)
# print("None")


# DELETE A NODE (HEAD)

# head = head.next

# DELETE A NODE (TAIL)

# while temp.next.next != None:
#     temp = temp.next 

# temp.next = None 
    
        
        
        
                
                
            
            
            
        
                
            
            
            
                
            
        
        
        