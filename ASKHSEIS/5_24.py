import sys
pr={'22510':'Μυτιλήνη','22710':'Χίος','22730':'Σάμος','22410':'Ρόδος','2310':'Θεσσαλονίκη','210':'Αθήνα'} 
til=input('Δώσε ένα τηλέφωνο:')
if len(til)!=10:
    print('Λάθος αριθμός')
    sys.exit()
if til[0:5] in pr:
    print(pr[til[0:5]])
elif til[0:4] in pr:
    print(pr[til[0:4]])
elif til[0:3] in pr:
    print(pr[til[0:3]])   
else:
    print('Άγνωστη περιοχή')


	














