# while True:
#     try:
#         a=int(input("enter the first number:"))
#         b=int(input("enter the second number:"))

#         print("What kind of operation do you want to perform.\nPress + for Addition\nPress - for substraction.\nPress * for multiplication.\nPress / for divison")

#         o=input(("Enter operation:"))
#         match o:
#             case "+":
#                 print(f"The result is {a+b}")
#             case "-":
#                 print(f"The result is {a-b}")
#             case "*":
#                 print(f"The result is {a*b}")
#             case "/":
#                 print(f"The result is {a+b}")
#             case default:
#                 print(f"There was an error")
#     except Exception as e:
#         print("Enter a valid value of a and b")
    
#     choice=input("Do you want to continue or not (Yes/no):")
#     if choice.lower()=="no":
#         break
    


import numpy as np

mat=np.array([{1,2,3},{4,5,6},{7,8,9}])
print(mat)