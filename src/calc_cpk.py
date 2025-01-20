from typing import NamedTuple


class Param(NamedTuple):
    usl: float  # 規格上限値
    lsl: float  # 規格下限値
    data: list[float]  # 工程データ


def calc_cpk(param: Param) -> float:
    """
    工程能力指数を計算する関数.

    Args:
        param (Param): 計算に必要な値

    Returns:
        float: 工程能力指数(Cpk)を小数点以下3桁で四捨五入した値
                問題文サンプルに合わせて 2.626 のように3桁で返します）
    """
    ...
