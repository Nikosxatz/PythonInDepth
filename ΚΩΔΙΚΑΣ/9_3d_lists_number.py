import random
epipedo1=[]
for i in range(4):
    epipedo2=[]
    for j in range(3):
        epipedo3=[]
        for k in range(2):
            epipedo3.append(random.randint(1,10))
        epipedo2.append(epipedo3)
    epipedo1.append(epipedo2)       
print(epipedo1)
