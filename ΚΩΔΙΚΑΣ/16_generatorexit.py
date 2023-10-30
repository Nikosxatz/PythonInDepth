def my_generator():
    try:
        for i in range(5):
            yield i
    except GeneratorExit:
        print('Δεν χρησιμοποίησες όλες τις τιμές')

# Κυρίως πρόγραμμα
g = my_generator()
print(g.__next__())
print(g.__next__())
print(g.__next__())
g.close()

















