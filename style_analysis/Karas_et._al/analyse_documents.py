from typing import List
from .Karas import main

def analyse_documents(documents: List[str]) -> List[dict]:
    result_list = main(data=documents)
    return result_list
