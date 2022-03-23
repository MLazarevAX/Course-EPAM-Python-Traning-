from main import count_words
import pytest



sentences = ['test for test in tests', 'nothing at all', 'testing']
word = 'test'
expected = 4


@pytest.mark.parametrize(
    "sentences,word,expected", [
        (["test for test in tests", "nothing at all", "testing"], "test", 4),
        ([], "test", 0),
        (["blablabla bla"], "bla", 4),
        (["test for test in tests"], "bla", 0),
        (["this is a random sentence", "iiii"], "i", 6),
        (["bla bla blablabla"], "blas", 0)
    ]
)
def test_count_words(sentences, word, expected):
    assert count_words(sentences=sentences, word=word) == expected
