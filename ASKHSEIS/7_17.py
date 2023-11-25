def palindromos1(num):
    arxikos=num
    s=0
    if num<=9: return True
    while True:
        digit=num%10
        s=(s*10)+digit
        num=num//10
        if num==0: break
    if s==arxikos:
        return True
    else:
        return False

def palindromos2(num):
	return str(num)==str(num)[::-1]
	
# Κυρίως πρόγραμμα
ar=int(input('Δώσε αριθμό:'))
if palindromos1(ar):
    print('Ο ',ar,'είναι παλίνδρομος - από κλασικό τρόπο')
else:
    print('Ο ',ar,'ΔΕΝ είναι παλίνδρομος - από κλασικό τρόπο')
if palindromos2(ar):
    print('Ο ',ar,'είναι παλίνδρομος - από «πυθωνικό» τρόπο')
else:
    print('Ο ',ar,'ΔΕΝ είναι παλίνδρομος - από «πυθωνικό» τρόπο')
