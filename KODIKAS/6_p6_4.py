ayxoysa=True
ar=int(input('Δώσε έναν ακέραιο αριθμό:'))
s=str(ar)
previous_digit=int(s[0])
for i in s:
    y=int(i)
    if y<previous_digit:
        ayxoysa=False
    previous_digit=y
if ayxoysa:
    print('Ναι, τα στοιχεία του αριθμού είναι σε αύξουσα σειρά')
else:
    print('Τα στοιχεία του αριθμού δεν είναι σε αύξουσα σειρά')


