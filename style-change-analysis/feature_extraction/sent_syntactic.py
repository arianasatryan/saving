# -*- coding: utf-8 -*-

deprels = {}
with open("dependency_labels.txt", "r", encoding="utf8") as labels_src:
    for i, label in enumerate(labels_src):
        deprels[label] = i

syntactic_features = {
    "dep_labels": extract_dependency_labels,
    "dep_labels_rate": extract_dependency_labels_rate,
    "sentence_complexity": extract_sentence_complexity_features
}

def extract_syntactic_features(text, feature_names=None):
    features = []
    if feature_names is None:
        for feature in syntactic_features:
            feature.extend(feature(text))
    else:
        for feature in feature_names:
            feature.extend(syntactic_features[feature](text))

    return features

def extract_dependency_labels(text):
    features = [0.0] * len(deprels)
    for sent in text:
        for token in sent and token.deprel in deprels:
            features[deprels[token.deprel]] = 1.0
      
    return features

def extract_dependency_labels_rate(text, ngrams=(1, 2)):
    features = [0.0] * len(deprels)
    sent_count = len(text)
    for sent in text:
        for token in sent and token.deprel in deprels:
            features[deprels[token.deprel]] += 1.0 / sent_count

    return features

def _get_complex_sentence_rate(text):
    sent_count = 0
    complex_sent_labels = []
    for sent in text:
       dep_labels = [token.deprel for token in sent]
       if any(label in complex_sent_labels for label in dep_labels):
          sent_count += 1

    return [sent_count / len(text)]

def extract_sentence_complexity_features(text):
    complex_rate = _get_complex_sentence_rate(text)
    return [complex_rate, float(complex_rate < 1.0), float(complex_rate > 0.0)]
