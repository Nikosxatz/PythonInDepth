'''
    Μελετήστε 
    α.) την παράγραφο 8.2 Συναρτήσεις µε µεταβλητό πλήθος ορισµάτων
    β.) την παράγραφο 8.9 Συναρτήσεις γεννήτριες και το παράδειγμα Π8.7
    γ.) την παράγραφο 9.3 πολυδιάστατες λίστες
    δ.) την παράγραφο 9.4 μεταβίβαση λιστών σε συναρτήσεις
    ε.) την παράγραφο 9.11 συμπερίληψη λίστας 
'''
import random
def create_2d_array_alfa(grammes,stiles,begin,end):
    a=[[ random.randint(begin,end) for i in range(stiles)] for j in range(grammes)]  
    return a
def create_2d_array_beta(grammes,stiles,fun,*args):
    a=[[ fun(*args) for i in range(stiles)] for j in range(grammes)]  
    return a
def create_2d_array_charly(grammes,stiles,fun,*args):   
    f=fun()
    a=[[ next(f) for i in range(stiles)] for j in range(grammes) ]  
    return a
def f1():
    return random.randint(1,100)
def f2():
    return 88
def f3(): #fibonacci_numbers 8_p8_7.py 
    fu1=0
    yield fu1  
    fu2=1
    yield fu2  
    while True:
        fu3=fu1+fu2
        yield fu3        
        fu1=fu2
        fu2=fu3  
def f4(x):     
        ar=int(input('δώσε αριθμό για ύψωση στην {} : '.format(x)))
        return ar**x
# Συνάρτηση για τις εκτυπώσεις πινάκων και μηνυμάτων
def printit(list,msg,lines,column):
    print(msg.format(lines,column))
    for element in list:
        print(element)
    print()
# Κυρίως πρόγραµµα
lines=3
column=4
msg=[
    '',
    '1. Δημιουργία ΚΕΝΟΥ πίνακα {} x {} με list comprehension',
    '2. Δημιουργία πίνακα {} x {} με ΤΥΧΑΙΟΥΣ αριθμούς με list comprehension',
    '3. Δημιουργία πίνακα {} x {} με ΤΥΧΑΙΟΥΣ αριθμούς μέσω μεταβίβασης συνάρτησης με list comprehension',
    '4. Δημιουργία πίνακα {} x {} με ΣΤΑΘΕΡΟ αριθμό μέσω μεταβίβασης συνάρτησης με list comprehension',
    '5. Δημιουργία πίνακα {} x {} με χρήση generator object σε συνδιασμό με list comprehension',
    '6. Δημιουργία πίνακα {} x {} με ΠΛΗΚΤΡΟΛΟΓΙΣΗ αριθμών μέσω παραμετρικής συνάρτησης με list comprehension'    
    ]
# Κενός πίνακας
list_a=[[list() for i in range(column)]for j in range(lines)]
printit(list_a,msg[1],lines,column)

# Πίνακας με τυχαίους αριθμούς
random.seed(1)
list_b=create_2d_array_alfa(lines,column,1,100) 
printit(list_b,msg[2],lines,column)

# Πίνακας με τυχαίους αριθμούς μέσω μεταβίβασης συνάρτησης
random.seed(1)
list_c=create_2d_array_beta(lines,column,f1) 
printit(list_c,msg[3],lines,column)

# Πίνακας σταθερό αριθμό μέσω μεταβίβασης συνάρτησης
list_d=create_2d_array_beta(lines,column,f2) 
printit(list_d,msg[4],lines,column)

# Πίνακας με χρήση generator object
x=2
list_d=create_2d_array_charly(lines,column,f3) 
printit(list_d,msg[5],lines,column)

# με ΠΛΗΚΤΡΟΛΟΓΙΣΗ αριθμών μέσω παραμετρικής συνάρτησης
list_d=create_2d_array_beta(lines,column,f4,x) 
printit(list_d,msg[6],lines,column)