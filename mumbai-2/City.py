class City(object):
    def __init__(self, name, country, population):
          self.name = name
          self.country  = country
          self.population  = population
   
    def __repr__(self): 
        return "Name: %s , Country: %s , Population: %d\n"  % (self.name, self.country, self.population) 


