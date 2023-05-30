import pandas
from os import system as sys

DATA_PATH = "nato_phonetic_alphabet.csv"

# reading CSV file
df = pandas.read_csv(DATA_PATH)

# creating dictionary with key set as letter and value set as word that describes it
nato_alphabet = {row[0]: row[1] for (index, row) in df.iterrows()}
# print(nato_alphabet)

# taking input from user
sys("cls")
word = input("\nEnter a word: ")

# creating list with words that describe each letter in word
word_NATO_alphabet = [nato_alphabet[n.upper()] for n in word]

# printing created list
print(word_NATO_alphabet)