with open('bin_1000','rb') as f:
    f.seek(12)
    print(f.tell())
    f.seek(-3,1)
    print(f.tell())
    f.seek(8,1)
    print(f.tell())
    f.seek(-20,2)
    print(f.tell())
    f.seek(20,2)
    print(f.tell())



