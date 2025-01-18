# 問題(11B): 特定の範囲の個数

## 問題文

ソート済みの整数配列 `arr` が与えられたとき、指定された範囲 `[l, r]` に含まれる要素の個数を求める関数 `count_in_range` を実装してください。

この問題では、**探索アルゴリズム** を用いて効率的に要素の個数を求めることが求められます。

## 入力

以下の `count_in_range` 関数を実装してください。

```python
from typing import List

def count_in_range(arr: List[int], l: int, r: int) -> int:
    """
    ソート済みの配列から指定範囲 [l, r] に含まれる要素の個数を求める関数。

    Args:
        arr (List[int]): ソート済みの整数配列（昇順）。
        l (int): 範囲の下限。
        r (int): 範囲の上限。

    Returns:
        int: 範囲 [l, r] に含まれる要素の個数。
    """
    ...
```

### 入力の制約

- `arr` は **昇順** にソートされた整数のリストである。
- `1 ≤ len(arr) ≤ 10^5`
- `-10^9 ≤ arr[i] ≤ 10^9`
- `-10^9 ≤ l ≤ r ≤ 10^9`

## 出力

- `int` 型で、`arr` 内の要素のうち `[l, r]` の範囲に含まれる個数を返してください。

---

## サンプル

### サンプル1: 基本ケース

```python
import pytest
from your_module import count_in_range  # your_module を適切なモジュール名に変更してください

def test_basic_case():
    arr = [1, 3, 5, 7, 9, 11]
    l, r = 4, 8
    assert count_in_range(arr, l, r) == 2  # 5, 7 の2つ
```

---

### サンプル2: 負の値を含むケース

```python
def test_negative_numbers():
    arr = [-5, -3, -1, 2, 4, 6, 8, 10]
    l, r = -2, 5
    assert count_in_range(arr, l, r) == 3  # -1, 2, 4 の3つ
```

---

### サンプル3: 範囲外のケース

```python
def test_out_of_range():
    arr = [1, 2, 3, 4, 5]
    l, r = 6, 10
    assert count_in_range(arr, l, r) == 0  # 範囲に該当なし
```

---

### サンプル4: 部分範囲のケース

```python
def test_partial_range():
    arr = [10, 20, 30, 40, 50]
    l, r = 15, 45
    assert count_in_range(arr, l, r) == 3  # 20, 30, 40 の3つ
```

---

### サンプル5: すべての要素が範囲内のケース

```python
def test_all_elements_in_range():
    arr = [1, 2, 3, 4, 5]
    l, r = -10, 10
    assert count_in_range(arr, l, r) == 5  # 全範囲を含む
```

---

### サンプル6: 1つの要素のみのケース

```python
def test_single_element():
    arr = [1]
    l, r = 1, 1
    assert count_in_range(arr, l, r) == 1  # 1つの要素のみ
```

---

### サンプル7: 範囲に含まれない1要素のケース

```python
def test_single_element_outside_range():
    arr = [1]
    l, r = 0, 0
    assert count_in_range(arr, l, r) == 0  # 範囲外
```
