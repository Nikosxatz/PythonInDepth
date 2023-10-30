try:
  onoma=input('Δώσε όνομα αρχείου :')
  f=open(onoma,'r')
  pl=sum=0
  for i in f:
      pl=pl+1
      ar=int(i)
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
  mo=sum/pl
except FileNotFoundError as e1:
  print('Το αρχειο που έδωσες δεν βρέθηκε')
except ValueError:
  print('Το αρχειο που έδωσες μάλλον δεν έχει ακέραιους αριθμούς έναν σε κάθε γραμμή')  
except ZeroDivisionError as e2:
  print('Το αρχειο που έδωσες δεν είναι άδειο')    
else:
  print('Πλήθος=',pl,' Μέση τιμή=',mo)
  print('Μέγιστος=',mx,' Ελάχιστος=',mn)

