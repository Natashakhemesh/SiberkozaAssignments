# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""
# simple normalization 

#x.nkh = 5            # int
#name_ = 'nour'    # string 
# y.kh = 5.5          # float 
#is_nkh = True      # boolean 


# muliple assignment

x_nkh , name_nkh , y_nkh, is_nkh = (7 ,'Natasha', 4.5 , True)

print("x_nkh") 

# basic math
z_nkh = x_nkh + y_nkh 

#casting

x_nkh = str(x_nkh)
y_nkh = int(y_nkh)

#it will print the new type of x_nkh 

print(type(x_nkh)) 



