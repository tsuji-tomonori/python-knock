from src.count_sales import Sale, count_sales


# サンプル1
def test_basic():
    sales = [
        Sale("Tokyo", "Credit", "Apple", 3),
        Sale("Tokyo", "Cash", "Apple", 2),
        Sale("Osaka", "Credit", "Apple", 5),
        Sale("Tokyo", "Credit", "Apple", 1),
        Sale("Osaka", "Credit", "Orange", 4),
        Sale("Tokyo", "Cash", "Banana", 2),
        Sale("Tokyo", "Credit", "Apple", 2),
    ]

    assert count_sales(sales) == {
        ("Tokyo", "Credit", "Apple"): 6,  # 3 + 1 + 2
        ("Tokyo", "Cash", "Apple"): 2,  # 2
        ("Osaka", "Credit", "Apple"): 5,  # 5
        ("Osaka", "Credit", "Orange"): 4,  # 4
        ("Tokyo", "Cash", "Banana"): 2,  # 2
    }


# サンプル2
def test_empty():
    sales = []
    assert count_sales(sales) == {}


# サンプル3
def test_multiple_payment_methods():
    sales = [
        Sale("Tokyo", "Credit", "Apple", 4),
        Sale("Tokyo", "Cash", "Apple", 5),
        Sale("Tokyo", "Credit", "Apple", 3),
        Sale("Tokyo", "MobilePay", "Apple", 2),
    ]

    assert count_sales(sales) == {
        ("Tokyo", "Credit", "Apple"): 7,  # 4 + 3
        ("Tokyo", "Cash", "Apple"): 5,  # 5
        ("Tokyo", "MobilePay", "Apple"): 2,  # 2
    }
