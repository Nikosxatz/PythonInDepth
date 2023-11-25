def fibonacci(oros):
    if oros==0:
        return 0
    elif oros==1:
        return 1
    else:  
        return fibonacci(oros-1)+fibonacci(oros-2)

# Κυρίως πρόγραμμα
for i in range(12):
    print(fibonacci(i))























