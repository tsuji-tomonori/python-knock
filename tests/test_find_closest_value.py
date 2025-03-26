from src.find_closest_value import find_closest_value


def test_sample1():
    # サンプル1
    # [1, 3, 5, 7, 9] において target=6 のとき最も近い値は 5 または 7。
    # ただし小さい方の 5 を返す。
    arr = [1, 3, 5, 7, 9]
    target = 6
    assert find_closest_value(arr, target) == 5


def test_sample2():
    # サンプル2
    # [2, 4, 6, 8, 10] において target=7 のとき最も近い値は 6 または 8。
    # ただし小さい方の 6 を返す。
    arr = [2, 4, 6, 8, 10]
    target = 7
    assert find_closest_value(arr, target) == 6


def test_sample3():
    # サンプル3
    # [1, 2, 3, 4, 5] において target=10 のとき最も近い値は 5。
    arr = [1, 2, 3, 4, 5]
    target = 10
    assert find_closest_value(arr, target) == 5


def test_sample4():
    # サンプル4
    # [-10, -5, 0, 5, 10] において target=-7 のとき最も近い値は -5。
    arr = [-10, -5, 0, 5, 10]
    target = -7
    assert find_closest_value(arr, target) == -5


def test_sample5():
    # サンプル5
    # [10] において target=7 のとき配列に 10 しかないので 10 を返す。
    arr = [10]
    target = 7
    assert find_closest_value(arr, target) == 10
