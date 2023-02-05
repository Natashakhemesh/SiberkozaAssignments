# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people_nkh = ['moath','ali','lara','halim']

#simple for loop 
'''
for person_nkh in people_nkh :
    print(f'current person_nkh : {person_nkh }')
'''
#break
'''
for person_nkh in people_nkh :
    if person_nkh == 'sara':
     break
    print(f'current person_nkh: {person_nkh }')
'''
# continue

for person_nkh in people_nkh :
    if person_nkh == 'sara':
     continue
    print(f'current person_nkh: {person_nkh }')

# range >> same as the previous but in another way  
"""
for i in range(len(people_nkh)) : 
    print(people_nkh[i])

for i in range(0,10):
    print(f'number:{i} ')    
"""

# While loops execute a set of statements as long as a condition is true.

count_nkh = 0 
while count_nkh <= 10 :
    print(f'count_nkh :{count_nkh} ')
    count_nkh += 1 
    