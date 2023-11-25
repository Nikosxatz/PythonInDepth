ar=0
while not (ar>=1000 and ar<=9999):
    ar=int(input('Δώσε τετραψήφιο αριθμό:'))
    if not (ar>=1000 and ar<=9999):
        print('Δεν έδωσες τετραψήφιο, παρακαλώ να τον ξαναδώσεις')
for i in range(1,5):
    y=(ar//10**(i-1))%10
    print(y)
    pass














