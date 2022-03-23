from typing import List
import re



def hash_names(names: List[str]) -> List[int]:
    """
    Function takes a list of strings and returns a list of their (strings) hashes.
    :param names: List[str]
    :return: List[int]
    """
    return list(map(hash, names))





