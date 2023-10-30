"""
    Πληροφορίες για τον υπολογιστή σας και την Python με τα αρθρώματα sys και platform.
        https://docs.python.org/3/library/sys.html
        https://docs.python.org/3/library/platform.html
    Ταξινόμηση σε λεξικό.
    Χρήση μορφοποιημένων συμβολοσειρών (formated strings , f-strings)
        Εισαγωγή χαρακτήρα {  μέσα σε f-string.
"""
import sys
import platform

print(f"Α. Το λειτουργικό σας σύστημα είναι: {platform.platform()}")
print(f"B. Ο επεξεργαστής του υπολογιστή σας είναι: {platform.processor()}")
print(f"Γ. Η έκδοση της Python είναι: {sys.version}")
print(
    f"Δ. H υλοποίηση της Python (python implementation) είναι: {platform.python_implementation()}"
)
# https://wiki.python.org/moin/PythonImplementations
print(f"Ε. Η διαδρομή του Python Interpreter είναι: {sys.executable}")
input(
    f"ΣΤ. Εισηγμένα αρθρώματα (imported modules) της Python. Πατήστε Enter:"
)
modules_dic = sys.modules
list_of_keys = list(
    modules_dic.keys()
)  # με σκοπό την ταξινόμηση του λεξικού modules.dic
list_of_keys.sort()  # ταξινόμηση της λίστας με τα κλειδιά του λεξικού
sorted_modules_dic = {
    i: modules_dic[i] for i in list_of_keys
}  # Δημιουργία νέου ταξινομημένου λεξικού
i = 0
for kleidi, timi in sorted_modules_dic.items():
    i += 1
    # print(i,'}',kleidi,timi)
    print(f"{{{i}}}  [{kleidi}] {timi}")  # Διπλά {{ για να εμφανιστεί ο χαρακτήρας {
input(
    "Ζ. Διαδρομές στις οποίες γίνεται αναζήτηση για διαθέσιμα αρθρώματα: Πατήστε Enter:"
)
list_path = sys.path
i = 0
for timi in list_path:
    i += 1
    print(f"({i}) \t {timi}")
