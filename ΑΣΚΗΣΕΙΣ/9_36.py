Lst=[1,2,3,4,5,6,7,8,9,10,11]
N=3
a=[Lst[i:i+N] for i in range(0,len(Lst),N)]
print(a)
