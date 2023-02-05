# If/ Else conditions are used to decide to do something based on something being true or false

x_nkh  = 21
y_nkh = 20

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values
#simple if 
#elif 
#if-else
'''
if x_nkh > y_nkh :
    print(f"{x_nkh }is greater than {y_nkh}") 

elif x_nkh==y_nkh : 
      print(f"{x_nkh} is equal than {y_nkh} ")

else : 
      print(f"{y_nkh} is greater or equal than {x_nkh}")
'''

#nested if  

'''
if x_nkh > 2 :
    if x_nkh <= 10 :
        print(f'{x_nkh} is greater than 2 and less than or equal to 10 ')
'''

# Logical operators (and, or, not) - Used to combine conditional statements >> we will get the same outp of the previous line (nested if)

# and

if x_nkh > 2 and x_nkh <= 10 : 
     print(f'{x_nkh} is greater than 2 and less than or equal to 10 ')

# or

if x_nkh > 2 or x_nkh <= 10 : 
     print(f'{x_nkh} is greater than 2 and less than or equal to 10 ')

# not

if not (x_nkh==y_nkh): 
     print(f'{x_nkh} is not equal to {y_nkh} ')





# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object

# in 
num_nkh =[1,2,3,4,5]
if x_nkh in num_nkh:
    print(x_nkh in num_nkh) 

# not in 
num_nkh =[1,2,3,4,5]
if x_nkh not in num_nkh:
    print(x_nkh not in num_nkh) 

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# is 
if x_nkh is y_nkh : 
    print(x_nkh is y_nkh )

# is not
if x_nkh is not y_nkh : 
    print(x_nkh is not y_nkh )  
