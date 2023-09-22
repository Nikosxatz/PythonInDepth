Lst=['Χίος','Λέσβος','Λήμνος']
plith=[44467,102345,18345]
therm=[5.5,-4.5,9.5]
for i in Lst:
  print(f'{i:^10}',end='')
print()
for i in plith:
  print(f'{i:,} ',end='')
print()   
for i in plith:
  print(f'{i:b} {i:x} {i:o}')
for i in therm:
  print(f'{i:+} ',end='')


