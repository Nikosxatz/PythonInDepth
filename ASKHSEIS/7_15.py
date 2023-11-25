def bouncy(ar):
    ayxoysa=True
    fthinoysa=True
    s=str(ar)
    previous_digit=int(s[0])
    for i in s:
        y=int(i)
        if y<previous_digit:
            ayxoysa=False
        if y>previous_digit:
            fthinoysa=False    
        previous_digit=y
    if not (ayxoysa or fthinoysa):
       return True
    else:
        return False

# Κυρίως πρόγραμμα
plithos=0
for i in range(100,10000):
    if bouncy(i):
        plithos+=1
print(plithos)

