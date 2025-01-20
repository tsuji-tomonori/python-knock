from src.calc_cpk import Param, calc_cpk


def test_basic_1():
    """
    問題文に記載のサンプルテスト
    """
    param = Param(
        usl=10.0,
        lsl=2.0,
        data=[4.5, 5.0, 4.8, 5.2, 5.5]
    )
    assert calc_cpk(param) == 2.626
