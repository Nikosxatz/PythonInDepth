"""
    Αυτό το πρόγραμμα διαβάζει ενα αρχείο κειμένου και το γράφει σε ένα άλλο με διαφορετική κωδικοποίηση.
    Κάνει έλεγχους με τη χρήση διαχείρισης εξαιρέσεων. (Κεφάλαιο 16 του βιβλίου)
    Αν η εκτέλεση του προγράμματος γίνεται στο terminal των windows και οχι στο IDLE εμφανίζει τα μηνύματα λάθους με χρώμα.
"""
import sys
import os  # τεκμηρίωση: https://docs.python.org/3/library/os.html
import platform  # τεκμηρίωση: https://docs.python.org/3/library/platform.html


def try_again():
    again = (
        input("Για νέα προσπάθεια πληκτρολόγησε Enter: Οτιδήποτε άλλο για διακοπή.")
        or "Yes"
    )
    if again != "Yes":
        sys.exit("Η εφαρμογή τερματίστηκε απο τον χρήστη.")


def color(col):
    """
    Εμφάνιση έγχρωμων χαρακτήρων μόνο με εκτέλεση σε terminal και λειτουργικό Windows
    Τεκμηρίωση: https://en.wikipedia.org/wiki/ANSI_escape_code
    \u001b Escape character. ascii code 27
    """
    color_codes = {
        "Reset": "[0m",
        "Black": "[30m",
        "Red": "[31m",
        "Green": "[32m",
        "Yellow": "[33m",
        "Blue": "[34m",
        "Magenta": "[35m",
        "Cyan": "[36m",
        "White": "[37m",
    }
    # Έλεγχος αν η εκτέλεση γίνεται σε terminal των windows ώστε να εμφανίζονται χρώματα στα μηνύματα λάθους.
    if "pythonw.exe" in sys.executable or platform.system() != "Windows":
        return ""
    else:
        return "\u001b" + color_codes[col]


# Άνοιγμα του αρχείου για ανάγνωση
def get_file_name():
    f_in = None
    while f_in == None:
        try:  # τεκμηρίωση για την διαχείριση εξαιρέσεων στο κεφάλαιο 16 του βιβλίου
            file_to_read = input("Δώσε το όνομα του αρχείου που θέλεις να διαβάσω: ")
            f_in = open(file_to_read, "r")
            f_in.close()
            return file_to_read
        except FileNotFoundError as msg:
            print(
                msg,
                color("Red")
                + "\nΤο αρχείο δεν υπάρχει στον τρέχοντα φάκελο εργασίας που είναι ο:"
                + color("Reset"),
            )
            print(os.getcwd())
            try_again()


# Κωδικοποίηση με την οποία εχει γραφτεί το αρχείο.
def get_encoding(file_to_read, error_info):
    while True:
        try:
            text_encoding = input("Δώσε την κωδικοποίηση που έχει το αρχείο: ")
            with open(file_to_read, "r", encoding=text_encoding) as f_in:
                text_readed = f_in.read()
                return text_readed
        except LookupError as msg:
            print(
                msg,
                color("Red"),
                "\nΑγνωστη κωδικοποίηση",
                color("Reset"),
                error_info,
            )
            try_again()
        except UnicodeDecodeError as msg:
            print(
                msg,
                color("Red") + "\nΑσύμβατη κωδικοποίηση." + color("Reset"),
                error_info,
            )
            try_again()


# Δημιουργία νέου αρχείου με άλλη κωδικοποίηση
def create_new_file(new_file_name, text, error_info):
    while True:
        try:
            new_encoding = (
                input(
                    "Ποιά κωδικοποίηση θέλεις να έχει το νέο αρχείο; (enter για utf-8): "
                )
                or "utf-8"
            )
            with open(new_file_name, "w", encoding=new_encoding) as f_out:
                f_out.write(text)
                print("Το αρχείο δημιουργήθηκε με επιτυχία.")
                return True
        except LookupError as msg:
            print(
                msg,
                color("Red"),
                "\nΆγνωστη κωδικοποίηση.",
                color("Reset"),
                error_info,
            )
            try_again()
        except UnicodeEncodeError as msg:
            print(
                msg,
                color("Red"),
                "\nΤο αρχείο δεν μπορεί να δημιουργηθεί με την κωδικοποίηση που είπες.",
                color("Reset"),
            )
            try_again()
        except OSError as msg:
            print(
                msg,
                color("Red"),
                "\nΚάτι δεν πήγε καλά και δεν δημιουργήθηκε το αρχείο.\n"
                + "Μήπως δεν έχεις δικαιώματα εγγραφής σε αυτό τον φάκελο;\n"
                + "Μήπως δεν έδωσες έγκυρο όνομα αρχείου;",
                color("Reset"),
            )
            try_again()
            return False


def main():
    print(__doc__)

    encoding_decoding_info_message = (
        color("Green")
        + """     
    \rΠληροφορίες για τις κωδικοποιήσεις στον παρακάτω σύνδεσμο.
    \rhttps://docs.python.org/3.11/library/codecs.html#standard-encodings   
    """
        + color("Reset")
    )
    # Πρώτο μέρος. Άνοιγμα του αρχείου για ανάγνωση
    file_to_read = get_file_name()

    # Δεύτερο μέρος. Πρέπει να δωθεί η σωστή κωδικοποίηση με την οποία έχει γραφτεί το αρχείο.
    text = get_encoding(file_to_read, encoding_decoding_info_message)
    print(text)

    # Τρίτο μέρος. Δημιουργία του νέου αρχείου με άλλη κωδικοποίηση
    done = False
    while not done:
        new_file_name = input("Δώσε το όνομα του ΝΕΟΥ αρχείου: ")
        done = create_new_file(new_file_name, text, encoding_decoding_info_message)


if __name__ == "__main__":
    main()
