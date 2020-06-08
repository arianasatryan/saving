import spacy_udpipe
import re
import stanza

PATH_TO_UDPIPE_MODEL = '/path/to/udpipe/model'
PATH_TO_STANZA_MODEL = '/path/to/stanza/model'

nlp_udpipe = spacy_udpipe.load_from_path(lang="hy",
                                  path=PATH_TO_UDPIPE_MODEL,
                                  meta={"description": "Custom 'hy' model"})
nlp_stanza = stanza.Pipeline(lang='hy', dir=PATH_TO_STANZA_MODEL, processors='tokenize, pos, lemma')


def lemmatizer(text: str):
    doc = nlp_stanza(text)
    return [word.lemma for sentence in doc.sentences for word in sentence.words]


def pos_tagger(text: str):
    doc = nlp_stanza(text)
    return [word.pos for sentence in doc.sentences for word in sentence.words]


def word_tokenize(text: str, remove_punctuation=False):
    text = remove_punct(text) if remove_punctuation else text
    doc = nlp_udpipe(text)
    return [word.text for word in doc]


def letter_tokenize(text: str):
    return list(re.sub(r'[^\u0561-\u0587\u0531-\u0556]', '', text))


def letters_and_numbers(text: str):
    return list(re.sub(r'[^\d\u0561-\u0587\u0531-\u0556]', '', text))


def remove_punct(text: str):
    return re.sub(r'[^\d\s\u0561-\u0587\u0531-\u0556]', ' ', text)


def sentence_tokenize(text: str):
    doc = nlp_udpipe(text)
    return [x.string for x in list(doc.sents)]


def syllables_counter(text: str):
    c = Counter(text)
    return c["ա"] + c["ե"] + c["է"] + c["ը"] + c["ի"] + c["ո"] + c["և"] + c["օ"]
