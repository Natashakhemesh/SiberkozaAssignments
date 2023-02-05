# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods
name_nkh = "natasha"
age_nm = 19 

#concatenate 

#print('my name_nkh is'+ name_nkh + 'and I am ' + str(age_nkh))

# String Formatting

# Arguments by positions 

#print('my name is {name_nkh} and I am {age_nkh}'.format(name_nkh = name_nkh, age_nkh = age_nkh)) 

# String Methods
s_nkh = 'hello all ' 

#capitalize string 

print(s_nkh.capitalize())

# make all uppercase 
print(s_nkh.upper())

# make all lowercase 
print(s_nkh.lower())

# swap case 
print(s_nkh.swapcase())

# get lenght 
print(len(s_nkh))

# replace 
print(s_nkh.replace('all','world'))

#count 
sub = 'h'
print(s_nkh.count(sub)) 

#starts with 
print(s_nkh.startswith('hello'))

#ends with 
print(s_nkh.endswith('l'))

#split into a list 
print(s_nkh.split())

#find position
print(s_nkh.find('a'))

#is all alphanumeric
print(s_nkh.isalpha())

#is all numeric 
print(s_nkh.isnumeric())

