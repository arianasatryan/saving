import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from nltk.corpus import stopwords
import os
import spacy_udpipe
import csv
import gc
import random


PATH_TO_CSV_FILE = '/path/to/csv/file'
PATH_TO_UDPIPE_MODEL = '/path/to/udpipe/model'
PATH = '/path/to/texts'
NEW_PATH = '/path/to/save/dataset'

nlp = spacy_udpipe.load_from_path(lang="hy",
                                  path=PATH_TO_UDPIPE_MODEL,
                                  meta={"description": "Custom 'hy' model"})


def sentence_tokenizer(text):
    doc = nlp(text)
    return [x.string for x in list(doc.sents)]


def divide_into_paragraphs(sents, one_author=False):
    new_texts = []
    temp_sent = ''
    a, b = (15, 25) if one_author else (5, 9)
    rand = random.randrange(a, b)
    for e in range(0, len(sents), rand):
        if len(sents[e: e + rand]) < 5:
            temp_sent = ' '.join(sents[e: e + rand])
        else:
            new_texts.append(' '.join(sents[e: e + rand]))
    if len(temp_sent) and len(new_texts):
        new_texts[-1] = new_texts[-1] + temp_sent
    return new_texts


def two_authors(i, j, nn, m, files, k):
    global multiauthor
    kw1 = k[i]
    kw2 = k[j]
    file1 = files[i]
    file2 = files[j]
    filename1 = os.path.join(PATH, file1)
    filename2 = os.path.join(PATH, file2)
    f = open(filename1, 'r')
    g = open(filename2, 'r')
    text1 = f.read()
    text2 = g.read()
    f.close()
    g.close()
    sents1 = sentence_tokenizer(text1)
    sents2 = sentence_tokenizer(text2)
    new_texts1 = divide_into_paragraphs(sents1)
    new_texts2 = divide_into_paragraphs(sents2)
    l1 = len(new_texts1)
    l2 = len(new_texts2)
    minl = min(l1, l2)
    if minl % 3 == 0:
        for e in range(0, minl, 3):
            new_filename = os.path.join(NEW_PATH, 'problem' + str(m) + '.txt')
            m = m + 1
            with open(new_filename, 'w') as wr:
            	wr.write(new_texts1[e] + '\n$' + new_texts2[e] + '\n$' + new_texts1[e+1])
            new_filename = os.path.join(NEW_PATH, 'problem' + str(m) + '.txt')
            m = m + 1
            with open(new_filename, 'w') as wr:
            	wr.write(new_texts2[e+1] + '\n$' + new_texts1[e+2] + '\n$' + new_texts2[e+2])
    elif minl % 2 == 1:
        for e in range(0, minl):
            new_filename = os.path.join(NEW_PATH, 'problem' + str(m) + '.txt')
            m = m + 1
            with open(new_filename, 'w') as wr:
            	wr.write(new_texts1[e] + '\n$' + new_texts2[e])
    elif minl % 2 == 0:
        for e in range(0, minl, 2):
            new_filename = os.path.join(NEW_PATH, 'problem' + str(m) + '.txt')
            m = m + 1
            with open(new_filename, 'w') as wr:
            	wr.write(new_texts1[e] + '\n$' + new_texts2[e] + '\n$' + new_texts1[e+1] + '\n$' + new_texts2[e + 1])
    if l1 == l2:
        files.remove(file1)
        files.remove(file2)
        k.remove(kw1)
        k.remove(kw2)
        os.remove(filename1)
        os.remove(filename2)
        return nn - 2, m, files, k
    if l1 > l2:
        f = open(filename1, 'w')
        f.write(''.join(new_texts1[l2:]))
        f.close()
        files.remove(file2)
        k.remove(kw2)
        os.remove(filename2)
        return nn - 1, m, files, k
    elif l2 > l1:
        g = open(filename2, 'w')
        g.write(''.join(new_texts2[l1:]))
        g.close()
        files.remove(file1)
        k.remove(kw1)
        os.remove(filename1)
        return nn - 1, m, files, k


def three_authors(i, j, r, nn, m, files, k):
    global multiauthor
    file1 = files[i]
    file2 = files[j]
    file3 = files[r]
    kw1 = k[i]
    kw2 = k[j]
    kw3 = k[r]
    filename1 = os.path.join(PATH, file1)
    filename2 = os.path.join(PATH, file2)
    filename3 = os.path.join(PATH, file3)
    f = open(filename1, 'r')
    g = open(filename2, 'r')
    z = open(filename3, 'r')
    text1 = f.read()
    text2 = g.read()
    text3 = z.read()
    f.close()
    g.close()
    z.close()
    sents1 = sentence_tokenizer(text1)
    sents2 = sentence_tokenizer(text2)
    sents3 = sentence_tokenizer(text3)
    new_texts1 = divide_into_paragraphs(sents1)
    new_texts2 = divide_into_paragraphs(sents2)
    new_texts3 = divide_into_paragraphs(sents3)
    l1 = len(new_texts1)
    l2 = len(new_texts2)
    l3 = len(new_texts3)
    minl = min(l1, l2, l3)
    if minl % 4 == 0:
        for e in range(0, minl, 4):
            new_filename = os.path.join(NEW_PATH, 'problem' + str(m) + '.txt')
            m = m + 1
            with open(new_filename, 'w') as wr:
            	wr.write(new_texts1[e] + '\n$' + new_texts2[e] + '\n$' + new_texts3[e] + '\n$' + new_texts1[e + 1])
            new_filename = os.path.join(NEW_PATH, 'problem' + str(m) + '.txt')
            m = m + 1
            with open(new_filename, 'w') as wr:
            	wr.write(new_texts2[e + 1] + '\n$' + new_texts3[e + 1] + '\n$' + new_texts2[e + 2] + '\n$' + new_texts1[e + 2])
            new_filename = os.path.join(NEW_PATH, 'problem' + str(m) + '.txt')
            m = m + 1
            with open(new_filename, 'w') as wr:
            	wr.write(new_texts2[e + 3] + '\n$' + new_texts3[e + 2] + '\n$' + new_texts1[e + 3] + '\n$' + new_texts3[e + 3])
    else:
        for e in range(0, minl):
            new_filename = os.path.join(NEW_PATH, 'problem' + str(m) + '.txt')
            m = m + 1
            with open(new_filename, 'w') as wr:
            	wr.write(new_texts1[e] + '\n$' + new_texts2[e] + '\n$' + new_texts3[e])
    if l1 == l2 == l3:
        files.remove(file1)
        files.remove(file2)
        files.remove(file3)
        k.remove(kw1)
        k.remove(kw2)
        k.remove(kw3)
        os.remove(filename1)
        os.remove(filename2)
        os.remove(filename3)
        return nn - 3, m, files, k, False
    if minl == l1:
        if l1 == l2:
            f = open(filename3, 'w')
            f.write(''.join(new_texts3[l1:]))
            f.close()
            files.remove(file1)
            files.remove(file2)
            k.remove(kw1)
            k.remove(kw2)
            os.remove(filename1)
            os.remove(filename2)
            return nn - 2, m, files, k, False
        if l1 == l3:
            f = open(filename2, 'w')
            f.write(''.join(new_texts2[l1:]))
            f.close()
            files.remove(file1)
            files.remove(file3)
            k.remove(kw1)
            k.remove(kw3)
            os.remove(filename1)
            os.remove(filename3)
            return nn - 2, m, files, k, False
        else:
            f = open(filename2, 'w')
            g = open(filename3, 'w')
            f.write(''.join(new_texts2[l1:]))
            g.write(''.join(new_texts3[l1:]))
            f.close()
            g.close()
            files.remove(file1)
            k.remove(kw1)
            os.remove(filename1)
            return nn - 1, m, files, k, (files.index(file2), files.index(file3))
    elif minl == l2:
        if l2 == l3:
            f = open(filename1, 'w')
            f.write(''.join(new_texts1[l2:]))
            f.close()
            files.remove(file2)
            files.remove(file3)
            k.remove(kw2)
            k.remove(kw3)
            os.remove(filename3)
            os.remove(filename2)
            return nn - 2, m, files, k, False
        else:
            f = open(filename1, 'w')
            g = open(filename3, 'w')
            f.write(''.join(new_texts1[l2:]))
            g.write(''.join(new_texts3[l2:]))
            f.close()
            g.close()
            files.remove(file2)
            k.remove(kw2)
            os.remove(filename2)
            return nn - 1, m, files, k, (files.index(file1), files.index(file3))
    elif minl == l3:
        f = open(filename1, 'w')
        g = open(filename2, 'w')
        f.write(''.join(new_texts1[l3:]))
        g.write(''.join(new_texts2[l3:]))
        f.close()
        g.close()
        files.remove(file3)
        k.remove(kw3)
        os.remove(filename3)
        return nn - 1, m, files, k, (files.index(file1), files.index(file2))



files = []
m = 0
k = []
with open(PATH_TO_CSV_FILE, 'r') as csvfile:
    kr = csv.reader(csvfile, delimiter=',')
    for row in kr:
        k.append(set(row[1:]))
        files.append(row[0])


nn = len(k)
while i < nn:
    has2intersection = False
    has3intersections = False
    indices = False
    for j in range(nn):
        if i != j and len(k[j].intersection(k[i])) > 0 and files[i][:files[i].find('.')] != files[j][:files[j].find('.')] and multiauthor<15000:
            for r in range(nn):
                if r != i and r != j and len(k[j].intersection(k[i]).intersection(k[r])) > 0 and files[i][:files[i].find('.')] != files[r][:files[r].find('.')] and files[r][:files[r].find('.')] != files[j][:files[j].find('.')]:
                    has3intersections = True
                    nn, m, files, k, indices = three_authors(i, j, r, nn, m, files, k)
                    break
            if not has3intersections:
                indices = (i, j)
            else:
                if not indices:
                    break
            nn, m, files, k = two_authors(indices[0], indices[1], nn, m, files, k)
            has2intersection = True
            break
    if not has2intersection and not has3intersections:
        filename1 = os.path.join(PATH, files[i])
        with open(filename1, 'r') as f:
            text1 = f.read()
        sents1 = sentence_tokenizer(text1)
        new_texts1 = divide_into_paragraphs(sents1, True)
        for e in range(len(new_texts1)):
            new_filename = os.path.join(NEW_PATH, 'problem' + str(m) + '.txt')
            m = m + 1
            with open(new_filename, 'w') as wr:
                wr.write(new_texts1[e])
        del files[i]
        del k[i]
        os.remove(filename1)
        nn = nn - 1

