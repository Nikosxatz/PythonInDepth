s={2,5,6,2,4,7,2,6,9,6,5}
i=iter(s)
print(i.__next__())
print(i.__next__())
while True:
  item=next(i,'Τέλος')
  if item=='Τέλος':
    break
  else:
    print(item,end=' ')
      

