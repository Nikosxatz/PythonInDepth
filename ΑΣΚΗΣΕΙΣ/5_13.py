fot=int(input('Δώσε πλήθος φωτοτυπιών :'))
if fot<=5:
    poso=fot*1
elif fot<=50:
    poso=5*1+(fot-5)*1.5
elif fot<=150:
    poso=5*1+45*1.5+(fot-50)*2
else:
    poso=5*1+45*1.5+100*2+(fot-150)*4
print('Συνολικό ποσό σε ευρώ:',poso/100)  













