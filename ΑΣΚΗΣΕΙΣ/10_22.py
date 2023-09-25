s1='Η Λέσβος είναι ωραία'
s2='Λήμνος'
b1=bytearray(s1,'GREEK')
b2=s2.encode('GREEK')
for i in range(2,8):
    b1[i]=b2[i-2]
s3=b1.decode('GREEK')    
print(s3)

