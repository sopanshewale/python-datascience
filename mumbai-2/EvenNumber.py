class EvenNumber(object):
   def __init__(self, low):
        if low % 2 != 0:
           self.current =  low + 1
        else: 
           self.current = low

   def __iter__(self):
        'Returns itself as an iterator object'
        return self

   def __next__(self):
        'Returns the next value till current is lower than high'
        self.current += 2
        return self.current - 2


