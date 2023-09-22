Lst=['Χίος','Λέσβος','Λήμνος']
plith=[44467,102345,18345]
therm=[5.5,-4.5,9.5]
for i in Lst:
  print('{:^10}'.format(i),end='')
print()
for i in plith:
  print('{:,} '.format(i),end='')
print()   
for i in plith:
  print('{:b} {:x} {:o}'.format(i,i,i))
for i in therm:
  print('{:+} '.format(i),end='')


