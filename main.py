#hangman game
#this is a game where we computer pick a random word from a given list and we have to guess what is the word.

import random
from word_list import words
import string


def get_valid_word(words):
    word=random.choice(words)
    while "-" in word or " " in word: #preventing a word with space or dash been selected 
        word=random.choice(words)
    return word.upper()

def hangman():
    print("Welcome to HANGMAN.......")
    diff=input("Select your diffculty level:\nEasy(e) Medium(m) Hard(h):").lower()
    if diff=="e":
        lives=12
    elif diff=="m":
        lives=9
    else: 
        lives=6
    word=get_valid_word(words)
    word_letters=set(word)  #letters in the word
    alphabet=set(string.ascii_uppercase)
    used_letters=set() #letters user have guessed
    
    while len(word_letters)>0 and lives>0:
        print("you have",lives,"remaining ","you have used these letters: "," ".join(used_letters))
        word_lst=[letter if letter in used_letters else '-' for letter in word]
        print("Current word: "," ".join(word_lst))
        user_letter=input("Guess a letter: ").upper()

        if user_letter in alphabet- used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives=lives-1 
                print("letter is not in the word")

        elif user_letter in used_letters:
            print("You have already Guessed that letter try another one")
    
        else:
            print("inavalid character:( you can only use letters")
    if len(word_letters)==0:
        print(f"Yay! you have gussed the correct word {word}")
    else:
        print(f"Sorry you ran out of lives:( The correct word was {word}")

hangman()