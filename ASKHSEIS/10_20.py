s='Νίκος'
b1=s.encode('UTF-8')
b2=s.encode('GREEK')
b3=s.encode('UTF-16')
s1=b1.decode('UTF-8')
s2=b2.decode('GREEK')
s3=b3.decode('UTF-16')
print(s1)
print(s2)
print(s3)
# b4=s.encode('ASCII') # Αν εκτελεστεί η πρόταση αυτή Θα υπάρξει μήνυμα λάθους
