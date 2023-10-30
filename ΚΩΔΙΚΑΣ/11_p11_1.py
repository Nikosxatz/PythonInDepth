f=open('lexeis.txt','w',encoding='iso-8859-7')
while True:
    lex=input('Δώσε λέξη:')
    if lex=='':
        break
    f.write(lex)
    f.write('\n')
f.close()
