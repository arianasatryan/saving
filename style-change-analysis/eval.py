# -*- coding: utf-8 -*-
import sys
import json
from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA

"""Configuration example:
```
{
  "tasks":["style_change", "style_breach"],
  "model": {
    "name": "karas",  # other options: "zlatkova", "nath", "pnb", "lof", "ac"
    "hyperparams": {
      ...  # list of hyperparams and their values
    }
  }
  "features": {
    "extractors": [],  # if not empty, should specify feature groups
    "selection": false,  # if true, performs feature selection
    "pca": false  # if true, performs dimensionality reduction using PCA
  },
  "datasets": {
    "train": "",  # path to train dataset
    "dev": "",  # path to development dataset
    "test": []  # paths to test datasets
  }
}
```
"""


methods = {
    "zlatkova": None,
    "nath": None,
    "karas": None,
    "pnb": None,
    "lof": None,
    "ac": None
}

feature_extractors = {
    "char_punct": None,
    "char_other": None,
    "word_abbrev": None,
    "word_num": None,
    "word_ngrams": None,
    "word_others": None,
    "sent_morph": None,
    "sent_syntax": None,
    "sent_other": None,
    "p_readiblity": None
}


def feature_selection(features):
    selector = VarianceThreshold()  # selects all features with non-zero variance
    return lambda x: selector.fit_transform(features(x))


def pca(features):
    reducer = PCA()  # picks all principal components
    return lambda x: reducer.fit_transform(features(x))


def process_results(results):
    print("style change task: accuracy = {}".format(results))


def eval(config):
    features = [feature_extractors[extractor] for extractor in config["features"]["extractors"]]
    if config["features"]["selection"]:
        features = [feature_selection(feature) for feature in features]
    if config["features"]["pca"]:
        features = pca(features)

    method = methods[config["method"]["name"]]
    model = method(config["method"]["hyperparams"], features)
    if method["trainable"]:
        model.train(config["datasets"]["train"], config["datasets"]["dev"])
    results = model.test(config["datasets"]["test"])

    process_results(results)


if __name__ == "__main__":
    with open(sys.argv[1], "r", encoding="utf8") as config_json:
        config = json.load(config_json)
    eval(config)
