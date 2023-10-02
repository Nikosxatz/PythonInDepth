def prosthiki(Lst,file):
    if not file.writable():
        return
    for i in Lst:
        file.write(str(i))
        file.write('\n')

    
f=open('randoms.txt','a')
new=[23,45,78,123,67,899]
prosthiki(new,f)
f.close()
