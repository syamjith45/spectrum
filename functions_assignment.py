# #  Write a program to define a function that can accept an integer number as    input and print the "It is an even number" if the number is even, otherwise print "It is odd".
# 1. Write a program to define a function that can accept an integer number as    input and print the "It is an even number" if the number is even, otherwise print "It is odd".

# 2. Write a program to define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.

# 3. Write a program to take a string as input and return a string with vowels removed.(implement List Comprehesion)

# 4. Write a program to display Powers of 2  using Anonymous functions?(lambda,map).

# 5. Write a program to implement bubble-sort algorithm

# 6. Write a program to implement binary-search algorithm

# 7. Write a program to take two list of same length as input and return a dictionary with one as keys and other as values.

# 8. Write a program to print fibonocci series using recursion.








# 9. Write a program to find the factorial of a number using recursion.

# 10. Program to implement concept of decorator to calculate the time needed to execute one or more function in a program.

# 11. Write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.(implement generator).

# 12. Write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.(implement generator)

# 13. Write a program to implement Insertion-Sort algorithm in python.

# 14. Program to implement Linear-Search Algorithm.

# 15. Program to implement Selection-Sort Algorithm.

# 16. Write a Python program to find the second smallest number in a list using function.


#1
# n=int(input("enter a number : "))
# def num(n):
#     if n%2==0:
#         print("EVEN NUMBER")
#     else:
#         print("ODD NUMBER")

# print(num(n))

#2
# def dict_sq():
#     sq_dict={}
#     for num in range(1,21):
#         sq_dict[num]=num**2
#         print(sq_dict)
# print(dict_sq())

# #3
# def vow(input_string):
#     vowels='AEIOUaeiou'
#     y=[i for i in input_string if i not in vowels]
#     return y
# input_string=input("enter a string :  ")
# print(vow(input_string))

#4
# powers_2=lambda x:2**x
# exponents=[0,1,2,3,4,5]
# power=map(powers_2,exponents)
# print(list(power))


#7
# name1=["hari","shane","aswin"]
# name2=["kaada","major","bony"]
# x=zip(name1,name2)
# print(dict(x))

#11
# def divisible_5_and_7(n):
#     for i in range(n+1):
#         if i%5==0 and i%7==0:
#             yield i
# print(tuple(divisible_5_and_7(1000)))


# #12
# def even_number(n):
#     for i in range(n+1):
#         if i%2==0:

#             yeild i
# print(list(even_number(100)))

# 16 list_1=[]
# n=int(input("enter the no.of elements: "))
# for i in range(1,n+1):
#     elem=int(input(" enter the elements "))
#     list_1.append(elem)

# list_1.sort()
# print("sorted list is",list_1)
# print("second smallest number is ",list_1[1])
#


#9.

# def fact(n):
#     if n==0:
#         return 1

#     x= n*fact(n-1)
#     return x

# result=fact(5)
# print(result)

#8
# def fibn(n):
#     if n<=1:
#         return n
#     return fibn(n-1) + fibn(n-2)

# n_terms=10
# for i in range(n_terms):
#     print(fibn(i))


# 5
# 15) def sort(a):
#     for i in range(len(a)-1):
#         minpos=i
#         for j in range(1,6):
#             if a[j]<a[minpos]:
#                 minpos=j
#         temp=a[i]
#         a[i]=a[minpos]
#         a[minpos]=temp

# a=[5,3,8,6,7,2]
# sort(a)
# print(a)


#6 pos=-1
# def search(list,x):
#     l=0
#     h=len(list)-1
#     mid = (l+h)//2
#     while l<=h:
#         mid = (l+h)//2
#         if list[mid]==x:
#             global pos
#             pos = mid
#             return True

#         else:
#             if list[mid]<x:
#                 l=mid+1
#                 pass
#             else:
#                 h=mid-1
#                 pass
#             pass
    










# list=[4,5,6,7,8,9]
# x=5
# if search(list,x):
#     print("found at",pos)
# else:
#     print("not found")





#13 def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         current_element = arr[i]
#         j = i - 1
#         while j >= 0 and current_element < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = current_element

# # Example usage:
# my_list = [5, 2, 9, 3, 6]
# insertion_sort(my_list)
# print(my_list)  # This will print the sorted list: [2, 3, 5, 6, 9]




#14 def linear_search(arr,x):
#     for i in range(len(arr)):
#         if arr[i]==x:
#             print("found at",i )


# arr=[2,6,5,1,3,4]
# x=4
# linear_search(arr,x)