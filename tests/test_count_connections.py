from src.count_connections import Param, Log, count_connections


def test_basic():
    """
    基本的なテストケース。
    時刻ごとの接続数をテストする。
    end_time=5, period=1 で複数のログを使用して接続数を集計。
    結果として [3, 5, 5, 5, 8, 6] が期待される。
    """
    param = Param(
        end_time=5,
        period=1,
        logs=[
            Log(0, 3, 0),
            Log(1, 2, 0),
            Log(4, 5, 2),
            Log(5, 3, 5),
        ],
    )
    assert count_connections(param) == [3, 5, 5, 5, 8, 6]


def test_no_logs():
    """
    ログが存在しない場合のテスト。
    すべての接続数が 0 であることを確認。
    """
    param = Param(end_time=3, period=1, logs=[])
    assert count_connections(param) == [0, 0, 0, 0]


def test_gap_logs():
    """
    ログの間隔にギャップがある場合のテスト。
    end_time=6, period=2 で複数のログを使用して接続数を集計。
    結果として [0, 4, 4, 5] が期待される。
    """
    param = Param(
        end_time=6,
        period=2,
        logs=[
            Log(1, 4, 0),
            Log(3, 1, 1),
            Log(6, 3, 2),
        ],
    )
    assert count_connections(param) == [0, 4, 4, 5]
