import pytest
from main import Book

price = 100.1
book = Book("William Faulkner", "The Sound and the Fury", 12)


@pytest.mark.parametrize(
    "price", [100.1, 102, 101, 120, -1, -100]
)
def test_book_price_with_error(price, book=book):
    with pytest.raises(ValueError):
        book.price = price
