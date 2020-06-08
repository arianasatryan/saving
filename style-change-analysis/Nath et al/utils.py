import spacy_udpipe
import stanza


nlp_stanza = stanza.Pipeline(lang='hy', dir='/path/to/stanza/model', processors='tokenize, pos, lemma')
nlp_udpipe = spacy_udpipe.load_from_path(lang="hy",
                                         path='/path/to/udpipe/model',
                                         meta={"description": "Custom 'hy' model"})


def lemmatize(text):
    doc = nlp_stanza(text)
    return [word.lemma for sentence in doc.sentences for word in sentence.words]


def sentence_tokenizer(text):
    doc = nlp_udpipe(text)
    return [x.string for x in list(doc.sents)]
