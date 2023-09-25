Lst=[2,9,6,7,8.5,3.5,5,7.5,3,2.5,9.5,10,8,6.5]
i=iter(Lst)
s=pl=0
o=next(i,'Τέλος')  
while o!='Τέλος':
  if o>=5:
    s=s+o
    pl=pl+1
  o=next(i,'Τέλος')  
print('MO=',s/pl)


