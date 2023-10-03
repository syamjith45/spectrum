#  Define a class which has at least two methods one, to get a string from console  input and other is to print the string in uppercase.
# class Greet():
#     def __init__(self,string):
#         self.string=string
#         pass
#     def put(self):
#         self.string=input("enter a string :")

#     def up(self):
#         print(self.string.upper())

# greet=Greet(" ")
# greet.put()
# greet.up()

#  Define a class named Circle which can be constructed by radius. The Circle class has a method which can compute the area.
# class Cricle():
     
#      def __init__(self,radius):
#          self.radius=radius
#      def area(self):
#          self.area=3.14*(self.radius*self.radius)
#          return self.area
# circle=Cricle(6)
# result=circle.area()
# print(result)

#Define a class, which have a class parameter and have a same instance parameter.
# class MyClass:
#     # Class parameter
#     class_param = "I am a class parameter"

#     def __init__(self, instance_param):
#         # Instance parameter
#         self.instance_param = instance_param

# # Creating instances of MyClass
# obj1 = MyClass("Instance 1")
# obj2 = MyClass("Instance 2")

# # Accessing class and instance parameters
# print("Class Parameter:", MyClass.class_param)
# print("Instance 1 Parameter:", obj1.instance_param)
# print("Instance 2 Parameter:", obj2.instance_param)

# Define a class named BankAccount. This class should contain methods withdraw() and deposit to calculate the balance amount remained in your account.
# class BankAccount():
#     def __init__(self,intial_balance=0):
#         self.balance=intial_balance
#         pass
#     def deposit(self,amount):
#         if amount>0:
#             self.balance+=amount
#             print("deposited amount is {} the new balance is {} ".format(amount,self.balance))
#             pass
#         pass
#     def withdraw(self,amount):
#         if amount>0:
#             if amount <=self.balance:
#                 self.balance-=amount
#                 print("withdrew is {} the new balance is {}".format(amount,self.balance))
#                 pass
# account = BankAccount(100000)
# account.deposit(50000)
# account.withdraw(40000)

    



#Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.


class Shape():
    def __init__(self) -> None:
        pass
    pass

        
class Square(Shape):

    def __init__(self,length) -> None:
        super().__init__()
        self.length=length
    def area(self):
        return self.length**2
square=Square(5)

result=square.area()
print(result)


