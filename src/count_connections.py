from typing import NamedTuple


class Log(NamedTuple):
    time: int  # 時刻 0 <= time <= 1000, 同一時刻のログは存在しない
    n_connect: int  # 新規接続台数 0 <= n_connect
    n_disconnect: int  # 新規切断台数 0 <= n_disconnect, 合計接続数を超えない


class Param(NamedTuple):
    end_time: int  # 集計終了時刻 0 <= end_time <= 1000
    period: int  # 集計間隔 1 <= period <= end_time
    logs: list[Log]  # ログデータ


def count_connections(param: Param) -> list[int]:
    """
    ある期間ごとの接続数を出力する関数.
    接続数は0より小さくならない。また、時刻0にログがない場合は接続数は0として扱う。

    Args:
        param (Param): 接続情報

    Returns:
        list[int]: ある期間ごとの接続数
    """
    ...
