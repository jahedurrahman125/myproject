def all_the_same(elements):
   if len(elements) < 1:
       return True
   return len(elements) == elements.count(elements[0])

all_the_same([42, 42, 42])