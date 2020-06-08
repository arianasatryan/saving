from feature_extraction.utils import word_tokenize

def is_long_word_accured(text: str):
    words = word_tokenize(text)
    all_words_len = sum(len(word)for word in words)
    avg_len = all_words_len/len(words)
    for word in words:
        if len(word) > avg_len:
            return [1.0]
    return [0.0]

def long_words_portion(text: str):
    words = word_tokenize(text)
    all_words_len = sum(len(word) for word in words)
    avg_len = all_words_len / len(words)
    accured_long_words = 0
    for word in words:
        if len(word) > avg_len:
            accured_long_words += 1
    return [float(accured_long_words/len(words))] if len(words)!=0 else [0.0]

