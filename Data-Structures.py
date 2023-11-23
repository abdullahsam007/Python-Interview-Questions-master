# -----------------Recursion------------------

# 1) Factorial of a number

# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# n = 4  
# factorial(n)


# 2) Reverse a string: 

# def revString(str):
#     if not str:
#         return " "
#     else:
#         return revString(str[::-1])
# str = "Hey"  
# revString(str)


# 3) fibonnaci series

# def fibonacci(n):
#     if n is [0, 1]:
#         return n
#     else: 
#         return fibonacci(n-1) + fibonacci(n+2)
        
# fibonacci(5)


# 4) Sum of digits

# def SOD(n):
#     if n == 0:
#         return 0
#     else:
#         return (n % 10) + SOD(n // 10)
    
   
# result = SOD(12)
# print(result)


# ----------LINKEDLIST------------

# 1) Creation of Singly Linkedlist

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
    
# class Node:
#     def __init__(self, value):
#         self.value = None
#         self.next = None
        
# newLL = LinkedList()
# node1 = Node(1)
# node2 = Node(2)

# newLL.head = node1
# newLL.head.next = node2
# newLL.tail = node2

# 2) Insertion 
# -> At the beginning (head) APPROACH 1

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def insert_at_head(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node

#     def print_list(self):
#         current = self.head
#         while current:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")

# linked_list = LinkedList()
# linked_list.insert_at_head(3)
# linked_list.insert_at_head(2)
# linked_list.insert_at_head(1)

# linked_list.print_list()

# -> At the beginning (head) APPROACH 2

# newNode = Node
# def insertAtHead(head, data):
#     if head != None:
#         newNode.next = head
#     return newNode
        

        
# -> At the end
# class Node:
#     def __init__(self, data):
#         self.data = None
#         self.next = None
    
# class LL:
#     def __init__(self):
#         self.head = None
#         self.tail = None
        
#     def insertTail(head, data):
#         newNode = Node(data) #creating newNode
        
#         if head == None:
#             head = newNode
#         else:
#             temp = head
#             while temp.next != None:
                
        
            
        
        
        
# -> In the middle
        
      
    
        





