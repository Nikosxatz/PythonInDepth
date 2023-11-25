class Lathos(Exception):
        pass
while True:
        try:
                ans=input('Τι κάνει νιάου νιάου στα κεραμίδια;')
                if ans!='γάτα':
                        raise Lathos('.. για ξαναπροσπάθησε')
        except Lathos as e1:
                print('Πλάκα μας κάνεις!!!',e1)
        else:
                break
print('Επιτέλους...')
