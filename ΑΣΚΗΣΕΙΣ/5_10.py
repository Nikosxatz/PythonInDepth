kafedes=int(input('Δώσε αριθμό καφέδων:'))
resta=500-kafedes*70
if resta<0: 
    print('Δεν φτάνουν τα χρήματα για τόσους καφέδες')
else:
    ker_2=resta//200
    resta=resta%200
    ker_1=resta//100
    resta=resta%100
    ker_50=resta//50
    resta=resta%50
    ker_20=resta//20
    resta=resta%20
    ker_10=resta//10
    resta=resta%10
    print('Ρέστα')
    if ker_2>0:
        print('Κέρματα 2E :',ker_2)
    if ker_1>0:
        print('Κέρματα 1E :',ker_1)
    if ker_50>0:
        print('Κέρματα 50Λ :',ker_50)
    if ker_20>0:
        print('Κέρματα 20Λ :',ker_20)
    if ker_10>0:
        print('Κέρματα 10Λ :',ker_10)










