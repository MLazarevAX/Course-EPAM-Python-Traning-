from typing import List
import re

def count_words(sentences: List[str], word: str) -> int:
    '''
    The Function counts the number of uses of a given word in a list of strings
    :param sentences: List[str]
    :param word: str
    :return: int
    '''
    find_string = ' '.join(sentences)
    substring_re = fr'{word}'
    return len(re.findall(substring_re, find_string))
