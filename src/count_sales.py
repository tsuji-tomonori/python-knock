from typing import NamedTuple


class Sale(NamedTuple):
    store: str  # 店舗名
    payment_method: str  # 支払い方法
    product: str  # 商品名
    quantity: int  # 売上数量（1以上の整数）


def count_sales(sales: list[Sale]) -> dict[tuple[str, str, str], int]:
    """
    各 (店舗名, 支払い方法, 商品名) ごとの売上数量を集計する関数.

    Args:
        sales (list[Sale]): 売上データのリスト

    Returns:
        dict[tuple[str, str, str], int]: (店舗名, 支払い方法, 商品名) をキーとし、売上数量を値とする辞書
    """
    ...
