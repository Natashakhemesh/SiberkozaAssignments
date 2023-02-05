# Python has functions for creating, reading, updating, and deleting files.

#open a file 
myfile_nkh = open('myfile_nkh.txt', 'w') 

#get some informations 
print('name :', myfile_nkh.name)
print('is closed :', myfile_nkh.closed)
print('opening mode :', myfile_nkh.mode)

# write to file 
myfile_nkh.write ('I love python') 
myfile_nkh.write (' and javascript') 
myfile_nkh.close()

#append to file 
myfile_nkh = open('myfile_nkh.txt', 'a') 
myfile_nkh.write('I also like PHP')
myfile_nkh.close()

# read from a file 
myfile_nkh = open('myfile_nkh.txt', 'r+')
text_nkh = myfile_nkh.read(100)
print(text_nkh) 