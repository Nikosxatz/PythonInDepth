hmera=int(input('Δώσε ημέρα:'))
minas=int(input('Δώσε μήνα:'))
if minas>2:
    s=(minas-1)*30-2+hmera
else:
    s=(minas-1)*30+hmera    
print('Είναι η',s,'μέρα του έτους')







