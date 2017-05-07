class Person(object):
    def __init__(self, name, age):
          self.name = name
          self.age  = age
   
    def __repr__(self): 
        return "Name: %s , Age: %d \n"  % (self.name, self.age) 


