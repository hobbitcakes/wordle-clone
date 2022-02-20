import json
import requests

def get_full_dictionary(site: str) -> list:
    response = requests.get(site)
    
    return str.splitlines(response.text)

def of_length(words: list, length: int) -> list:
    words_of_length = list(filter(lambda w: (len(w) == length), words)) 
    return words_of_length

def write_dictionary(words: list, filename: str) -> None:
    with open(filename, 'w') as file:
        dictionary = json.dump(words, file)

def main(word_len: int):
    words = get_full_dictionary('https://www.mit.edu/~ecprice/wordlist.10000')
    words_of_length = of_length(words, word_len)
    write_dictionary(words_of_length, f'../words-of-length-{word_len}.json')

if __name__ == '__main__':
    main(5)