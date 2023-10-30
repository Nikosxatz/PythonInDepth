with open('file3a.txt','r',encoding='utf-8') as f:
        grammes=0
        pl=0
        for line in f:
                pl=pl+1
                print(pl,'-',line,end='')
        print()
        print('=================')
        print('Σύνολο γραμμών:',pl)
print(f.closed)

