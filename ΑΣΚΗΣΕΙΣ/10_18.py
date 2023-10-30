b=bytearray(b'ABCD1234')
b.insert(0,ord('-'))
b.append(ord('-'))
b.insert(5,ord('*'))
print(b)
b.extend(range(200,221))
print(b)
i=0
while True:
    while b[i]%2==0:
        b.pop(i)
        if i>=len(b):
            break
    i=i+1
    if i>len(b):
        break
b.extend(int.to_bytes(1000000,4,'big'))
for i in b:
    print(i)         
print(int.from_bytes(b[:3],'big'))
