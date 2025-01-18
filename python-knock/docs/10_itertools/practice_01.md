# 問題(10A): ランレングス符号化

## 問題

ランレングス符号化 (Run-Length Encoding, RLE) は、データ圧縮の一種であり、連続する同じ値をまとめて表現する手法です。

例えば、文字列 `"aaabbcdddd"` をランレングス符号化すると、`[("a", 3), ("b", 2), ("c", 1), ("d", 4)]` のように変換されます。

あなたの課題は、与えられた文字列をランレングス符号化する関数 `run_length_encoding` を実装することです。

---

## 入力

以下の関数を実装してください。

```python
from typing import List, Tuple

def run_length_encoding(s: str) -> List[Tuple[str, int]]:
    """
    文字列をランレングス符号化する関数

    Args:
        s (str): 符号化する文字列（1文字以上）

    Returns:
        List[Tuple[str, int]]: ランレングス符号化されたリスト
    """
    ...
```

### 入力の制約

- `s` は **英小文字 (`a-z`) のみ** からなる文字列。
- `1 ≤ len(s) ≤ 10^5`（最大 100,000 文字）

---

## 出力

- ランレングス符号化後のリストを返します。
  - 各タプル `(c, n)` は、文字 `c` が `n` 回連続していることを表します。
  - タプルは文字列内の出現順に並びます。

---

## サンプル

### サンプル1

#### 入力:
```python
run_length_encoding("aaabbcdddd")
```

#### 出力:
```python
[("a", 3), ("b", 2), ("c", 1), ("d", 4)]
```

#### 説明:
- `"a"` が 3 回連続
- `"b"` が 2 回連続
- `"c"` が 1 回
- `"d"` が 4 回連続

---

### サンプル2

#### 入力:
```python
run_length_encoding("abc")
```

#### 出力:
```python
[("a", 1), ("b", 1), ("c", 1)]
```

#### 説明:
- すべての文字が単独で現れるため、それぞれ 1 回ずつ。

---

### サンプル3

#### 入力:
```python
run_length_encoding("aaaaaaa")
```

#### 出力:
```python
[("a", 7)]
```

#### 説明:
- `"a"` が 7 回連続。

---

### サンプル4

#### 入力:
```python
run_length_encoding("aabbaaaabb")
```

#### 出力:
```python
[("a", 2), ("b", 2), ("a", 4), ("b", 2)]
```

#### 説明:
- `"a"` が 2 回
- `"b"` が 2 回
- `"a"` が 4 回
- `"b"` が 2 回

---

## ヒント

- `itertools.groupby` を使用すると、隣接する同じ文字をグループ化できます。

例えば:
```python
from itertools import groupby

s = "aaabbcdddd"
for key, group in groupby(s):
    print(key, list(group))
```
このコードは以下を出力します:
```
a ['a', 'a', 'a']
b ['b', 'b']
c ['c']
d ['d', 'd', 'd', 'd']
```
これを利用して、各グループの文字とその長さを取得できます。
