import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from nltk.corpus import stopwords
import os
import spacy_udpipe
import csv
import gc
import random
from difflib import SequenceMatcher


PATH_TO_UDPIPE_MODEL = '/path/to/udpipe/model'
PATH = '/path/to/texts'
NEW_PATH = '/path/to/save/dataset'
m = 0


nlp = spacy_udpipe.load_from_path(lang="hy",
                                  path=PATH_TO_UDPIPE_MODEL,
                                  meta={"description": "Custom 'hy' model"})


def string_intersection(string1, string2):
    match = SequenceMatcher(None, string1, string2).find_longest_match(0, len(string1), 0, len(string2))
    return match.size > 20


def sentence_tokenizer(text):
    doc = nlp(text)
    return [x.string for x in list(doc.sents)]


def divide_into_paragraphs(sents):
    new_texts = []
    temp_sent = ''
    a, b = (8, 10)
    rand = random.randrange(a, b)
    for e in range(0, len(sents), rand):
        if len(sents[e: e + rand]) < 4:
            temp_sent = ' '.join(sents[e: e + rand])
        else:
            new_texts.append(' '.join(sents[e: e + rand]))
    if len(temp_sent) and len(new_texts):
        new_texts[-1] = new_texts[-1] + temp_sent
    return new_texts


def join_pars(par1, par2=None, par3=None, par4=None):
    global m
    global filename
    new_filename = os.path.join(NEW_PATH, filename + '{}.txt'.format(m))
    with open(new_filename, 'w') as wr:
        if not par2:
	    wr.write(par1)
        else:
	    if not par3:
	        wr.write(par1 + '\n$' + par2)
	    elif not par4:
	        wr.write(par1 + '\n$' + par2 + '\n$' + par3)
	    else:
	        wr.write(par1 + '\n$' + par2 + '\n$' + par3 + '\n$' + par4)


def no_changes1(par1):    
    for i in range(0, len(par1) - 1):
        for j in range(i, len(par1)):
            join_pars(par1='\n'.join([par1[i], par1[j]]))


def no_changes2(par1):
    for i in range(len(par1) - 2):
        for j in range(i, len(par1) - 1):
            for k in range(j, len(par1)):
                join_pars(par1='\n'.join([par1[i], par1[j], par1[k]]))


def no_changes3(par1):
    for i in reversed(range(len(par1) - 3)):
        for j in range(i, len(par1) - 2):
            for k in range(j, len(par1) - 1):
                for l in range(k, len(par1)):
                    join_pars(par1='\n'.join([par1[i], par1[j], par1[k], par1[l]]))


def one_change(par1, par2):
    for i in range(len(par1)):
        for j in range(i, round(len(par2))):
            if not string_intersection(par1[i], par2[j]):
                join_pars(par1=par1[i], par2=par2[j])
        for j in range(i, len(par2)-1):
            if not string_intersection(par1[i], par2[j]) and not string_intersection(par1[i], par2[j+1]):
                join_pars(par1=par1[i], par2='\n'.join([par2[j], par2[j+1]]))
        for j in range(i, len(par2)-2):
            if not string_intersection(par1[i], par2[j]) and not string_intersection(par1[i], par2[j + 1]) and not string_intersection(par1[i], par2[j + 2]):
                join_pars(par1=par1[i], par2='\n'.join([par2[j], par2[j+1], par2[j+2]]))
    for i in range(len(par1)-1):
        for j in range(i, len(par2) - 1):
            join_pars('\n'.join([par1[i], par1[i+1]]), '\n'.join([par2[j], par2[j+1]]))
                

def two_changes(par1, par2):
    for i in range(len(par1) - 1):
        for j in range(i, round(len(par2))):
            for k in range(i+1, len(par1)):
                if not string_intersection(par1[i], par2[j]) and not string_intersection(par1[k], par2[j]):
                    join_pars(par1[i], par2[j], par1[k])
        for j in range(round(len(par2)/2), len(par2)-1):
            for k in range(i+1, len(par1)):
                if not string_intersection(par1[i], par2[j]) and not string_intersection(par1[k], par2[j]) and \
                   not string_intersection(par1[k], par2[j+1]) and not string_intersection(par1[i], par2[j+1]):
                       join_pars(par1[i], '\n'.join([par2[j], par2[j+1]]), par1[k])
    for i in range(len(par1) - 2):
        for j in range(i, len(par2)):
            for k in range(i+1, len(par1)-1):
                join_pars(par1[i], par2[j], '\n'.join([par1[k], par1[k+1]]))


def three_changes(par1, par2):
    for i in range(len(par1) - 1):
        for j in range(i, len(par2) - 1):
            for k in range(i+1, len(par1)):
                for l in range(j+1, len(par2)):
                    if not string_intersection(par1[i], par2[j]) and not string_intersection(par1[k], par2[j]) and \
                            not string_intersection(par1[i], par2[l]) and not string_intersection(par1[k], par2[l]):
                        join_pars(par1[i], par2[j], par1[k], par2[l])


def main(filenames):
    for filename1, filename2 in filenames:
        file1 = os.path.join(PATH, filename1)
        file2 = os.path.join(PATH, filename2)
        with open(file1) as f1:
            par1 = divide_into_paragraphs(sentence_tokenizer(f1.read()))
        with open(file2) as f2:
            par2 = divide_into_paragraphs(sentence_tokenizer(f2.read()))

        if len(par1) < len(par2):
            one_change(par1, par2)
        else:
            one_change(par2, par1)
        two_changes(par1, par2)
        three_changes(par1, par1)

        no_changes(par1)
        no_changes(par2)


if __name__ == '__main__':
    filenames = []
    main(filenames)


