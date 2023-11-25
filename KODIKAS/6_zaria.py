import random
while True:
    z1=random.randint(1,6)
    z2=random.randint(1,6)
    ans=input('Πάτησε <Ernter> για μια ζαριά και κάτι άλλο για έξοδο!')
    if ans!='':
        break
    print('Η ζαριά σου: ',z1,'-',z2 )
print('Τέλος το μπαρμπούτι!')
