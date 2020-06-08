import re
from utils import nlp_udpipe as nlp


def cardinal_numbers(text: str):
    doc = nlp(text)
    with open('external_data/cardinal_numbers.txt', 'r') as f:
        numbers = f.read().replace('\n', '|')[:-1]
    forms = [0.0, 0.0]
    for word in doc:
        if not forms[0] and re.search(numbers, word.lemma_) and not word.lemma_.endswith('շաբթ'):
            forms[0] += 1
        if not forms[1] and word.pos_ == 'NUM':
            forms[1] += 1
        if forms == [1.0, 1.0]:
            break
    return forms


def ordinal_numbers(text: str):
    doc = nlp(text)
    with open('external_data/ordinal_numbers.txt', 'r') as f:
        numbers = f.read().replace('\n', '|')[:-1]
    forms = [0.0] * 5
    for word in doc:
        if not forms[0] and re.search(numbers, word.lemma_):
            forms[0] += 1
        if not forms[1] and re.search('i|x|v', word.text):
            forms[1] += 1
        if not forms[2] and re.search('I|X|V', word.text):
            forms[2] += 1
        if not forms[3] and re.search('\d-րդ', word.text):
            forms[3] += 1
        if not forms[4] and re.search('\dրդ', word.text):
            forms[4] += 1
        if forms == [1.0] * 5:
            break
    return forms


def date_format(text: str):
    with open('external_data/months.txt', 'r') as f:
        months = f.read().replace('\n', '|')[:-1]
    forms = [0.0] * 9
    if not forms[0] and re.search(r"(0*[1-30-9]){1,2}\\(0*[1-90-2]){1,2}\\\d{2}", text):
        forms[0] += 1
    if not forms[1] and re.search(r"(0*[1-30-9]){1,2}\/(0*[1-90-2]){1,2}\/\d{2}", text):
        forms[1] += 1
    if not forms[2] and re.search(r"(0*[1-30-9]){1,2}\\(0*[1-90-2]){1,2}\\\d{4}", text):
        forms[2] += 1
    if not forms[3] and re.search(r"(0*[1-30-9]){1,2}\/(0*[1-90-2]){1,2}\/\d{4}", text):
        forms[3] += 1
    if not forms[4] and re.search(r"(0*[1-30-9]){1,2}\.(0*[1-90-2]){1,2}\.\d{2}", text):
        forms[4] += 1
    if not forms[5] and re.search(r"(0*[1-30-9]){1,2}-(0*[1-90-2]){1,2}-\d{2}", text):
        forms[5] += 1
    if not forms[6] and re.search(r"(0*[1-30-9]){1,2}\.(0*[1-90-2]){1,2}\.\d{4}", text):
        forms[6] += 1
    if not forms[7] and re.search(r"(0*[1-30-9]){1,2}-(0*[1-90-2]){1,2}-\d{4}", text):
        forms[7] += 1
    if not forms[8] and re.search(r"(0*[1-30-9]){1,2},*\s*(" + months + ")(\u056B|\u053B)?,*\s*\d{4}", text):
        forms[8] += 1
    return forms