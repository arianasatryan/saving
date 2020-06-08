from typing import List
from main import main

def analyse_documents(documents: List[str]) -> List[dict]:
    predictions = main(test_data=documents)
    result_dict = [{'style_change': True if prediction == 1 else False} for prediction in predictions]
    return result_dict