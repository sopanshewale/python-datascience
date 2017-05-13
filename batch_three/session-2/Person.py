class Person(object):
    def __init__(self, name, age):
          self.name = name
          self.age  = age
   
    def __repr__(self): 
        return "NAME: %s , AGE: %d \n"  % (self.name, self.age) 

    def sayAge(self):
        return self.age

