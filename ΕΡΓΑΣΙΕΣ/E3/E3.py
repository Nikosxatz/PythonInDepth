def towers(num,stylos_apo,stylos_se,stylos_temp):
    if num==1:
        print('Μετακίνησε τον δίσκο 1 από τον στύλο ',stylos_apo,' στον στύλο ', stylos_se)
        return
    # Αναδρομική κλήση της συνάρτησης
    towers(num-1, stylos_apo, stylos_temp, stylos_se)
    print('Μετακίνησε τον δίσκο',num,'από τον στύλο ',stylos_apo, ' στον στύλο ',stylos_se)
    # Αναδρομική κλήση της συνάρτησης
    towers(num-1, stylos_temp, stylos_se, stylos_apo)

# Κυρίως πρόγραμμα
n=int(input('Δώσε αριθμό δίσκων :'))
print('Η σειρά των απαιτούμενων κινήσεων είναι:')
towers(n, 'Α', 'Γ', 'Β')
