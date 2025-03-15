"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Karel Nechvátal
email: knechvatal6@seznam.cz
"""
import string

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

# Registrovaní uživatelé
USERS = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# Přihlášení uživatele
username = input("username: ")
password = input("password: ")

if USERS.get(username) != password:
    print("unregistered user, terminating the program..")
    exit()

print("-" * 40)
print(f"Welcome to the app, {username}")
print("We have 3 texts to be analyzed.")
print("-" * 40)

# Výběr textu
try:
    choice = int(input("Enter a number btw. 1 and 3 to select: "))
    print("-" * 40)
    if choice not in range(1, 4):
        print("Invalid choice. Exiting the program.")
        exit()
except ValueError:
    print("You must enter a number. Exiting the program.")
    exit()

text = TEXTS[choice - 1]
words = text.split()
clean_words = [word.strip(string.punctuation) for word in words]

# Analýza textu
word_count = len(clean_words)
titlecase_count = sum(1 for word in clean_words if word.istitle())
uppercase_count = sum(1 for word in clean_words if word.isupper() and word.isalpha())
lowercase_count = sum(1 for word in clean_words if word.islower())
numeric_values = [int(word) for word in clean_words if word.isdigit()]
numeric_count = len(numeric_values)
numeric_sum = sum(numeric_values)

# Výpis statistik
print(f"There are {word_count} words in the selected text.")
print(f"There are {titlecase_count} titlecase words.")
print(f"There are {uppercase_count} uppercase words.")
print(f"There are {lowercase_count} lowercase words.")
print(f"There are {numeric_count} numeric strings.")
print(f"The sum of all the numbers {numeric_sum}")
print("-" * 40)

# Sloupcový graf délky slov
word_lengths = {}
for word in clean_words:
    length = len(word)
    if length in word_lengths:
        word_lengths[length] += 1
    else:
        word_lengths[length] = 1

print("LEN|  OCCURENCES  |NR.")
print("-" * 40)
for length in sorted(word_lengths):
    print(f"{length:>3}| {'*' * word_lengths[length]:<15} |{word_lengths[length]}")
