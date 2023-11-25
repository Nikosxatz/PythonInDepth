import random
def plithos(Lst):
    pl=0
    for i in Lst:
        nai=0
        oxi=0
        for j in i:
            if j=='Ν':
                nai=nai+1
            elif j=='Ο':
                oxi=oxi+1
        if nai>oxi:
            pl=pl+1
    return pl
    
# Κυρίως πρόγραμμα
apantiseis=[['Ν', 'Ο', 'Δ'], ['Δ', 'Ο', 'Δ'], ['Ο', 'Ο', 'Ο'], ['Ν', 'Δ', 'Δ'], ['Ν', 'Δ', 'Ν']]
print(plithos(apantiseis))
