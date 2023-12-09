# Variables
# If-else Statements
# Loops
# ----------Math------------






# 1) fibonnaci series

# def fibonacci(n):
#     if n is [0, 1]:
#         return n
#     else: 
#         return fibonacci(n-1) + fibonacci(n+2)
        
# fibonacci(5)


# 2) Sum of digits

# def SOD(n):
#     if n == 0:
#         return 0
#     else:
#         return (n % 10) + SOD(n // 10)
    
   
# result = SOD(12)
# print(result)


# 3) 








# ----------Arrays----------

# 1) Reverse an array of intergers

# arr = [1,2,3,4,5]
# arr.sort(reverse=True)

# print(arr)

# 2) Mix and Max in array

# arr = [1,23,4,5,6,78]
# ma = max(arr)
# mi = min(arr)

# print("Max: ", ma)
# print("Min: ", mi)

# 3) Intersection of two unsorted arrays

# arr1 = [1,3,5,2]
# arr2 = [3,1,7,9]


# def intersection(arr1, arr2):
#     a = set(arr1)
#     b = set(arr2)

#     result = a & b
#     print(result)

# intersection(arr1, arr2)

# 4) Union of two arrays
# arr1 = [1,2,5,6]
# arr2 = [3,4]

# def union(arr1, arr2):

#     a = set(arr1)
#     b = set(arr2)

    
#     result = a | b

#     print(result)

# union(arr1, arr2)

# 5) Remove duplicacy from array

# arr = [1,1,2,3,4,5,6,7,7]

# def dup(arr):
#     a = set(arr)

#     print(a)

# dup(arr)

# 6) Find the Second largest number in an array

# arr = [1,2,5,4]
# a = max(arr)-1

# print(a)


# 5) Left rotate an array by 1 place

# arr = [1, 2, 3, 4, 5]

# def rotation(arr):
#     if not arr:
#         return arr
    
#     mod_arr = arr[1:] + arr[:1]
#     

# rotation(arr)


# 6) Left rotate an array by D places

# def rotation(arr, d):
#     if not arr:
#         return arr
    
#     n = len(arr)
#     d = d % n # for effective rotation

#     modified_array = arr[d:] + arr[:d]

#     print(modified_array)

# arr = [1, 2, 3, 4, 5]
# rotation(arr, 2)


# 7) Right rotate an array by D places

# def right_rotation(arr, d):
#     if not arr:
#         return arr
    
#     n = len(arr)
#     d = n - (d % n)

#     modified_array = arr[:d] + arr[d:]

#     print(modified_array)

# arr = [1, 2, 3, 4, 5]
# right_rotation(arr, 1)


# 8) Moving zeroes to end

# def zeroes(arr):
#     non_zero = []
#     count_zero = 0

#     for i in arr:
#         if i != 0:
#             non_zero.append(i)

#         else:
#             count_zero += 1

#     result = non_zero + [0] * count_zero
#     return result
# arr = [1,0,2,3,5,6]  
# zeroes(arr)

# 9) Linear search basic question

# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i  # Return the index if the target is found
#     return -1  # Return -1 if the target is not found

# arr = [4, 2, 7, 1, 9, 5]
# target = 7
# result = linear_search(arr, target)
# if result != -1:
#     print(f"Element {target} found at index {result}")
# else:
#     print(f"Element {target} not found in the array")


# 10) Find Duplicates in an array

# def find_duplicates(arr):
#     seen = set()
#     duplicates = []
#     for num in arr:
#         if num in seen:
#             duplicates.append(num)
#         else:
#             seen.add(num)
            
#     return duplicates

# arr = [1, 2, 3, 4, 5]    
# duplicates = find_duplicates(arr)
# if duplicates:
#     print(duplicates)

# else:
#     print("Duplicates not present!")

# 11) Plus one (Increment +1 the last element of an array)

# def plusOne(arr):
#     if arr:
#         last = arr[-1]
#         increment = last + 1
#         arr[-1] = increment
#         print(arr)
#     else:
#         print('Bye')
# arr = [1, 2, 5]        
# plusOne(arr)

# IN FOR LOOP AS WELL

# def plusOne(arr):
#     for i in arr:
#         if i == arr[-1]:
#             temp = i
#             inc = temp + 1
#             arr[-1] = inc
            
#     print(arr)
            
# arr = [1, 2, 5]        
# plusOne(arr)


# 12) Island Perimeter






# --------------Strings---------------

# 1) Reverse a string
# def palindrome(str):

#     rev = str[::-1]
#     print(rev)
# str = 'Hello'
# palindrome(str)


# 2) Check if the string/ digit palindrome or not

# def palindrome(str):
#     if str == str[::-1]:
#         print("Palindrome!")
#     else:
#         print("Not Palindrome!")
# str = "amma"        
# palindrome(str)


# 3) Find duplicate characters in string


# def duplicates(str):
    
#     seen = set()
#     dup = set()
    
#     for char in str:
#         if char in seen:
#             dup.add(char)
#         else:
#             seen.add(char)
            
#     return dup
        
    
# str = "programming"    
# result = duplicates(str)
# print(result)

# 4) Check if two strings are anagram?

# def anagram(s, t):
    
#     return sorted(s) == sorted(t)
    
# s = 'anagram'
# t = 'angaram'    
# anagram(s, t)


# 5) Check one string is the rotation of other

# def checkRotation(s1, s2):
#     if sorted(s) == sorted(t):
#         print(" S1 is Rotation of S2")
#     else:
#         print("No")
        
        
# s1 = 'ABCD'
# s2 = 'BCDA'
# checkRotation(s1, s2)

# 6) Compress a string if aaa then a3 if aabb then a2b2








# -------------Queues-------------
# -------------HashSets / Sets-------------
# -------------HashMaps / Dictionary-------------
# -------------Tuples-------------
# -------------Heaps-------------
# -------------Functions-------------
# -------------Classes-------------
