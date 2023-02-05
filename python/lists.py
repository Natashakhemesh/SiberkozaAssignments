# A List is a collection which is ordered and changeable. Allows duplicate members.

#creat a list 

num_nkh= [1,2,3,4,5]
fruits_nkh = ['apple','banana','grapes','berry']

#use a constructor

#num_nkh1 = list((1,2,3,4,5))
#print(num_nkh , num_nkh1)

#get a value 
print(fruits_nkh[1])

#get lenght 
print(len(fruits_nkh))

#append to list 
fruits_nkh.append('pears')
print(fruits_nkh)

#remove from a list 
fruits_nkh.remove('banana')
print(fruits_nkh)

#insert into position 

fruits_nkh.insert(3,'strawberry')
print(fruits_nkh)

#remove with pop 
fruits_nkh.pop(2)

#reverse list 
fruits_nkh.reverse() 
print(fruits_nkh) 

#sort list 
fruits_nkh.sort()

#reverse sort 
fruits_nkh.sort(reverse=True)

#change values 
fruits_nkh[1]='orange'





 