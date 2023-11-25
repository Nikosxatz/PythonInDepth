def compare(Lst):
    return sum(Lst)

# Κυρίως πρόγραμμα
a=[[9,2,3],[7,8],[1,2,3,4],[2,3]]
a.sort(reverse=True,key=compare)
print(a)




    



