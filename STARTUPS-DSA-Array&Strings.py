# -----------ARRAYS-------------

# 1) Second Largest number in an array

# def secondLargest(arr):
    
#     arr.sort()
#     kth_max = arr[-k]
    
#     return kth_max
    
      
# arr = [6,4,5,2,3,1]
# k = 2
# result = secondLargest(arr)
# print("Second Largest no is: ", result)





# 2) Rotate an array by k

# def rotateArray(arr, k):
#     r = arr[k:] + arr[:k]
    
#     return r
    
# arr = [1,5,4,3,2,6]  
# k = 2
# result = rotateArray(arr, k)
# print(result)





# 3) Intersection of Two arrays

# s = [1,2,5,6,7]
# t = [2,5,6,9,8,4]

# a = set(s)
# b = set(t)

# intersection = a & b
# print(intersection)




# 4) Pair sum

# arr = [1, 2, 3, 4, 5]
# target = 6

# found_pair = False

# n = len(arr)

# for i in range(n):
#     for j in range(i + 1, n):
#         if arr[i] + arr[j] == target:
#             print(arr[i], arr[j])
#             found_pair = True
            
# if not found_pair:
#     print(-1)




# 5) Move zeroes to end

# arr = [1,2,0,0,0,3,4,9]
# zeroes = []

# for i in arr:
#     if i == 0:
#         zeroes.append(i)
# result = [num for num in arr if num != 0] + zeroes
# print(result)




# 6) First missing positive

# arr = [2,4,-1,1]

# filtered_array = [num for num in arr if num > 0]
# # arr = [2,4,1]

# filtered_array.sort()
# # arr = [1,2,4]

# smallest_missing = 1
# for i in filtered_array:
#     if i == smallest_missing:
#         smallest_missing += 1
#     elif i > smallest_missing:
#         break
# print("Missing number is: ",smallest_missing)





# 7) Bubble Sort Algorithm

# arr = [6,2,8,4,10]

# n = len(arr)

# for i in range(n):
#     for j in range(i+1 ,n):
#         if arr[i] > arr[j]:
#             temp = arr[i]
#             arr[i] = arr[j]
#             arr[j] = temp
            
# print("Bubble Sorted Array: ",arr)



# 8) Insertion sort 

# arr = [2,8,5,3,9,4,1]
# n = len(arr)

# for i in range(n):
#     for j in range(i+1, n):
        
#         if arr[i] > arr[j]:
#             arr[i],arr[j] = arr[j],arr[i]
            
# print("Insertion Sorted Array: ",arr)



# 9) 
            
            
    
    













# ---------------- STRINGS ------------------

# 1) Reverse the string words wise

# s = "Welcome to Coding Ninjas"

# a = s.split()
# result = ' '.join(a[::-1])
# print(result)




# 2) Encoding String

# s = "aaaabbbccdaa" 
# count = 1
# result = ""

# for i in range(1, len(s)):
#     if s[i] == s[i-1]:
#         count += 1
#     else:
#         result += s[i-1] + str(count)
#         count = 1
        
# result += s[-1] + str(count)
# print(result)



# 3) First non-repeating character in the string

# def first_non_repeating_char(s):
#     d = {}
    
#     for i in s:
#         if i not in d:
#             d[i] = 0
#         d[i] += 1

   
#     for char in d:
#         if d[char] == 1:
#             print("First non-repeating character is:", char)
#             return
        
#     print("No non-repeating character found")

# s = "pentaloop"
# first_non_repeating_char(s)




# 4) Check permuatation

# string1 = "HEY"
# string2 = "EYH"

# if sorted(string1) == sorted(string2):
#     print("Strings provided are anagram!")
# else:
#     print("Not Anagrams!")



