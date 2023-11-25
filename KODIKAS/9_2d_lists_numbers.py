import random
epipedo1=[]
for i in range(3):
    epipedo2=[]
    for j in range(4):
        epipedo2.append(random.randint(1,100))
    epipedo1.append(epipedo2)
    print(epipedo2)
print(epipedo1)
