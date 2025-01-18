# 問題(09B): 会議室予約システム

## 問題

ある会社では、複数の会議室を予約するためのシステムを構築しようとしています。
各会議室は特定の時間帯に予約することができ、予約が重ならないように管理する必要があります。
与えられた予約リクエストに対して、どの予約が受理され、どの予約が拒否されるかを判定してください。

## 入力フォーマット

以下の `RoomReservation` クラスを実装してください。

```python
from typing import NamedTuple, List


class Reservation(NamedTuple):
    room_id: int  # 会議室ID (1 <= room_id <= 100)
    start_time: int  # 予約開始時間 (0 <= start_time < end_time <= 1000)
    end_time: int  # 予約終了時間 (start_time < end_time <= 1000)


class RoomReservation:
    def __init__(self):
        """会議室予約システムの初期化"""
        pass

    def request_reservation(self, reservation: Reservation) -> bool:
        """
        会議室の予約をリクエストする。

        予約が承認される場合は True を返し、拒否される場合は False を返す。

        Args:
            reservation (Reservation): 予約リクエストの情報。

        Returns:
            bool: 予約が受理された場合 True、拒否された場合 False。
        """
        pass
```

## 入力条件

- `room_id` は 1 以上 100 以下の整数。
- `start_time` と `end_time` は 0 以上 1000 以下の整数で、`start_time < end_time` が常に成り立つ。
- 各予約は 1 つの会議室 (`room_id`) に対して行われる。
- 会議室ごとに予約が管理され、予約時間が重複する場合、新しい予約リクエストは拒否される。

## 出力フォーマット

各予約リクエストが受理された場合は `True` を、拒否された場合は `False` を返します。

## サンプル

### サンプル1

```python
def test_basic():
    system = RoomReservation()
    assert system.request_reservation(Reservation(1, 10, 20)) == True  # 予約成功
    assert system.request_reservation(Reservation(1, 15, 25)) == False  # 時間が重複しているため拒否
    assert system.request_reservation(Reservation(1, 20, 30)) == True  # 予約成功
    assert system.request_reservation(Reservation(2, 10, 20)) == True  # 別の会議室なので予約成功
    assert system.request_reservation(Reservation(2, 15, 25)) == False  # 会議室2の予約が重複
```

### サンプル2

```python
def test_edge_cases():
    system = RoomReservation()
    assert system.request_reservation(Reservation(1, 0, 500)) == True  # 長時間予約成功
    assert system.request_reservation(Reservation(1, 500, 1000)) == True  # 予約時間が連続するが重ならない
    assert system.request_reservation(Reservation(1, 499, 501)) == False  # 予約時間が重なるため拒否
```

## 解説

- 予約は `room_id` ごとに管理され、各会議室には独立した予約リストが存在する。
- `start_time` と `end_time` の範囲が他の予約と重複する場合、新しい予約は拒否される。
- `end_time` がちょうど既存の予約の `start_time` と同じ場合は重複しないため予約可能。
