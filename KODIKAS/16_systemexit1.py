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
    print_sqrt(a)
