# CS 6301.M02
# NLP
# Project1: Building a Corpus
# Kevin Tabesh
# Net-id: KXT170430
# ============================================
from nltk.corpus import wordnet as wn
from nltk.wsd import lesk
from nltk.corpus import sentiwordnet as swn
import nltk
from nltk.book import *
import math

def start(name):
   extract(name)
def extract(name):

    print('List of Synsets:')
    for synset in wn.synsets(name):
        print(synset)
    allNoun=[]
    for synset in wn.synsets(name, pos=wn.NOUN):
        allNoun.append(synset)
    print('=============================')
    print('Definition: \n ', allNoun[0].definition())
    print('=============================')
    print('Usage Example: \n ', allNoun[0].examples())
    print('=============================')
    print('Lemmas: \n ', allNoun[0].lemmas())
    print('=============================')
    print('Synsets Hypernyms:\n ')
    for synset in wn.synsets(name):
        print(synset.hypernyms())

    print('=============================')
    print('Synsets Hyponyms:\n ')
    for synset in wn.synsets(name):
        print(synset.hyponyms())

    print('=============================')
    print('Synsets Meronyms:\n ')
    for synset in wn.synsets(name):
        print(synset.part_meronyms())

    print('=============================')
    print('Synsets Holonyms:\n ')
    for synset in wn.synsets(name):
        print(synset.part_holonyms())

    allVerb = []
    for synset in wn.synsets(name, pos=wn.VERB):
        allVerb.append(synset)
    print('=============================')
    selectedVerb = allVerb[0]
    theVerb = allVerb[0].lemmas()
    print('Selected Verb: ', theVerb[0].name(), '\n')
    print('Definition: \n ', selectedVerb.definition())
    print('Usage Example: \n ', selectedVerb.examples() )
    print('Lemmas: \n ', selectedVerb.lemmas() )

    print('Synsets Hypernyms:\n ')
    for synset in wn.synsets(theVerb[0].name()):
        print(synset.hypernyms())

    print('=============================')
    print('Synsets Hyponyms:\n ')
    for synset in wn.synsets(theVerb[0].name()):
        print(synset.hyponyms())

    print('=============================')
    print('Synsets Meronyms:\n ')
    for synset in wn.synsets(theVerb[0].name()):
        print(synset.part_meronyms())

    print('=============================')
    print('Synsets Holonyms:\n ')
    for synset in wn.synsets(theVerb[0].name()):
        print(synset.part_holonyms())

    print('=============================')
    print('Morphy:\n ',wn.morphy(theVerb[1].name(), wn.NOUN))
    print('Morphy:\n ',wn.morphy(theVerb[1].name(), wn.VERB))

    print('=============================')
    print('Wu-Palmer Similarity Metric (Run-Jump):\n')
    run = wn.synset('run.v.01')
    jump = wn.synset('jump.v.01')
    print(wn.path_similarity(run, jump))


    print('=============================')
    print('SentiWordNet (desperate):\n')
    desperate = swn.senti_synset('desperate.s.03')
    print(desperate)
    print("Positive score = ", desperate.pos_score())
    print("Negative score = ", desperate.neg_score())
    print("Objective score = ", desperate.obj_score())

    print('=============================')
    print('Collocations (text4):\n')
    text4.collocations()
    vocab = len(set(text6))
    hg = text4.count('fellow citizens')/vocab
    print("p(fellow citizens) = ",hg )
    h = text4.count('fellow')/vocab
    print("p(fellow) = ", h)
    g = text4.count('citizens')/vocab
    print('p(citizens) = ', g)
    # pmi = math.log2(hg / (h * g))
    # print('pmi = ', pmi)



if __name__ == '__main__':
    start('exercise')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
