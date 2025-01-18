# 問題(07B): 回転寿司屋の席案内システム

## キューの基本概念

キュー（Queue）は、**先入れ先出し（FIFO: First In, First Out）** の特性を持つデータ構造です。
つまり、**最初に追加された要素が最初に取り出される** という特徴があります。

## キューの特徴

- **要素の追加（enqueue）**: 新しい要素を **後ろ（末尾）** に追加する。
- **要素の削除（dequeue）**: 先頭の要素を **取り出して削除** する。
- **先入れ先出し（FIFO）**: 追加した順に処理される。

## 問題文

回転寿司屋では、お客さんが来店すると **受付で番号を取得し、順番に席へ案内** されます。
また、満席の場合は **席が空くまで待つ** 必要があります。
このシステムを **キュー（Queue）** を用いて実装してください。

お客さんの動作は以下の 2 種類です：

1. **"arrive name"**:
   - `name` という名前のお客さんが来店し、待機リストに追加される。
   - ただし、すでに `name` が待機リストに存在する場合は追加しない。

2. **"seat N"**:
   - `N` 席が空いたため、**待機リストの先頭から順に `N` 人が席へ案内** される。
   - もし待機リストが `N` 人未満の場合は、**全員が席へ案内** される。

## 入力フォーマット

以下の `sushi_seating` 関数を実装してください。

```python
from typing import List

def sushi_seating(commands: List[str]) -> List[str]:
    """
    回転寿司屋の席案内システムを実装する関数。

    Args:
        commands (List[str]): 到着・席案内のコマンドリスト

    Returns:
        List[str]: 案内されたお客さんのリスト
    """
    ...
```

### 入力値の条件

- `commands` の各要素は以下の形式のいずれかである：
  - `"arrive name"` (`name` は英数字の文字列)
  - `"seat N"` (`N` は `1 <= N <= 100`)
- `1 <= len(commands) <= 1000`
- 同じ `name` のお客さんが **複数回 "arrive" することはない**
- `"seat"` コマンドは待機リストが空でも実行可能（この場合は何もしない）

## 出力フォーマット

- 席へ案内されたお客さんの名前を、案内順に **リスト** で出力してください。

---

## サンプル

### サンプル1

```python
commands = [
    "arrive Alice",
    "arrive Bob",
    "seat 1",
    "arrive Charlie",
    "seat 2",
    "arrive Dave",
    "arrive Eve",
    "seat 3"
]

assert sushi_seating(commands) == ["Alice", "Bob", "Charlie", "Dave", "Eve"]
```

#### サンプル1解説

- `"arrive Alice"` → 待機リスト: `[Alice]`
- `"arrive Bob"` → 待機リスト: `[Alice, Bob]`
- `"seat 1"` → `Alice` を席へ案内 → 出力 `["Alice"]`
- `"arrive Charlie"` → 待機リスト: `[Bob, Charlie]`
- `"seat 2"` → `Bob, Charlie` を席へ案内 → 出力 `["Alice", "Bob", "Charlie"]`
- `"arrive Dave"` → 待機リスト: `[Dave]`
- `"arrive Eve"` → 待機リスト: `[Dave, Eve]`
- `"seat 3"` → `Dave, Eve` を席へ案内 → 出力 `["Alice", "Bob", "Charlie", "Dave", "Eve"]`

---

### サンプル2: 席が足りない場合

```python
commands = [
    "arrive Tom",
    "arrive Jerry",
    "arrive Spike",
    "seat 2",
    "arrive Butch",
    "seat 2"
]

assert sushi_seating(commands) == ["Tom", "Jerry", "Spike", "Butch"]
```

#### サンプル2解説

- `"arrive Tom"` → `[Tom]`
- `"arrive Jerry"` → `[Tom, Jerry]`
- `"arrive Spike"` → `[Tom, Jerry, Spike]`
- `"seat 2"` → `Tom, Jerry` を案内 → 出力 `["Tom", "Jerry"]`
- `"arrive Butch"` → `[Spike, Butch]`
- `"seat 2"` → `Spike, Butch` を案内 → 出力 `["Tom", "Jerry", "Spike", "Butch"]`

---

### サンプル3: 席数より待機客が少ない場合

```python
commands = [
    "arrive Anna",
    "arrive Elsa",
    "seat 5"
]

assert sushi_seating(commands) == ["Anna", "Elsa"]
```

#### サンプル3解説

- `"arrive Anna"` → `[Anna]`
- `"arrive Elsa"` → `[Anna, Elsa]`
- `"seat 5"` → `Anna, Elsa` を案内（5 席空いたが 2 人しか待機していない） → 出力 `["Anna", "Elsa"]`
