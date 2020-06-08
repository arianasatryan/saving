from feature_extraction.utils import sentence_tokenize, word_tokenize

#by simbols
def sent_count(text: str):
    return [float(len(sentence_tokenize(text)))]

def min_sent_len_by_simbols(text: str):
    sents = sentence_tokenize(text)
    return [float(len(min(sents,key=len)))]

def max_sent_len_by_simbols(text: str):
    sents = sentence_tokenize(text)
    return [float(len(max(sents,key=len)))]

def avg_sent_len_by_simbols(text: str):
    sents = sentence_tokenize(text)
    all_sents_len = sum(len(sent)for sent in sents)
    return [float(all_sents_len / len(sents))] if sents else [0.0]

def is_short_sent_by_simbols_accured(text: str):
    sents = sentence_tokenize(text)
    avg_sent_len = avg_sent_len_by_simbols(text)[0]
    for sent in sents:
        if len(sent) <= avg_sent_len:
            return [1.0]
    return [0.0]

def is_long_sent_by_simbols_accured(text: str):
    sents = sentence_tokenize(text)
    avg_sent_len = avg_sent_len_by_simbols(text)[0]
    for sent in sents:
        if len(sent) > avg_sent_len:
            return [1.0]
    return [0.0]

def short_sents_by_simbols_portion(text: str):
    sents = sentence_tokenize(text)
    avg_sent_len = avg_sent_len_by_simbols(text)[0]
    short_sent_count = 0
    for sent in sents:
        if len(sent) <= avg_sent_len:
            short_sent_count += 1
    return [float(short_sent_count / len(sents))] if sents else [0.0]

def long_sents_by_simbols_portion(text: str):
    sents = sentence_tokenize(text)
    avg_sent_len = avg_sent_len_by_simbols(text)[0]
    long_sent_count = 0
    for sent in sents:
        if len(sent) > avg_sent_len:
            long_sent_count += 1
    return [float(long_sent_count / len(sents))] if sents else [0.0]


#by words
def min_sent_len_by_words(text: str):
    sents = sentence_tokenize(text)
    sents_words = [word_tokenize(sent) for sent in sents]
    return [float(len(min(sents_words,key=len)))]

def max_sent_len_by_words(text: str):
    sents = sentence_tokenize(text)
    sents_words = [word_tokenize(sent) for sent in sents]
    return [float(len(max(sents_words,key=len)))]

def avg_sent_len_by_words(text: str):
    sents = sentence_tokenize(text)
    sents_words = [word_tokenize(sent) for sent in sents]
    all_sents_words = sum(len(sent_words) for sent_words in sents_words)
    return [float(all_sents_words / len(sents))] if sents else [0.0]

def is_short_sent_by_words_accured(text: str):
    sents = sentence_tokenize(text)
    avg_sent_len = avg_sent_len_by_words(text)[0]
    for sent in sents:
        if len(word_tokenize(sent)) <= avg_sent_len:
            return [1.0]
    return [0.0]

def is_long_sent_by_words_accured(text: str):
    sents = sentence_tokenize(text)
    avg_sent_len = avg_sent_len_by_words(text)[0]
    for sent in sents:
        if len(word_tokenize(sent)) > avg_sent_len:
            return [1.0]
    return [0.0]

def short_sents_by_words_portion(text: str):
    sents = sentence_tokenize(text)
    avg_sent_len = avg_sent_len_by_words(text)[0]
    short_sent_count = 0
    for sent in sents:
        if len(word_tokenize(sent)) <= avg_sent_len:
            short_sent_count += 1
    return [float(short_sent_count / len(sents))] if sents else [0.0]

def long_sents_by_words_portion(text: str):
    sents = sentence_tokenize(text)
    avg_sent_len = avg_sent_len_by_words(text)[0]
    short_sent_count = 0
    for sent in sents:
        if len(word_tokenize(sent)) > avg_sent_len:
            short_sent_count += 1
    return [float(short_sent_count / len(sents))] if sents else [0.0]
