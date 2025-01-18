# 問題(11A): 近似値探索

## 問題文

ソート済みの整数配列 `arr` と探索値 `target` が与えられたとき、 `arr` 内で `target` に最も近い値を返す関数 `find_closest_value` を実装してください。

最も近い値が複数ある場合は、その中で最小の値を返してください。

## 入力

```python
from typing import List

def find_closest_value(arr: List[int], target: int) -> int:
    """
    ソート済みの整数配列から、指定された値に最も近い値を返す。

    Args:
        arr (List[int]): ソートされた整数のリスト (要素数は 1 以上)
        target (int): 探索値

    Returns:
        int: arr 内で target に最も近い値
    """
```

### 入力条件

- `arr` は昇順にソートされた整数のリストで、長さは `1` 以上である。
- `arr` 内の値はすべて異なる。
- `target` は整数である。

### 制約

- `1 ≤ len(arr) ≤ 10^5`
- `-10^9 ≤ arr[i], target ≤ 10^9`
- `arr` の要素は昇順にソートされており、重複はない。

## 出力

- `arr` 内で `target` に最も近い値を返す。
- 近い値が複数ある場合は **小さい方** を返す。

## サンプル1

```python
assert find_closest_value([1, 3, 5, 7, 9], 6) == 5
```

**解説**

- 配列 `[1, 3, 5, 7, 9]`
- 探索値 `6`
- `6` に最も近い値は `5` または `7` だが、より小さい `5` を返す。

## サンプル2

```python
assert find_closest_value([2, 4, 6, 8, 10], 7) == 6
```

**解説**

- `7` に最も近い値は `6` または `8` だが、小さい方の `6` を返す。

## サンプル3

```python
assert find_closest_value([1, 2, 3, 4, 5], 10) == 5
```

**解説**

- `10` に最も近い値は `5` だけなので、`5` を返す。

## サンプル4

```python
assert find_closest_value([-10, -5, 0, 5, 10], -7) == -5
```

**解説**

- `-7` に最も近い値は `-5`。

## サンプル5

```python
assert find_closest_value([10], 7) == 10
```

**解説**

- 配列に `10` しかないので、それを返す。
