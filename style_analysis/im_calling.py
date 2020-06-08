#from feature_extraction.tokenizers import word_tokenize
from feature_extraction.word_abbrev import mostly_lowercased_starts





with open('/Users/hekpo/Desktop/try/problem-6959.txt','r',encoding='utf-8')as fin:
    text=fin.read()
    print(mostly_lowercased_starts(text))



