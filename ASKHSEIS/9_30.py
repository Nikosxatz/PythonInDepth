def compare(t):
    return sum(t)

# Κυρίως πρόγραμμα
a=[(2,3,4),(2,3),(4,5,1),(6,5),(9,2)]  
a.sort(reverse=True,key=compare)
print(a)




    



