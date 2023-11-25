s=int(input('Δώσε το πλήθος των Sms:'))
if s<=50:
    poso=0
elif s<150:
    poso=(s-50)*1.2
elif s<350:
    poso=100*1.2+(s-150)*0.8
else:
    poso=100*1.2+200*0.8+(s-350)*0.5
print('Η χρέωση των',s,'SMS είναι',poso,'ευρώ')





