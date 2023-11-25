s='abcdefg123456789'
a=iter(s)
for i in range(4):
  a.__next__()
o=next(a,0)  
while o!=0:
  print(o)
  o=next(a,0) 


