from  feature_extraction.utils import word_tokenize
import re

punct_regex = r'[^\d\s\u0561-\u0587\u0531-\u0556]'

#punctation
def contains_punct(text: str, punct: str=None):
    if not punct:
        if not re.search(punct_regex, text):
            return [1.0]
    else:
        if text.find(punct) != -1:
            return [1.0]
    return [0.0]

def punct_portion(text: str, punct: str=None):
    words = word_tokenize(text)
    punct_count = len(re.findall(punct_regex, text)) if not punct else text.count(punct)
    return [float(punct_count / len(words))] if words else [0.0]

def contains_before_spaced_punct(text: str, punct: str=None):
    iter = re.finditer(punct_regex, text) if not punct else re.finditer(punct, text)
    indices = [m.start(0) for m in iter]
    for index in indices:
        if index != 0 and text[index-1] == ' ':
            return [1.0]
    return [0.0]

def contains_after_spaced_punct(text: str, punct: str=None):
    iter = re.finditer(punct_regex, text) if not punct else re.finditer(punct, text)
    indices = [m.start(0) for m in iter]
    for index in indices:
        if index != len(text)-1 and text[index + 1] == ' ':
            return [1.0]
    return [0.0]

def before_spaced_punct_portion(text: str, punct: str=None):
    iter = re.finditer(punct_regex, text) if not punct else re.finditer(punct, text)
    indices = [m.start(0) for m in iter]
    before_spaced_count = 0
    for index in indices:
        if index != 0 and text[index-1] == ' ':
            before_spaced_count += 1
    return [float(before_spaced_count / len(indices))] if len(indices) != 0 else [0.0]

def after_spaced_punct_portion(text: str, punct: str=None):
    iter = re.finditer(punct_regex, text) if not punct else re.finditer(punct, text)
    indices = [m.start(0) for m in iter]
    after_spaced_count = 0
    for index in indices:
        if index != len(text)-1 and text[index + 1] == ' ':
            after_spaced_count += 1
    return [float(after_spaced_count / len(indices))] if len(indices) != 0 else [0.0]
