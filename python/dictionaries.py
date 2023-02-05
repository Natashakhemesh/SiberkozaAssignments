# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

#creat dic 
person_nkh ={
    "first_name":"joe",
    "last_name":"malak",
    "age":18
}
print(person_nkh,type(person_nkh)) 

#use a constructor 
#person_nkh1=dict(first_name="samer",last_name="waed")
#print(person_nkh1,type(person_nkh1))

#get value 
print(person_nkh["first_name"])
print(person_nkh.get("last_name"))

#add value 
person_nkh['phone']= '100-100-1000'
print(person_nkh)

#get dic keys 
print(person_nkh.keys())

#get dic items
print(person_nkh.items())

#copy dic 
person_nkh1=person_nkh.copy()
person_nkh1['city']='Ramallah'
print(person_nkh1)

#remove an item > two ways 
del(person_nkh["age"])
person_nkh.pop('phone')
print(person_nkh)

#clear a dic
person_nkh.clear()
print(person_nkh)

#get lenght 
print(len(person_nkh1))

# list of dic 
people = [
    {"name":"mary","age":20},
    {"name":"losy","age":15} 
    ]
print(people)
print(people[0]["name"])




# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries
