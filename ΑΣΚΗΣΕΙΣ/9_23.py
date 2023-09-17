def tax(Lst):
    ayxoysa=True
    fthinousa=True
    for i in range(1,len(Lst)):
        if Lst[i]<Lst[i-1]:
            ayxoysa=False
        elif Lst[i]>Lst[i-1]:
            fthinousa=False
    if ayxoysa and fthinousa:
        return 3
    elif fthinousa:
        return 2    
    elif ayxoysa:
        return 1
    else:
        return 0

# Κυρίως πρόγραμμα
test=[8,3,2,1]
print(tax(test))
test=[8,13,22,31]
print(tax(test))
test=[8,3,12,4]
print(tax(test))
test=[8,8,8,8]
print(tax(test))

