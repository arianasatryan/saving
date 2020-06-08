from src.algorithms.threshold_clustering.executor import execute_threshold_clustering
from typing import List
import preprocess_NLP_pkg


def analyse_documents(documents: List[str]) -> List[dict]:
    result_dict = []
    for text in documents:
        prediction_TBC = execute_threshold_clustering(text, merge_threshold=50, add_node_threshold=50,
                                                      prune=True, number_of_terms=50,
                                                      distance_measure=preprocess_NLP_pkg.clark_distance,
                                                      use_duplication_feature=False)
        result_dict.append({"style_change": bool(prediction_TBC > 1)})
    return result_dict
