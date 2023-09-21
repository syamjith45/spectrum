#1 Write a program to check whether the entered number is postive or negative
#num =int(input("enter a number : "))
# if num>0:
#     print("positive")
# else:
#     print("negative")***


#2.Write a program to  swap two variables.
# a=20
# b=30
# temp=a
# a=b
# b=temp
# print(a)
# print(b)

#3.Write a program to  Determine If Year Is Leap Year
# num=int(input("enter the year: "))
# if (num%4==0) or (num%100!= 0):

#     print('leap year')
# else:
#     print("not leap year")

#4.Write a program check whether the given number is odd or even.
# num=int(input("enter a number: "))
# if num%2==0:
#     print("even")
# else:
#     print("odd")



#5.Write a program to print the fibonocci series.
# num=int(input("enter a number: "))
# a=0
# b=1
# count=0
# while num>count:
#     print(a)
#     c=a+b
#     a=b
#     b=c
#     count+=1

#6.Write a program to print the prime numbers between given interval
# num=int(input("enter a number: "))
# for i in range(2,num):
#     if (num%i)==0:
#         print(num,"is not a prime")
#         break
#     print(num,'is a prime number')
 
 # 7.Python program to display all the prime numbers within an interval

# lower = 1
# upper = 100

# print("Prime numbers between", lower, "and", upper, "are:")
# for num in range(lower,upper+1):
#     if num>1:
#         for i in range(2,num):
#             if (num%i)==0:
#                 break
#         else:
#             print(num)


#8. Write a program for Printing Odd numbers between 1 and 50 and calculate the sum of that numbers.
# sum=0
# for i in range(1,51,2):
    
#     sum=sum+i
# print(sum)

#9.Write a program to find the factorial of the given number.
# num=10
# factorial=1
# for i in range(1,num+1):
#     factorial=factorial*i
# print(factorial)


#10.Write a program to Check if the given string  is Palindrome or not.
# txt="malayalam"
# reverse=txt[::-1]
# if txt == reverse:
#     print("palindrome")
# else:
#     print("not a palindrome")
# rev=""
# for i in txt:
#     rev=i+rev
# print(rev)
#11. Write a program to find sum of all integers greater than 100 and less than 200 that are divisible by 7
# lower=100
# upper=200
# sum=0
# for num in range(lower,upper+1):
#     if (num%7)==0:
#         sum=sum+num
# print(sum)

#12.Write a program to Display Multiplication Table
# num=int(input("enter a number: "))
# for i in range(1,11):
#     m=i*num
#     print(i,"*",num,"=",m)



#13. Write a program to calculate the area and perimeter of a rectangle..
# l=int(input("enter a number: "))
# b=int(input("enter a number: "))
# perimeter=2*(l+b)
# area=l*b
# print("perimeter:",perimeter)
# print("area :",area)



#14. Write a program to find the sum of n' Natural Numbers.
# num=int(input("enter a number: "))
# sum=0
# for i in range(num+1):
#     sum+=i
#     print(sum)

#15.Write a program to find whether given no. is Armstrong or not
# num=370
# n=num
# sum,digit=0,0
# length=len(str(n))
# for i in range(length):
#     digit=int(n%10)
#     n=n//10
#     sum=sum+pow(digit,length)
# if sum==num:
#      print("Armstrong number")
# else:
#     print("not armstrong number")

#16. Write a program to find the largest among 3 numbers

# num1=int(input("enter a number: "))
# num2=int(input("enter a number: "))
# num3=int(input("enter a number: "))
# if num1>num2 and num1>num3:
#     print(num1)
# elif num2>num1 and num2>num3:
#     print(num2)
# else:
#     print(num3)



#17. Write a program to remove all punctuations from given string.
# test_str = "Gfg, is best : for ! Geeks ;"

# pun= '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

# for i in test_str:
#     if i in pun:
#         print(i)
#         test_str=test_str.replace(i,"")
# print(test_str)


#18.Write a program to count the no:of each vowel in a given string
# string="hello world"
# count=0
# vowels_list=['a','e','i','o','u']
# for i in string:
        
#         if i in vowels_list:
                
#                 count=count+1
                
        
# print(count)

 #Program to perform Addition,Subtraction,Multiplication and division on Complex-No's.
# real_part = float(input("Enter the real part: "))
# imaginary_part = float(input("Enter the imaginary part: "))
# complex_num1=complex(real_part,imaginary_part)
# complex_num2=complex(real_part,imaginary_part)

# #addition
# addition_result = complex_num1 + complex_num2
# print("Addition:", addition_result)

# subtraction_result = complex_num1 - complex_num2
# print("subtraction:", subtraction_result)

# multiplication_result = complex_num1 * complex_num2
# print("Multiplication:", multiplication_result)

# division_result = complex_num1 / complex_num2
# print("Division:", division_result)


#patterns
# (a)*
#    *  *
#    *  *  *
#    *  *  *  *
#    *  *  *  *  *
# num=5
# for i in range(0,num):
#         for j in range(0,i+1):
#                 print("*",end="")
#         print()
    # 1
    # 2  3
    # 4  5  6
    # 7  8  9  10





#  A
#     A  B
#     A  B  C
#     A  B  C  D

# for i in range(65,69):
#     for j in range(65,i+1):
#         print(chr(j),end=" ")
#     print()

#  21. Find Value of the following expressions
# num_1 = 10
# num_2 = 11
 
# print(num_1 % num_2)
# print(num_1 - num_2)
# print(num_1 * num_2)

# 22. Find the results of the following expressions (True or False)
# num_1=7
# num_2 = 6
 
# print(num_1 < num_2)
# print(num_1 > num_2)
# print(num_1 <= num_2)
# print(num_1 >= num_2)
# print(num_1==num_2)

   
# 23. Find the results of the following expressions (True or False)
# num_1=3
# num_2 = 4
 
# print((num_1 < num_2) and (num_1 != num_2))
# print((num_2 >= num_1) or (num_1 > num_2))
# print(not (num_1 == num_2))


# 24.  Output of the following while loop
# i=1
# while (i<6):
#     i = i +1
#     print(i) 
# 23456



# 25. Select the correct option
 
# customer_num =5
# invoice_num =1212
# print("Invoice No(s):")
# while(customer_num >0):
#      print("INV -", invoice_num)
#      invoice_num = invoice_num +3
#      customer_num = customer_num -1