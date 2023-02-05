# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

#class 
class user_nkh : 
    #constructor
    def __init__(self, name,email,age) :
        self.name = name 
        self.email = email
        self.age = age 

    def greeting(self) :
     return f'my name is {self.name} & I am {self.age} '

    def has_birthday(self):
      self.age += 1

# extend class 
class customer(user_nkh):
    #constructor
    def __init__(self, name,email,age) :
        self.name = name 
        self.email = email
        self.age = age 
        self.balance = 0

    def set_balance(self,balance):
        self.balance = balance 

    def greeting(self) :
     return f'my name is {self.name}, I am {self.age} & my balance is {self.balance} '

#init user object 
natasha = user_nkh('natasha khemesh','natasha@gmail.com',19 )

#init customer object 
janet = customer('janet johnsn','janet@hotmail.com',24 )

janet.set_balance(1000)
print(janet.greeting())
print(type(natasha))
print(natasha.has_birthday())
print(natasha.greeting()) 




