def mesos(*bath):
    s=0
    for i in bath:
        s=s+i
    if len(bath)==0:
        return None
    else:
        return s/len(bath)

# Κυρίως πρόγραμμα
print(mesos(6,7,8))			
print(mesos(9.5,6,7,8,4,5))
print(mesos())









