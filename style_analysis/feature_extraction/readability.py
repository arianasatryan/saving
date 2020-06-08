rom utils import word_tokenize, letter_tokenize, letters_and_numbers, remove_punct, sentence_tokenize, syllables_counter
import math


def flesch_reading_ease(text: str):
    words_count = len(word_tokenize(text))
    syllables_count = syllables_counter(text)
    sentences_count = len(sentence_tokenize(text))
    try:
        FSE = 78.39 + 2.6 * (words_count / sentences_count) - 32.3 * (syllables_count / words_count)
    except ZeroDivisionError:
        return 0.0
    return [round(FSE, 2)]


def smog_index(text: str):
    syllables_count = syllables_counter(text)
    sentences_count = len(sentence_tokenize(text))
    try:
        smog = 0.6 * math.sqrt(syllables_count / sentences_count) + 9.0
    except ZeroDivisionError:
        return 0.0
    return [round(smog, 2)]


def flesch_kincaid_grade(text: str):
    words_count = len(word_tokenize(text))
    syllables_count = syllables_counter(text)
    sentences_count = len(sentence_tokenize(text))
    try:
        FK = -0.33 * (words_count / sentences_count) + 6.42 * (syllables_count / words_count) + 4.7
    except ZeroDivisionError:
        return 0.0
    return [round(FK, 2)]


def coleman_liau_index(text: str):
    letters_count = len(letter_tokenize(text))
    words_count = len(word_tokenize(text))
    sentences_count = len(sentence_tokenize(text))
    try:
        CL = 1.2 * (letters_count / words_count) + 62.65 * (sentences_count / words_count) + 0.662
    except ZeroDivisionError:
        return 0.0
    return [round(CL, 2)]


def automated_readability_index(text: str):
    letters_and_nums_count = len(letters_and_numbers(text))
    words_count = len(word_tokenize(text))
    sentences_count = len(sentence_tokenize(text))
    try:
        AT = 3.062 * (letters_and_nums_count / words_count) - 0.049 * (words_count/sentences_count) + 0.078
    except ZeroDivisionError:
        return 0.0
    return [round(AT, 2)]


def dale_chall_readability_score(text: str):
    words = word_tokenize(text)
    words_count = len(words)
    c = 0.0
    for word in words:
        if syllables_counter(word) > 3:
            c += 1
    count = words_count - c
    try:
        per = count / (words_count * 100)
    except ZeroDivisionError:
        return 0.0
    difficult_words = 100 - per
    score = ((0.1579 * difficult_words) + (0.0496 * words_count / len(sentence_tokenize(text))))
    if difficult_words > 5:
        score += 3.6365
    return [round(score, 2)]


def linsear_write_formula(text: str):
    words = word_tokenize(text)[:100]
    sentences_count = len(sentence_tokenize(' '.join(words)))
    c1 = 0.0
    c3 = 0.0
    for word in words:
        if syllables_counter(word) < 3:
            c1 = c1 + 1
        else:
            c3 = c3 + 1
    try:
        lin = (c1 + c3) / sentences_count
    except ZeroDivisionError:
        return 0.0
    return [round(lin, 2)]


def difficult_words(text: str):
    c = 0.0
    for word in word_tokenize(text):
        if syllables_counter(word) > 3:
            c += 1
    return [c]


def gunning_fog(text: str):
    words = word_tokenize(text)
    words_count = len(words)
    sentences_count = len(sentence_tokenize(text))
    c = 0.0
    for word in words:
        if syllables_counter(word) > 3:
            c += 1
    try:
        GF = 0.4 * (words_count / sentences_count + 100 * (c / words_count))
    except ZeroDivisionError:
        return 0.0
    return [round(GF, 2)]