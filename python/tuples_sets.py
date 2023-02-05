# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
#creat tuple 
fruits_nkh = ("apple","orange","grapes")
#fruits_nkh1 = tuple(("apple","orange","grapes"))
#print(fruits_nkh ,fruits_nkh1)

fruits_nkh2 = ("apple")
print(fruits_nkh2,type(fruits_nkh2))

#get value 
print(fruits_nkh[2])


#delete a tuple 

del fruits_nkh2 
# print(fruits_nkh2)

# get length 
print(len(fruits_nkh))





# A Set is a collection which is unordered and unindexed. No duplicate members.

fruit_setnkh ={"apple","orange","grapes"}

#check if an item is in th set 
print("apple"in fruit_setnkh)

#add to set 
fruit_setnkh.add("grape")
#print(fruit_setnkh)

#remove from a set 
fruit_setnkh.remove("grape")

#clear set 
fruit_setnkh.clear()
print(fruit_setnkh)

#delete a set 
del fruit_setnkh 
print(fruit_setnkh)



# we can't insert any item that already there like this >> add duplicate : fruit_setnkh.add("apple")