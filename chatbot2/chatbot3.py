# import random
# import json
# import pickle
# import numpy as np
# import urllib.parse
# import urllib.request
#
# import nltk
# from nltk.stem import WordNetLemmatizer
#
# from tensorflow import keras
# from keras.models import load_model
#
# lemmatizer = WordNetLemmatizer()
# intents = json.loads(open('intents.json').read())
#
# words = pickle.load(open('words.pkl', 'rb'))
# classes = pickle.load(open('classes.pkl', 'rb'))
#
# model = load_model('chatbotmodel.h5')
#
# context = {}
#
# def clean_up_sentence(sentence):
#     sentence_words = nltk.word_tokenize(sentence)
#     sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
#     return sentence_words
#
# def bag_of_words(sentence):
#     sentence_words = clean_up_sentence(sentence)
#     bag = [0] * len(words)
#     for w in sentence_words:
#         for i,word in enumerate(words):
#             if word == w:
#                 bag[i] = 1
#     return np.array(bag)
#
# # Prediction
# def predict_class(sentence):
#     bow = bag_of_words(sentence)
#     res = model.predict(np.array([bow]))[0]
#     ERROR_TRESHOLD = 0.25
#     results = [[i, r] for i, r in enumerate(res) if r > ERROR_TRESHOLD]
#
#     results.sort(key=lambda x: x[1], reverse= True)
#     return_list = []
#     for r in results:
#         return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
#
#     return return_list
#
# def get_response(intents_list, intents_json):
#     tag = intents_list[0]['intent']
#     list_of_intents = intents_json['intents']
#     for i in list_of_intents:
#         if i['tag'] == tag:
#             result = random.choice(i['responses'])
#             break
#     return result
#
# def search_web(query):
#     query = urllib.parse.quote(query)
#     url = "https://google.com/search?q=" + query
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
#     req = urllib.request.Request(url, headers=headers)
#     resp = urllib.request.urlopen(req)
#     respData = resp.read()
#     return respData
#
# def get_wikipedia_summary(query):
#     query = query.replace(' ', '_')
#     url = f"https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exsentences=3&explaintext=1&titles={query}"
#     headers = {'User-Agent': 'Mozilla/5.0'}
#     req = urllib.request.Request(url, headers=headers)
#     resp = urllib.request.urlopen(req)
#     data = json.loads(resp.read())
#     page = next(iter(data['query']['pages'].values()))
#     summary = page['extract']
#     return summary
#
# def get_answer(intents_list):
#     tag = intents_list[0]['intent']
#     list_of_intents = intents['intents']
#     for i in list_of_intents:
#         if i['tag'] == tag:
#             if 'context_set' in i:
#                 context['context_set'] = i['context_set']
#             if 'context_filter' not in i or ( 'context_filter' in i and i['context_filter'] in context and context[i['context_filter']] == True):
#                 return random.choice(i['responses'])
#
#
#
#
# def handle_context(intents_list):
#     global context
#     if 'context_filter' in intents_list[0]:
#         if intents_list[0]['context_filter'] != context.get('context_set'):
#             return "I am not able to answer that question right now."
#     if 'context_set' in intents_list[0]:
#         context['context_set'] = intents_list[0]['context_set']
#
# def chat():
#     print("Start The Chat!")
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() == 'quit':
#             break
#
#         # Prediction
#         results = predict_class(user_input)
#
#         # Get the most probable intent
#         response = get_response(results, intents)
#
#         # Handle context of the conversation
#         handle_context(results)
#
#         # Check for special cases
#         if response == "search_web":
#             search_query = user_input.split('search for')[-1].strip()
#             print("Searching for: " + search_query)
#             results = search_web(search_query)
#             print(results)
#         elif response == "get_wikipedia_summary":
#             search_query = user_input.split('tell me about')[-1].strip()
#             print("Searching wikipedia for: " + search_query)
#             summary = get_wikipedia_summary(search_query)
#             print(summary)
#         else:
#             print("Bot: " + response)
#
# if __name__ == '__main__':
#     chat()





import random
import json
import pickle
import numpy as np
import urllib.parse
import urllib.request

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow import keras
from keras.models import load_model

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())

words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))

model = load_model('chatbotmodel.h5')

context = {}

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

# Prediction
def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})

    return return_list

def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result

def search_web(query):
    query = urllib.parse.quote(query)
    url = f"https://google.com/search?q={query}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    return respData

def get_wikipedia_summary(query):
    query = query.replace(' ', '_')
    url = f"https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exsentences=3&explaintext=1&titles={query}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    data = json.loads(resp.read())
    page = next(iter(data['query']['pages'].values()))
    summary = page['extract']
    return summary

def get_answer(intents_list):
    tag = intents_list[0]['intent']
    list_of_intents = intents['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            if 'context_set' in i:
                context['context_set'] = i['context_set']
            if 'context_filter' not in i or ('context_filter' in i and i['context_filter'] in context and context[i['context_filter']] == True):
                return random.choice(i['responses'])


def handle_context(intents_list):
    global context
    if 'context_filter' in intents_list[0]:
        if intents_list[0]['context_filter'] in context:
            if context[intents_list[0]['context_filter']] == True:
                return get_answer(intents_list)
            else:
                return "I'm sorry, I cannot answer that without additional context."
        else:
            return "I'm sorry, I cannot answer that without additional context."
    elif 'context_set' in intents_list[0]:
        context[intents_list[0]['context_set']] = True
        return get_answer(intents_list)
    else:
        return get_answer(intents_list)

def chat():
    print("Start talking with the bot (type quit to stop)!")
    while True:
        message = input("> ")
        if message.lower() == "quit":
            break

        # get the response based on the input message
        ints = predict_class(message)
        res = get_answer(ints)

        # handle context for follow-up questions
        handle_context(ints)

        # check if the bot needs to search the web or wikipedia for an answer
        if res == "search_web":
            print("I'm sorry, I don't know the answer. Let me search the web for you...")
            data = search_web(message)
            print(data)
        elif res == "get_wikipedia_summary":
            print("I'm sorry, I don't know the answer. Let me check wikipedia for you...")
            summary = get_wikipedia_summary(message)
            print(summary)
        else:
            print(res)

if __name__ == '__main__':
    chat()
