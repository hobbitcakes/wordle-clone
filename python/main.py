import json
import random
from colorama import Style, Back, Fore

def load_words(w_len):
    with open(f'../words-of-length-{w_len}.json') as file:
        words = json.load(file)
    
    return words

def get_random_word(words: list) -> str:
    return random.choice(words)    

def enter_guess(w_len: int, dictionary: list):
    guess_template = '_ ' * w_len
    print(guess_template.strip())
    guess = input()
    if len(guess) != w_len:
        print("Fault: Guessed word length should be {}".format(w_len))
        return enter_guess(w_len, dictionary)
    
    #if guess not in dictionary:
    #    print("Fault: That's not a real word.")
    #    return enter_guess(w_len, dictionary)
    
    return guess

def correct_guess(guess: str, word: str) -> bool:
    
    if len(guess) != len(word):
        raise Exception("Guessed word length is not: {}".format(len(word)))
    for g_letter, w_letter in zip(guess, word):
        if g_letter != w_letter:
            return False
            
    
    return True

def green(letter: str):
    return Fore.GREEN + letter + Fore.WHITE
    
def yellow(letter: str):
    return Fore.YELLOW + letter + Fore.WHITE

def rgb_guess(guess: str, word: str) -> str:
    if len(guess) != len(word):
        raise
    
    rgb = ""
    letters = [letter for letter in word]

    for g_letter, w_letter in zip(guess, word):
        if g_letter == w_letter:
            rgb += green(g_letter)
            letters.remove(g_letter)
        elif g_letter in word and g_letter in letters:
            rgb += yellow(g_letter)
            letters.remove(g_letter)
        else:
            rgb += g_letter
    
    return rgb
    
def add_guessed_letters(letters: list, word: str):
    for character in word:
        letters.append(character)
    
    letters.sort()
    
def print_guess(guess: str, word:str) -> None:
    print(rgb_guess(guess, word))

def game_logic(word: str, w_len: int, guesses: int):
    dictionary = load_words(w_len)
    prior_guesses = []
    guessed_letters = []
    abc = []
    for i in range(1, guesses + 1):
        guess = enter_guess(w_len, dictionary)
        correct = correct_guess(guess, word)
        prior_guesses.append(guess)

        if correct:
            return True

        print("\n++++++++++++++\n")
        for guess in prior_guesses:
            print_guess(guess, word)
        
        add_guessed_letters(guessed_letters, guess)
        
        

def main(w_len: int):
    wordle_word = get_random_word(load_words(w_len))
    guesses = 5
    print("Welcome to the hobbit wordle!")
    print("Same rules as wordle, your objective is to guess the right word using guesses and hints to figure it out!")
    win = game_logic(wordle_word, w_len, guesses)
    if win:
        print("You won!")
    else:
        print("You loose, the word was:")
        print(wordle_word)
    
    

if __name__ == '__main__':
    main(w_len=5)