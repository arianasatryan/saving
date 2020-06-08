from typing import List, Tuple
import stanza
#from config import STANZA_MODEL_HY

STANZA_MODEL_HY="C:\\Users\\hekpo\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\stanza\\"

class KarasModel(object):

    def __init__(self, hyperparams, features):
        self.nlp = stanza.Pipeline('hy', dir=STANZA_MODEL_HY)
        self.features = features

    def train(self, train_set: List[Tuple[str, dict]], dev_set: List[Tuple[str, dict]]):
        pass

    def test(self, test_set: List[Tuple[str, dict]]):
        docs = [x for x, y in test_set]
        pred_results = self.analyse_documents(docs)
        return sum([test[1] == pred for test, pred in zip(test_set, pred_results)]) / len(test_set)

    def analyse_documents(self, documents: List[str]):
        results = []
        for document in documents:
            doc = self.nlp(document)
            features = self.features([[(w.text, w.lemma, w.pos, w.deprel) for w in sent.word] for sent in doc.sentences])
            results += self._analyse(features)

    def _analyse(self, features: List[float]):
        # replace with the implementation of the actual model
        return {
            "style_change": True,
            "style_breaches": []
        }


model=KarasModel()
