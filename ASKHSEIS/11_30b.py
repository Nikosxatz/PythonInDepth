with open('bin_out','rb') as fin:
    b=fin.read()
    Lst=b.split(b'\xff')
    for onom in Lst:
        print(onom.decode('utf-8'))


