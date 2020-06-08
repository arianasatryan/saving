from feature_extraction.utils import word_tokenize

def get_suffixes_list():
    return open('external_data/suffixes.txt','r',encoding='utf-8').read().splitlines()

def get_prefixes_list():
    return open('external_data/suffixes.txt','r',encoding='utf-8').read().splitlines()

def suffixed_words_portion(text: str,suffix: str=None):
    words = word_tokenize(text)
    suffixed_count = 0
    if not suffix:
        suffix_list = get_suffixes_list()
        for word in words:
            for suffix in suffix_list:
                if word.endswith(suffix):
                    suffixed_count += 1
    else:
        for word in words:
            if word.endswith(suffix):
                suffixed_count += 1
    return [float(suffixed_count / len(words))] if words else [0.0]

def prefixed_words_portion(text: str,prefix: str=None):
    words = word_tokenize(text)
    prefixed_count = 0
    if not prefix:
        prefix_list = get_prefixes_list()
        for word in words:
            for prefix in prefix_list:
                if word.startswith(prefix):
                    prefixed_count += 1
    else:
        for word in words:
            if word.startswith(prefix):
                prefixed_count += 1
    return [float(prefixed_count / len(words))] if words else [0.0]