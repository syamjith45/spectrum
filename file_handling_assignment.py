# # 1. Write a program to create a new file and write data to it ?
file_path = '/home/syam/Downloads/cars_sampled.csv'
# with open(file_path,'w') as file:
#     file.write("Hello WORLD\n")
#     file.write("this is created new file in python")
# print(f"Data has been written to {file_path}")

#2. Write a program to read data from a file ? (using read() and readline())?
# with open(file_path,'r')as file:
#     x=file.read()
#     c=file.readline()
#     while c:
#         print(c.strip())
#         c=file.readline()
#4 Write a program to perform read and write operation on a CSV File ?
# import csv
# with open(file_path,'w') as file:
#     writer=csv.writer(file)
#     writer.writerow(['SI','NAME','ADDRESS'])
#     writer.writerow(['1','SYAMJITH','POKKALAYIL'])
#     writer.writerow(['2','ssssss','ddddddd'])
# 3 import math
# b=10
# a=4
# c=2
# discr=(b**2 - 4*a*c)
# root1 = (-b + math.sqrt(discr))/2
# root2 = (-b - math.sqrt(discr))/2
# print(root1)
# print(root2)
