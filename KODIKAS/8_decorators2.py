def garnitoura(func):
    def inner():
        print('**********')
        func()
        print('##########')
    return inner

@garnitoura
def display():
    for i in range(5):
        print('Python decorators')

# Κυρίως πρόγραμμα
display()

