while True:
  onoma=input('Δώσε όνομα αρχείου :')
  try:
    f=open(onoma,'r')
  except FileNotFoundError:
    print('Το αρχειο που έδωσες δεν βρέθηκε ... δώσε άλλο')
  else:
    break
pl=sum=0
for i in f:
  try:
    ar=int(i)
  except ValueError:
    continue
  pl=pl+1
  if pl==1:
    mn=ar
    mx=ar
  else:
    if ar>mx:
      mx=ar
    elif ar<mn:
      mn=ar
  sum=sum+ar
f.close()
try:
  mo=sum/pl
except ZeroDivisionError:
  print('Το αρχειο που έδωσες δεν έχει κανέναν ακέραιο αριθμό')  
else:
  print('Πλήθος=',pl,' Μέση τιμή=',mo)
  print('Μέγιστος=',mx,' Ελάχιστος=',mn)

