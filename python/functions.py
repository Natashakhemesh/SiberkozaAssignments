# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# creat a fun 
def sayHello(name):
    print(f"Hello {name}")
    sayHello("mohammed") 


# return values 
def getSum(num1,num2):
 total = num1+num2
 return total 
print(getSum(2,5))   
num = getSum(6,5)
print(num)


# A lambda function is a small anonymous function.

getSum = lambda num1, num2 : num1 + num2
print(getSum(5,4))  



# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

