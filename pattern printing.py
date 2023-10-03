# a)*
#    *  *
#    *  *  *
#    *  *  *  *
#    *  *  *  *  *
# for i in range(6):

#     for j in range(i):

#         print("*",end=" ")
#     print()

#   b) # 1
#     2  3
#     4  5  6
#     7  8  9  10

# count=1
# for i in range(6):
#     for j in range(i):
#         print(count,end=" ")
#         count+=1
#     print()

#pyramid
for i in range(5):
    for j in range(5-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print(" # ",end=" ") 
    print()

