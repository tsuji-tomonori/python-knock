from sample.run_length_encoding import run_length_encoding


# サンプルテストケース
def test_sample1():
    # "aaabbcdddd" -> [("a", 3), ("b", 2), ("c", 1), ("d", 4)]
    assert run_length_encoding("aaabbcdddd") == [("a", 3), ("b", 2), ("c", 1), ("d", 4)]


def test_sample2():
    # "abc" -> [("a", 1), ("b", 1), ("c", 1)]
    assert run_length_encoding("abc") == [("a", 1), ("b", 1), ("c", 1)]


def test_sample3():
    # "aaaaaaa" -> [("a", 7)]
    assert run_length_encoding("aaaaaaa") == [("a", 7)]
