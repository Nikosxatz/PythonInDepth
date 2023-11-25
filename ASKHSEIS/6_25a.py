while True:
    gr=int(input('Δώσε το ύψος του δένδρου :'))
    if gr>=4 and gr<=20:
        break
    else:
        print('Η τιμή δεν είναι αποδεκτή, δώσε νέα τιμή')
for i in range(gr-2):
    for j in range(gr-2-i):
        print(' ',end='')
    for j in range(i*2+1):
        print('*',end='')
    print()
for j in range(gr-2):
    print(' ',end='')	 
print('*')





        











    
