d1={'ct18022':'Μηχαήλ','ct22099':'Χρύσα','ct22001':'Νίκος'}
print(d1.get('ct20099'))
d1.update({'ct21011':'Φωτεινή'})
for on in d1.values():
    print(on)
print(d1.pop('ct22001'))
s1={'ct22002','ct21089','ct19099'}
d2=dict.fromkeys(s1,'Ανώνυμος')
print(d2)
d1.update(d2)
for k in d1.keys():
    if 'ct22' in k:
        print(d1.get(k))



    

