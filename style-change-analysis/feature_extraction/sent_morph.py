from feature_extraction.utils import pos_tagger
from nltk import ngrams
import ctypes

ctypes.cdll.LoadLibrary('caffe2_nvrtc.dll')


def pos_ngram_portion(text: str,searched_pos_ngram: tuple):
    n = len(searched_pos_ngram)
    POSes = pos_tagger(text)
    res_pos_ngrams = ngrams([POS for POS in POSes], n)
    accured_count = 0
    for pos_ngam in res_pos_ngrams:
        if pos_ngam == searched_pos_ngram:
            accured_count += 1
    return [float(accured_count / (len(POSes)-n-1))] if len(POSes)-n-1 != 0 else [0.0]
