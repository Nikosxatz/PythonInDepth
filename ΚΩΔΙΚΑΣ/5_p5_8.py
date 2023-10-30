NomosLesvou=('Λέσβος','Λήμνος','Άγιος Ευστράτιος')
NomosXiou=('Χίος','Ψαρά','Οινούσσες')
NomosSamou=('Σάμος','Ικαρία','Φούρνοι')
Nisi=input('Δώσε το όνομα ενός νησιού:')
if Nisi in NomosLesvou:
    print('To νησί ανήκει στον νομό Λέσβου')
elif Nisi in NomosXiou:
    print('To νησί ανήκει στον νομό Χίου')
elif Nisi in NomosSamou:
    print('To νησί ανήκει στον νομό Σάμου')
else:
    print('Το νησί δεν βρίσκεται στην Περιφέρεια Β. Αιγαίου')





