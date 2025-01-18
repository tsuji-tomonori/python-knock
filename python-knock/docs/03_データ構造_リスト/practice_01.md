# 問題(03A): 時間単位での接続数の集計

## 問題

あるテレビ番組の視聴デバイスの接続数を一定の期間ごとに集計したいとします。

各デバイスがテレビ番組を視聴する際、接続や切断の情報がサーバーに記録されます。この記録をもとに、指定した時間範囲内の各期間ごとの接続数を求めてください。

サーバーには、以下の形式で接続情報がログとして保存されています。

- **時刻 (time)**: 接続・切断のアクションが発生した時間（単位は整数で、0 以上 1000 以下）。
- **新規接続端末数 (n\_connect)**: この時間に新たに接続した端末の数。
- **新規切断端末数 (n\_disconnect)**: この時間に切断された端末の数。

指定された時刻の範囲に対して、一定間隔での接続数を出力する関数を実装してください。

## 入力フォーマット

以下の count_connections 関数を実装してください。

```python
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
```


### 入力値の条件

- end_time (int): `0 <= end_time <= 1000`
  - end_time は接続ログの集計を行う終了時間を表します。
- period (int): `1 <= period <= end_time`
  - period は集計する間隔で、end_time より大きいことはありません。
- logs (list[Log]): 接続と切断の情報を含むログデータのリストです。
  - ログの各エントリ (Log):
    - time (int): `0 <= time <= end_time`
      - 各ログは end_time の範囲内の時刻で記録されます。
      - 同一時刻のログは存在しないものとします（各時刻には1つのログのみが存在します）。
    - n_connect (int): `0 <= n_connect`
      - 新規接続した端末の台数を示します。
    - n_disconnect (int): `0 <= n_disconnect`
      - 新規切断した端末の台数を示します。
      - n_disconnect はその時刻における合計接続数を超えることはありません。

### 接続数についての条件

- 接続数は 0 より小さくならないものとします。
- 時刻 0 のタイミングでログが存在しない場合、接続数は 0 として扱います。

## 出力フォーマット

- **list[int]**: 指定された時間の範囲を period の間隔ごとに分割し、各期間の接続数をリストとして出力します。

各期間の接続数は、時刻 0 から end_time までの接続および切断の情報をもとに計算します。リストの各要素は、各 period ごとの時刻における接続数を示します。

## サンプル

### サンプル1

以下は count_connections 関数の動作例です。

```python
import src.itp2_1e as t

def test_basic():
    param = t.Param(
        end_time=5,
        period=1,
        logs=[
            t.Log(0, 3, 0),  # 時刻 0 に 3 台の端末が接続
            t.Log(1, 2, 0),  # 時刻 1 に 2 台の端末が接続
            t.Log(4, 5, 2),  # 時刻 4 に 5 台接続、2 台切断
            t.Log(5, 3, 5),  # 時刻 5 に 3 台接続、5 台切断
        ]
    )
    assert t.count_connections(param) == [3, 5, 5, 5, 8, 6]
```

#### サンプル1解説

- **時刻 0**: 3 台接続 → 合計接続数 3
- **時刻 1**: 2 台接続 → 合計接続数 5
- **時刻 2, 3**: ログがないため、接続数は変わらず **5**。
- **時刻 4**: 5 台接続、2 台切断 → 合計接続数 8
- **時刻 5**: 3 台接続、5 台切断 → 合計接続数 6

各 period 毎の接続数のリストとして、 [3, 5, 5, 5, 8, 6] を返します。

ログがない期間については、直前の接続数をそのまま引き継ぎます。このため、時刻 2 と 3 の接続数は時刻 1 と同じく 5 となります。

### サンプル2

```python
import src.itp2_1e as t

def test_with_no_logs():
    param = t.Param(
        end_time=3,
        period=1,
        logs=[]  # ログがない場合
    )
    assert t.count_connections(param) == [0, 0, 0, 0]
```

#### サンプル2解説

- **test\_with\_no\_logs**: ログが全くない場合は、すべての時刻における接続数は 0 となります。そのため、[0, 0, 0, 0] を返します。

### サンプル3

```python
import src.itp2_1e as t

def test_with_gap_logs():
    param = t.Param(
        end_time=6,
        period=2,
        logs=[
            t.Log(1, 4, 0),  # 時刻 1 に 4 台の端末が接続
            t.Log(3, 1, 1),  # 時刻 3 に 1 台接続、1 台切断
            t.Log(6, 3, 2),  # 時刻 6 に 3 台接続、2 台切断
        ]
    )
    assert t.count_connections(param) == [0, 4, 4, 5]
```

#### サンプル3解説

- **test\_with\_gap\_logs**:
  - **時刻 0, 2, 4, 5**: ログがないため、直前の接続数を引き継ぎます。
  - **時刻 1**: 4 台接続 → 合計接続数 4
  - **時刻 3**: 1 台接続、1 台切断 → 合計接続数 4
  - **時刻 6**: 3 台接続、2 台切断 → 合計接続数 5
  - 集計間隔 period=2 のため、時刻 0、2、4、6 における接続数を出力し、[0, 4, 4, 5] を返します。
