# Return true if there's duplicate in string else false

# arr = [1,2,3,4,5,1,2]

# def duplicate(arr):

#     return len(arr) != len(set(arr))
# duplicate()



# See if the given two strings anagram
# def anagram(s, t):
#     return sorted(s) == sorted(t)

# anagram()


# Find Common letter between two strings

# def common():
#     a = input("Enter string 1: ")
#     b = input("Enter string 2: ")

#     c = set(a)
#     d = set(b)

#     commonLogic = c & d

#     print(commonLogic)

# common()


# Count the frequency of the words

# def frequency():
#     a = input("Enter a string: ")
#     seperator = a.split()
#     d = {}

#     for i in seperator:
#         if i not in d.keys():
#             d[i] = 0
#         d[i] = d[i] + 1

#     print(d)
# frequency()



# Convert two lists into a dictionary

# def list_to_dic():
#     list1 = ["One", "Two", "Three"]
#     list2 = [1, 2, 3]

#     my_dict = dict(zip(list1, list2))
#     print(my_dict)

# list_to_dic()

# Sum of digits

# def SOD(n):
#     total = 0
#     while n > 0:
#         digit = n % 10 
#         total += digit
#         n = n // 10
        
#     return total

# SOD(5)






