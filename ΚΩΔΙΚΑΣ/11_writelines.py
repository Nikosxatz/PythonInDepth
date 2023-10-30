with open('ar.txt','w',encoding='utf-8') as out:
        lst=['Ένα','Δύο','Τρία']
        out.writelines(lst)
        out.write('\n----------\n')
        out.write('\n'.join(lst))
        out.write('\n----------\n')
        for i in range(len(lst)):
                lst[i]=lst[i]+'\n'
        out.writelines(lst)

