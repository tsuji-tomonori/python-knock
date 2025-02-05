from src.count_word_frequencies import count_word_frequencies


def test_basic():
    text = "apple banana apple orange banana apple"
    assert count_word_frequencies(text) == {"apple": 3, "banana": 2, "orange": 1}


def test_single_word():
    text = "python"
    assert count_word_frequencies(text) == {"python": 1}


def test_tied_frequencies():
    text = "dog cat bird cat dog bird"
    assert count_word_frequencies(text) == {"bird": 2, "cat": 2, "dog": 2}
