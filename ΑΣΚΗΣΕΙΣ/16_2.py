try:
  frasi=input('Δώσε φράση :')
  b=int(input('Δώσε No χαρακτήρα :'))
  print(frasi[b])
except ValueError as e1:
  print('Μάλλον κάτι έδωσες λάθος:')  
  print(e1)  
except IndexError:
  print('Είσαι σίγουρος για το No ;')
except:
  print('Κάτι πήγε στραβά!!!')
