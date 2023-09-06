frasi=input('Δώσε μια φράση:')
frasi=frasi.replace(' ','')
if frasi==frasi[::-1]:
    print('Η φράση είναι παλύνδρομο')
else:
    print('Η φράση δεν είναι παλύνδρομο')
    
