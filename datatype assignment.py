
# 1. Write a program to find the transpose of a matrix.

# X = [[12,7],
#     [4 ,5],
#      [3 ,8]]
# result = [[0,0,0],
#           [0,0,0]]
# for i in range(len(X)):
#    for j in range(len(X[0])):
#     result[j][i] = X[i][j]
# for r in result



#6. write a program to find the sum of all the elements in list

# list1=[]
# for i in range(5):
#     val = int(input("enter numbers :"))
#     list1.append(val)
# sum=0
# for i in range(5):
#     sum = sum + list1[i]
# print(sum)

# 2.write a program thaat accept sequence of lines as input and prints the lines after making all characters in the sentences captilazied
# lines=[ ]
# while True:
#     l=input(" enter a lines  ")
#     if l:
#         lines.append(l.upper())
#     else:
#         break
# for l in lines:
#     print(l)

#8. write a program that accept a sentences and calculate the numbers of letter and digit

# s=input("input a string ")
# d=l=0
# for c in s:
#     if c.isdigit():
#         d=d+1
#     elif c.isalpha():
#         l+=1
#     else:
#         pass
# print("letters",l)
# print("digits",d)

# #10.write a program to implement list comprehension
# x=[i for i in range(0,100,2) if i%5==0]
# print(x)

#13.write a python program to print the number of specified list after removing even numbers from it.
# x=[i for i in range(0,100)]
# y=[]
# for i in x:
#     if i%2!=0:
#         y.append(i)
# print(y)

# 12,write a program to find the largest and smallest element from a list
# x=[i for i in range(0,100)]
# print("largest number is" ,max(x))
# print("smallest number is" ,min(x))

# 14. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30
# x=[i**2 for i in range(1,30)]
# print(x[:5])
# print(x[-5:])
# 15.Write a Python program to insert a given string at the beginning of all items in a list.
# list1=['apple','orange','grape']
# prifix_string="fruit_"
# modified_list=[] 
# for i in list1:
#     modified_item=prifix_string+i
#     modified_list.append(modified_item)
# print(modified_list)
# 16.Write a Python program to iterate over two lists simultaneously.

# list1 = [1, 2, 3, 4]
# list2 = ['a', 'b', 'c', 'd']

# # Use the zip function to iterate over both lists simultaneously
# for item1, item2 in zip(list1, list2):
#     print(item1, item2)


# 20. Write a Python program to sum all the items in a dictionary.
# # Create a dictionary
# my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# # Add a new key-value pair
# my_dict['country'] = 'USA'

# # Print the updated dictionary
# print(my_dict)


# 21 Create a dictionary to hold information about pets. Each key is an
# animal's name, and each value is the kind of animal.Eg : {'Dog':'Willie'}
# Put at least 3 key-value pairs in your dictionary.
# Use a for loop to print out a series of statements such as "Willie is a
# dog."


# pets = {'Willie': 'Dog', 'Fluffy': 'Cat', 'Buddy': 'Rabbit'}

# for x,y in pets.items():
#     print("{} is a {}".format(x,y))
    
# 22. Write a python function to create and return a new dictionary from the
# given dictionary (subject: mark).
# Create a new dictionary with subject having marks more than 50.
# marks = {English: 40,'Maths': 60, 'Hindi: 30,'Chemistry': 46,'Physics': 70}

# def filter_marks(marks_dict):
    # filtered_dict = {}
#     for subject, mark in marks_dict.items():
#         if mark > 50:
#             filtered_dict[subject] = mark
#     return filtered_dict

# # Original dictionary
# marks = {'English': 40, 'Maths': 60, 'Hindi': 30, 'Chemistry': 46, 'Physics': 70}

# # Call the function to create a new dictionary with marks more than 50
# filtered_marks = filter_marks(marks)

# # Print the filtered dictionary
# print(filtered_marks)


# 23. Write a python function which accepts a sentence and finds the
# number of letters and digits in the sentence.
# It should return a dictionary in which the key should be letter count and
# value should be digit count. Ignore the spaces or any other special
# character in the sentence.

# def count_letters_and_digits(sentence):
#     letter_count = 0
#     digit_count = 0

#     # Iterate through each character in the sentence
#     for char in sentence:
#         # Check if the character is a letter
#         if char.isalpha():
#             letter_count += 1
#         # Check if the character is a digit
#         elif char.isdigit():
#             digit_count += 1

#     # Create a dictionary with letter count as the key and digit count as the value
#     result_dict = {'Letter Count': letter_count, 'Digit Count': digit_count}

#     return result_dict

# # Input sentence
# sentence = "Hello, 123 World!"

# # Call the function to count letters and digits
# result = count_letters_and_digits(sentence)

# # Print the result
# print(result)


# 24. Write a Python function which generates and returns a dictionary
# where the keys are numbers between 1 and n (both inclusive) and the
# values are square of keys.


# def generate_square_dictionary(n):
#     square_dict = {}
#     for i in range(1, n + 1):
#         square_dict[i] = i**2
#     return square_dict

# # Example: Generate a dictionary for numbers from 1 to 5
# n = 5
# result_dict = generate_square_dictionary(n)

# # Print the result
# print(result_dict)
