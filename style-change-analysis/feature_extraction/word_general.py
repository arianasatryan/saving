import re
from collections import defaultdict, Counter
from utils import lemmatizer, nlp_stanza as nlp


dict_of_freqs = {}
with open('external_data/words_with_freqs.txt', 'r') as f:
    for line in f:
        key, val = line.split()
        dict_of_freqs[key] = int(val)


def list_of_uncommon_words():
    res = defaultdict(list) 
    for key, val in sorted(dict_of_freqs.items()): 
        res[val].append(key)
    return res[1]


def find_not_armenian_letters(text: str):
    for char in text:
        if char.isalpha() and re.search('[^\u0561-\u0587\u0531-\u0556]', char) != None:
            return [1.0]
    return [0.0]


def contains_jargon(text:str):
    with open('external_data/jargon_words.txt', 'r') as f:
        jargon_words = f.read().split('\n')
    lemmas = lemmatizer(text)
    for jargon_word in jargon_words:
        if jargon_word in lemmas:
            return [1.0]
    return [0.0]


def uncommon_words(text: str):
    lemmas = lemmatize(text)
    for uncommon_word in list_of_uncommon_words():
        if uncommon_word in lemmas:
            return[1.0]
    return [0.0]


def uncommon_words_freq(text: str):
    lemmas = lemmatizer(text)
    c = Counter(lemmas)
    count = 0.0
    for word in list_of_uncommon_words():
        count += c[word]
    return count/len(lemmas)
   

def average_freq_of_words(text: str):
    all_words_count = sum(dict_of_freqs.values())
    lemmas = lemmatizer(text)
    print(lemmas)
    return [dict_of_freqs.get(word, 0)/all_words_count for word in lemmas]

