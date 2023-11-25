def calc(ch,a,b):
    if ch=='+':
        return a+b
    elif ch=='*':
        return a*b
    elif ch=='#':
        return (a+b)/2
    else:
        print('Αντικανονική κλήση συνάρτησης')
    
# Kυρίως πρόγραμμα
print(calc('+',5,7))
print(calc('*',5,7))
print(calc('#',5,7))
print(calc('A',5,7))     



 
