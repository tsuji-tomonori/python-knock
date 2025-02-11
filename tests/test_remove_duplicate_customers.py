from src.remove_duplicate_customers import remove_duplicate_customers


def test_sample1():
    """
    サンプルテストケース1:
    [101, 202, 303, 101, 404, 202, 505] → (101, 202, 303, 404, 505)
    """
    customer_ids = [101, 202, 303, 101, 404, 202, 505]
    expected = (101, 202, 303, 404, 505)
    assert remove_duplicate_customers(customer_ids) == expected


def test_sample2():
    """
    サンプルテストケース2:
    [1, 2, 3, 4, 5, 6, 7, 8, 9] → (1, 2, 3, 4, 5, 6, 7, 8, 9)
    """
    customer_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    expected = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    assert remove_duplicate_customers(customer_ids) == expected


def test_sample3():
    """
    サンプルテストケース3:
    [42, 42, 42, 42, 42] → (42,)
    """
    customer_ids = [42, 42, 42, 42, 42]
    expected = (42,)
    assert remove_duplicate_customers(customer_ids) == expected


def test_sample4():
    """
    サンプルテストケース4:
    [] → ()
    """
    customer_ids = []
    expected = ()
    assert remove_duplicate_customers(customer_ids) == expected


def test_sample5():
    """
    サンプルテストケース5:
    [500, -1, 500, -1, 200, 300, 200, -100] → (500, -1, 200, 300, -100)
    """
    customer_ids = [500, -1, 500, -1, 200, 300, 200, -100]
    expected = (500, -1, 200, 300, -100)
    assert remove_duplicate_customers(customer_ids) == expected
