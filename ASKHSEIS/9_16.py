a=[[5,8,9,4,2,1],[1,6,5],[4,3,0,3,5]]
s=0
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j]%3==0:
            s=s+a[i][j]
print(s)



    



