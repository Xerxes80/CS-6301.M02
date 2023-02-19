# CS 6301.MS2
# Homework4_KXT170430
# NLP
# Homework 4: Language Models Part 2
# Kevin Tabesh
# Net-id: KXT170430

# ===========================
import pathlib
import pickle
import os
from nltk import word_tokenize, ngrams

lang_list = ("english", "french", "italian")


def compute_prob(line, unigram_dict, bigram_dict, v):
    # n is the number of tokens in the training data
    # v is the vocabulary size in the training data (unique tokens)

    unigrams_test = word_tokenize(line)
    bigrams_test = list(ngrams(unigrams_test, 2))
    p_laplace = 1  # calculate probability using Laplace smoothing

    for bigram in bigrams_test:

        b = bigram_dict[bigram] if bigram in bigram_dict else 0
        u = unigram_dict[bigram[0]] if bigram[0] in unigram_dict else 0
        p_laplace = p_laplace * ((b + 1) / (u + v))
    return p_laplace

def compute_accuracy():
    if os.path.exists("Pr_result.txt") and os.path.exists("data/LangId.sol"):
        with open(pathlib.Path.cwd().joinpath("data/LangId.sol"), 'r') as f:
            src_text = f.read()
        src_file = src_text.splitlines()

        with open(pathlib.Path.cwd().joinpath("Pr_result.txt"), 'r') as f:
            res_text = f.read()
        result_file = res_text.splitlines()
        # Calculating accuracy
        acc_res = 0
        incorrect_lines = []
        for x in range(0, len(src_file)):
            if src_file[x] == result_file[x]:
                acc_res +=1;
            else:
                incorrect_lines.append(x+1)
        accuracy = (acc_res / len(src_file)) * 100
        print("Accuracy : ", accuracy,"%")
        print("Incorrect line numbers : ",  incorrect_lines)

def main():

    if os.path.exists("Pr_result.txt"):
        os.remove("Pr_result.txt")

    with open(pathlib.Path.cwd().joinpath("data/LangId.test"), 'r') as f:
        test_text = f.read()
    lines = test_text.splitlines()
    # Unloading pickled files and calculating length of bigram dictionaries
    for lang in lang_list:
        if lang == "english":
            english_unigram_unpickle = pickle.load(open("english_unigram.pickle", "rb"))
            english_bigram_unpickle = pickle.load(open("english_bigram.pickle", "rb"))
            v_english = len(english_bigram_unpickle)
        elif lang == "french":
            french_unigram_unpickle = pickle.load(open("french_unigram.pickle", "rb"))
            french_bigram_unpickle = pickle.load(open("french_bigram.pickle", "rb"))
            v_french = len(french_bigram_unpickle)
        else:
            italian_unigram_unpickle = pickle.load(open("italian_unigram.pickle", "rb"))
            italian_bigram_unpickle = pickle.load(open("italian_bigram.pickle", "rb"))
            v_italian = len(italian_bigram_unpickle)

    # Computing probability for each line in the LangId.test
    counter = 1
    for line in lines:
        english_pr = compute_prob(line, english_unigram_unpickle, english_bigram_unpickle, v_english)
        max = (english_pr, "English")
        french_pr = compute_prob(line, french_unigram_unpickle, french_bigram_unpickle, v_french)
        if french_pr > max[0]:
            max = (french_pr, "French")

        italian_pr = compute_prob(line, italian_unigram_unpickle, italian_bigram_unpickle, v_italian)
        if italian_pr > max[0]:
            max = (italian_pr, "Italian")

        with open("Pr_result.txt", "a") as file_object:
            file_object.write(str(counter)+" "+ max[1]+"\n")
        counter += 1

    compute_accuracy()

if __name__ == "__main__":
    main()
