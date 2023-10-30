c=[[[5,8],[4,2],[9,10]],[[2,3],[7,6],[4,9]],[[2,10],[3,1],[0,4]]]
s=0
for i in c:
    for j in i:
        for k in j:
            s=s+k
print(s)
