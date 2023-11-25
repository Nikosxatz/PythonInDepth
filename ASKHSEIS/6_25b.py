# «Πυθωνικός» τρόπος λύσης της άσκησης 6.25 με έναν μόνο βρόχο for
while True:
    gr=int(input('Δώσε το ύψος του δένδρου :'))
    if gr>=4 and gr<=20:
        break
    else:
        print('Η τιμή δεν είναι αποδεκτή, δώσε νέα τιμή')
for i in range(gr-2):
    print((gr-i)*' '+(2*i+1)*'*')
print(gr*' '+'*')	 








        











    
