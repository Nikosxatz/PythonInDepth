# Τμήμα Α
for i in ('ΠΑΠΑ','ΧΑΤΖΗ','ΚΑΡΑ'):
    for j in ('ΓΙΑΝΝΗΣ','ΒΑΣΙΛΗΣ','ΝΙΚΟΛΑΣ','ΜΑΝΩΛΗΣ'):
        print(i+j,end=' ')
    print()
print('================================================')
# Τμήμα Β
for i in (1,10,2):
    for j in (5,10):
        print(i*j,end=' ')
    print()
print('================================================')
# Τμήμα Γ
for i in ((5,10),(100,200)):
    for j in ((1,10,2),(4,5),(7,8,9,2)):
        for k in i:
            for n in j:
                print(k*n,end=' ')
print()
print('================================================')
# Τμήμα Δ
for i in ('524'):
    for j in ('Python'):
        print(int(i)*j,end=' ')
    print()
print('================================================')














