from src.simulate_langtons_ant import simulate_langtons_ant


def test_steps_0():
    """
    サンプル1: ステップ数0
    まだ移動していないため、黒いマスは存在しない。
    出力: []
    """
    assert simulate_langtons_ant(0) == []


def test_steps_1():
    """
    サンプル2: ステップ数1
    初期位置(0, 0)が白→黒になり右折して(1, 0)へ。
    黒いマスは[(0, 0)]。
    """
    assert simulate_langtons_ant(1) == [(0, 0)]


def test_steps_5():
    """
    サンプル3: ステップ数5
    黒いマスのリスト: [(0, -1), (1, -1), (1, 0)]
    """
    assert simulate_langtons_ant(5) == [(0, -1), (1, -1), (1, 0)]
