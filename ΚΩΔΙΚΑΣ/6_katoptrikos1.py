import sys
ar=int(input('Δώσε τετραψήφιο αριθμό:'))
if not (ar>=1000 and ar<=9999):
    print('Δεν έδωσες τετραψήφιο!!!')
    sys.exit()
y1=ar%10
y2=(ar//10)%10
y3=(ar//100)%10
y4=(ar//1000)%10
k=y1*1000+y2*100+y3*10+y4
print('Ο κατοπτρικός του {} είναι {}'.format(ar,k))
















