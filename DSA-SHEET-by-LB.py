# Reverse an array/string

# a  = ['ali','ila']
# print(a[::-1])



# Find the maximum and minimum element in an array

# arr = [5,3,4,2]
# maxval = minval = arr[0]

# for i in arr:
    
#     if i > maxval:
#         maxval = i
        
#     elif i < minval:
#         minval = i
        
# print(maxval, minval)





# Find the “Kth” max and min element of an array

# def kth(arr, k):
#     if not arr or k <= 0:
#         return None, None
    
#     sorted_arr = sorted(arr)
    
#     kth_max = sorted_arr[-k]
#     kth_min = sorted_arr[k-1]
    
#     return kth_min, kth_max
# kth(1,4,5,6,3)
# k = 3





# Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo

# class Sorting:
#     def letSort(self, arr, n):
#         return arr.sort() 
        
#     letSort(0,1,4)






# Move all negative elements to the end

# arr = [2, 1, 3, -4, 5, -6]

# positive = [num for num in arr if num >= 0]
# negative = [num for num in arr if num < 0]

# final  = positive + negative
# print(final)




# Find the UNION and INTERSECTION of two arrays
# a = [1,2,4,5]
# b = [2,3,4,7]

# c = set(a)
# d = set(b)

# intersection = c & d
# print(intersection)

# union = c | d
# print(union)






# Left rotate the last element

# arr = [1, 2, 6, 4, 8, 42]
# last = arr[-1]

# rotated_array = [last] + arr[:-1]
# print(rotated_array)





# Median of two sorted arrays of Different sizes

# a = [1, 5, 9]
# b = [2, 3, 6, 7]

# c = a + b
# arr = sorted(c)

# n = len(arr)

# if n % 2 == 1:
#     # Odd number of elements
#     median = arr[n // 2]
# else:
#     # Even number of elements
#     median = (arr[n // 2 - 1] + arr[n // 2]) / 2

# print("Median:", median)







# Median of one unsorted array
# a = [10, 5, 9, 2, 3, 7]

# arr = sorted(a)

# n = len(arr)

# if n % 2 == 1:
#     # Odd number of elements
#     median = arr[n // 2]
# else:
#     # Even number of elements
#     median = (arr[n // 2 - 1] + arr[n // 2]) / 2

# print("Median:", median)





# Check if the array is palindromic or not








    


    
    
    
  
 



