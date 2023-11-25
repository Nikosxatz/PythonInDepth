import sys
import math
def print_sqrt(ar):
    if ar>1000:
        sys.exit()
    else:
        tr=math.sqrt(ar)
        print('Η τετραγωνική ρίζα είναι:',tr)
        
# Κυρίως πρόγραμμα
for i in range(10):
    a=int(input('Δώσε αριθμό:'))
    try:
        print_sqrt(a)
    except SystemExit:
        print('Όχι δεν σταματώ!!!')
    except ValueError:
        print('Όχι αρνητικό παρακαλώ!')
