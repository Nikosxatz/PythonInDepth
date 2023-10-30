ar=int(input("Δώσε έναν ακέραιο αριθμό:"))
gin=1
if ar==0: print(gin*ar)
while ar>0:
    y=ar%10
    gin=gin*y
    ar=ar//10
print('Γινόμενο ψηφίων:',gin)















