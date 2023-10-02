import random
with open('randoms.txt','w',encoding='cp1253') as f:
    for i in range(100):
        r=random.randint(1,1000)
        f.write(str(r))
        f.write('\n')

    

    
