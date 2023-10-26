try:
  frasi=input('Δώσε φράση :')
  if len(frasi)>40:
    raise ValueError('Πολύ μέγάλη φράση')
  b=int(input('Δώσε Νο χαρακτήρα :'))
  print(frasi[b])
except ValueError as e1:
  print('Μάλλον κάτι έδωσες λάθος:')  
  print(e1)  
except IndexError:
  print('Είσαι σίγουρος για το Νο;')
except:
  print('Κάτι πήγε στραβά!!!')
