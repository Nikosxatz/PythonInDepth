b=bytearray(2)
print(len(b))
b[0]=65
b[1]=66
print(b)
b.extend(range(67,70))
print(len(b))
print(b)
b.insert(1,45)
print(b)
b.pop()
b.append(45)
print(b)
b.remove(45)
print(b)
b.reverse()
print(b)


         
