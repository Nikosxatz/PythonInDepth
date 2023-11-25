def type_check(f):
        def inner(a,b):
                if type(a)!= int or type(b)!=str:
                      print('Λάθος τύπος ορισμάτων κλήσης')
                      return None
                else:
                      return f(a,b)
        return inner

@type_check
def multi(x:int,y:str)->str:
	return x*y

# Κυρίως πρόγραμμα
r=multi(5,2)
print(r)
r=multi(3,'Python')
print(r)
