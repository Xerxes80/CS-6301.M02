# CS 6301.M02
# NLP
# Ngram
# Kevin Tabesh
# Net-id: KXT170430

# ===========================

import pathlib
import pickle
from os import path

from nltk.tokenize import word_tokenize
from nltk.util import ngrams

file_names=("LangId.train.English", "LangId.train.French", "LangId.train.Italian")

def process(item):


    # Defining language name

    x = item.split(".")
    lang =x[2]
    if not path.exists(lang.lower()+"_unigram.pickle"):
        # Creating unigram and bigram

        unigrams = create_unigram_list(item)
        print("Creating " + lang + " Unigram Dictionary! Please Wait...")
        unigram_dict = create_unigram_dict(unigrams)
        pickle.dump(unigram_dict, open(lang.lower() + "_unigram.pickle", "wb"))
    elif not path.exists(lang.lower() + "_bigram.pickle"):
        print("test")
        unigrams = create_unigram_list(item)

    if not path.exists(lang.lower() + "_bigram.pickle"):
        bigrams = create_bigram_list(unigrams)

        # Creating dictionaries of counts for the unigrams and bigrams

        print("Creating "+lang+" Bigram Dictionary! Please Wait...")
        bigram_dict = create_bigram_dict(bigrams)
        pickle.dump(bigram_dict, open(lang.lower()+"_bigram.pickle", "wb"))



def create_unigram_list(n):
    path =  'data/'+n
    with open(pathlib.Path.cwd().joinpath(path), 'r') as f:
        raw_text = ""
        for readline in f:
            line_strip = readline.strip()
            raw_text += line_strip

        unigrams = word_tokenize(raw_text)

        return unigrams

def create_bigram_list(unigrams):

    bigrams = list(ngrams(unigrams, 2))
    return bigrams

def create_unigram_dict(unigrams):
    unigram_dict = {t: unigrams.count(t) for t in set(unigrams)}
    return unigram_dict

def create_bigram_dict(bigrams):
    bigram_dict = {b: bigrams.count(b) for b in set(bigrams)}
    return bigram_dict

def main():

    for item in file_names:
        process(item)

    print("\n** All Dictionaries Have Been Successfully Created **\n")


if __name__ == "__main__":
   main()
