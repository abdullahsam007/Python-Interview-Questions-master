
# pentaloop questions

# 1) Check if linkedlist has a loop
# 2) Find the minimum difference between any pair in the array.
# 3) ANAGRAMS
# 4) Given a string, Find the first non-repeating character in it. 

# Sperdian Technologies questions

# 5) How to get matching element in integer array
# 6) How to traverse to the middle of linkedlist



# ----------- SOLVED VERSION -------------

# 3) Anagrams

# s = 'Hey'
# t = 'yeH'
# if sorted(s) == sorted(t):
#     print("ANAGRAM!")
# else:
#     print("No")


# 2) Find the minimum difference between any pair in the array.

# arr = [1, 5, 3, 19, 18, 25]
        
# n = len(arr)
# min_difference = float('inf')


# for i in range(n):
#     for j in range(i + 1, n):
#         difference = abs(arr[i]-arr[j])
#         min_difference = min(min_difference, difference)
        
        
# print(min_difference)


# 5) How to get matching element in an array

# arr = [1,1,2,3,4,5,5]

# n = len(arr)
# matching_element = []

# for i in range(n):
#     for j in range(i + 1, n):
#         if arr[i] == arr[j]:
#             matching_element.append(arr[i])
            
# print(matching_element)



# 2) Find the first non repeating character in string







