# 問題(10A): ランレングス符号化

## 問題文

ランレングス符号化 (Run-Length Encoding, RLE) は、データ圧縮の一種であり、連続する同じ値をまとめて表現する手法です。

例えば、文字列 `"aaabbcdddd"` をランレングス符号化すると、`[("a", 3), ("b", 2), ("c", 1), ("d", 4)]` のように変換されます。

与えられた文字列をランレングス符号化する関数 `run_length_encoding` を実装してください。

## 入力

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


## 出力

- ランレングス符号化後のリストを返します。
  - 各タプル `(c, n)` は、文字 `c` が `n` 回連続していることを表します。
  - タプルは文字列内の出現順に並びます。

## サンプル1

```python
assert run_length_encoding("aaabbcdddd") == [("a", 3), ("b", 2), ("c", 1), ("d", 4)]
```

**解説**
- `"a"` が 3 回連続
- `"b"` が 2 回連続
- `"c"` が 1 回
- `"d"` が 4 回連続

## サンプル2

```python
assert run_length_encoding("abc") == [("a", 1), ("b", 1), ("c", 1)]
```

**解説**
- すべての文字が単独で現れるため、それぞれ 1 回ずつ。

## サンプル3

```python
assert run_length_encoding("aaaaaaa") == [("a", 7)]
```

**解説**
- `"a"` が 7 回連続。
