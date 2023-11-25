def test(s):
    t=s(4,7)
    print(t)

test(lambda x,y:x*y)
test(lambda x,y:x+y)
test(lambda x,y:(x+y)/2)
f=lambda x,y:x**y
test(f)
