from typing import List
import operator
import scipy.sparse as sp
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from sklearn.feature_extraction.text import TfidfVectorizer
from information import get_starts_of_paragraphs, get_paragraphs_of, breaches_from_borders

def borders_by_AC(paragraphs: list, starts:dict , dataframe: pd.DataFrame, n_clusters: int, linkage: str, affinity: float) -> list:
    style_change_borders = []
    starts_of_paragraphs = starts
    if len(paragraphs) > 1:
            if linkage == 'ward':
                affinity = 'euclidean'
            if len(paragraphs)>n_clusters:
                model = AgglomerativeClustering(n_clusters = n_clusters, linkage = linkage, affinity = affinity)
                clusters = model.fit_predict(dataframe)
                for i in range(len(clusters) - 1):
                    if clusters[i] != clusters[i + 1]:
                        style_change_borders.append(starts_of_paragraphs[i + 1 + 1])        # +1 cause the numeration of paragraphs starts at 1
    return style_change_borders

def method_for_text(text: str , features: List[str], hyperparams: list) -> dict:
    # text segmentation
    paragraphs = get_paragraphs_of(text)                                                    # use this for regular files
    starts_of_paragraphs = get_starts_of_paragraphs(paragraphs)                             # use this for regular files
    #starts_of_paragraphs = annot_get_starts_of_paragraphs(paragraphs)                      # use this for annotated '#Text=' files
    #paragraphs = annot_get_paragraphs_of(texts)                                            # use this for annotated '#Text=' files


    # style fingerprints by features
    #!!!!!!!!!!define dataframe


    vectors = sp.hstack((item for item in used_features_vecs), format='csr')
    denselist = (vectors.todense()).tolist()
    df = pd.DataFrame(data=denselist)


    # used outlier detection  method
    n_clusters = hyperparams[0] if not hyperparams else 1.0
    linkage = hyperparams[1] if not  hyperparams else 0.05


    style_change_borders = borders_by_AC(paragraphs = paragraphs, )

    # result format correction
    style_breaches = [] if not style_change_borders else breaches_from_borders(style_change_borders,len(text))
    result_dict = {}
    result_dict['style_change'] = True if style_change_borders else False
    result_dict['style_breaches'] = style_breaches
    return result_dict

def main(data: List[str]) -> List[dict]:
    all_results = []
    for text in data:
        all_results.append(method_for_text(text=text,features=None,hyperparams=[1,0.05]))
    return all_results






