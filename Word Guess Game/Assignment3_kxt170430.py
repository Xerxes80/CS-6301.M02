# CS-6301.M02
# Homework3_KXT170430
# Word Guessing Game
# Kevin Tabesh
# Net-id: KXT170430

# ===========================
import pathlib
import sys
from random import randint

import nltk
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from lexical_diversity import lex_div as ld


def proccessor(tk):
    tokenized_text = list(tk)
    tokens = [t.lower() for t in tokenized_text]
    print("\nThe number of tokens in text: ", len(tokens))
    tokens_t = [t for t in tokens if t.isalpha() and
           t not in stopwords.words('english') and
           len(t)>5]

    wnl = WordNetLemmatizer()
    lemmas = [wnl.lemmatize(t) for t in tokens_t]
    # make unique
    lemmas_unique = list(set(lemmas))


    tags = nltk.pos_tag(lemmas_unique)
    print('TAGS: ',tags[:20])

    noun_lemmas = [token for token,pos in tags \
                   if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS')]

    print("\nNumber of Tokens: ", len(tokens_t))
    print("\nNumber Of Noun Lemmas: ", len(noun_lemmas))

    pos_dict = {}
    for tok in tokens_t:
        if wnl.lemmatize(tok) in noun_lemmas:
            counter = tokens_t.count(tok)
            pos_dict[tok]= counter


    sorted_Dict = sorted(pos_dict.items(), key = lambda x: x[1], reverse = True)

    print('The 50 most common words and their counts: ', sorted_Dict[:50])

    guessing_list = [key for key, value in sorted_Dict[:50]]

    return guessing_list

def calc_lex_dev(text,tokens):
    # if ld:
    #     flt = ld.flemmatize(text)
    #     lx_dv =  ld.ttr(flt)
    #     print('\nLexical diversity using lexical_diversity libarary: ',"{:.2f}".format(lx_dv))
    #

    # lowercase the text
    tokens_t = [t.lower() for t in tokens]
    # create a set of tokens (not-repeated)
    set_t = set(tokens_t)
    # measuring lexical diversity
    print("\nLexical diversity manually calculated: %.2f" % (len(set_t) / len(tokens_t)))

def random_num():
    return randint(0, 49)

def guessing_game(guessing_list):


    # Initiate

    index = random_num()                    # Random number
    word = guessing_list[index]             # Define the randomly selected word
    target_list = list(word)                # List of word letters
    target_set = set(target_list)           # Set of letters in the word
    target_set_length = len(target_set)     # Length of word's letters set
    guessed_chars = []                      # List of guessed letters
    score = 5                               # Starting score
    # Printing the placeholders underscores
    preview = ''
    for ch in target_list:
            preview += ' _'
    print(preview)
    # End of initiate

    stop = 0
    while score>=0 and stop ==0:            # while score is not negative get user input
        user_input = get_user_input()
        if user_input in guessed_chars:
            # Repeated guess
            score -= 1
            print_message(0, score)
            preview_result(target_list, guessed_chars)
        else:
            res = target_list.count(user_input)
            if res>0:
                # Right guess
                guessed_chars.append(user_input)
                score += 1
                print_message(1, score)
                preview_result(target_list, guessed_chars)
            else:
                # Wrong Guess
                score -= 1
                if score >=0:
                    print_message(0, score)
                    preview_result(target_list, guessed_chars)
        # All letters are guessed
        if target_set_length == len(guessed_chars):
            stop =1

    if score>=0 and stop ==1:
        print_message(2, score)
    if score<0 :
        print_message(3, score)

def get_user_input():
    # Get User input and exit if input is '!'
    new_quess = input("Guess a letter: ")
    if new_quess == '!':
        quit()
    else:
        return new_quess

def preview_result(target,guessed):
    # print the result after validating
    preview = ''
    for ch in target:
        if ch in guessed:
            preview += ' ' + ch
        else:
            preview += ' _'
    print(preview)

def print_message(status, score):
    if status == 1:
        print("Right! Score is ",score)
    elif status == 2:
        print("You solved it!")
        print("\nCurrent score: ",score)
        print("\nGuess another word\n")
    elif status == 3:
        print("You lost!")
        print("\nGuess another word\n")
    else:
        print("Sorry, guess again. Score is ",score)


def main():
    path = 'anat19.txt'
    with open(pathlib.Path.cwd().joinpath(path), 'r') as f:

        raw_text = f.read()
        tokens = word_tokenize(raw_text)
        calc_lex_dev(raw_text, tokens)
        guessing_list = proccessor(tokens)
        print("\nLet's play a word guessing game!")
        while True:
            guessing_game(guessing_list)


if __name__ == "__main__":
   main()
