with open('glossa.txt','r',encoding='utf-8') as f:
    s=f.read()
    all={}
    for ch in s:
        cnt=all.setdefault(ch,0)
        all.update({ch:cnt+1})
    L=list(all.items())
    L.sort()
    for i in L:
        if (i[0].isprintable()):
            print(i[0],i[1])

