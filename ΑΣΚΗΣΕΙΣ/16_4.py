while True:
  try:
    frasi=input('Δώσε φράση :')
    b=int(input('Δώσε Νο χαρακτήρα :'))
    print(frasi[b])
  except ValueError as e1:
    print('Μάλλον κάτι έδωσες λάθος:')  
  except IndexError:
    print('Είσαι σίγουρος για το Νο;')
  except:
    print('Κάτι πήγε στραβά!!!')
  else:
    break
