def countmax(Lst,ar):
    c=0
    for i in Lst:
        if i>=ar:
            c=c+1
    return c

a=[11,7,15,6,2,34,23,12,45]
print(countmax(a,30))
