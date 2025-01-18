# 問題(08A): 列の幅を揃える

## 問題

テキストデータの各行には `$` (ドル記号) によって区切られたフィールドが含まれています。
このフィールドを各列ごとに整列し、適切な間隔を保ちながら出力してください。

また、各列の単語を **左寄せ (left justified)**、**右寄せ (right justified)**、**中央寄せ (center justified)** のいずれかで整列できるようにしてください。

### 入力フォーマット

以下の `align_columns` 関数を実装してください。

```python
from typing import List, Literal

def align_columns(text: List[str], alignment: Literal["left", "right", "center"]) -> List[str]:
    """
    各行のフィールドを `$` で区切り、列ごとに整列した文字列を返す。

    Args:
        text (List[str]): `$` 区切りの文字列リスト
        alignment (Literal["left", "right", "center"]): 整列方法 ("left", "right", "center")

    Returns:
        List[str]: 整列後の文字列リスト
    """
    ...
```

### 入力の条件

- `text` は `1` 以上 `100` 以下の要素を持つリストで、それぞれの要素は `1` 以上 `200` 以下の長さを持つ文字列。
- 各文字列は `$` をフィールドの区切りとして含む（ただし、末尾に `$` が含まれることもある）。
- `alignment` は `"left"`、`"right"`、または `"center"` のいずれか。

### 出力の仕様

- 各列の単語を `alignment` に従って整列する。
- 列ごとの最小の間隔を 1 スペースとして、適切に整列させる。
- 末尾の不要なスペースは除く。

## サンプル

### サンプル1

```python
text = [
    "Given$a$text$file$of$many$lines,",
    "are$delineated$by$a$single$'dollar'$character,",
    "Further,$allow$for$each$word$in$a$column$to$be$either"
]
alignment = "left"
print("\n".join(align_columns(text, alignment)))
```

#### 出力
```
Given      a        text     file  of      many  lines,
are        delineated by     a     single 'dollar' character,
Further,   allow    for      each  word   in     a       column to be either
```

---

### サンプル2

```python
text = [
    "Given$a$text$file$of$many$lines,",
    "are$delineated$by$a$single$'dollar'$character,",
    "Further,$allow$for$each$word$in$a$column$to$be$either"
]
alignment = "right"
print("\n".join(align_columns(text, alignment)))
```

#### 出力
```
   Given         a  text  file   of  many   lines,
     are delineated    by     a single 'dollar' character,
Further,    allow    for  each  word    in     a column to be either
```

---

### サンプル3

```python
text = [
    "Given$a$text$file$of$many$lines,",
    "are$delineated$by$a$single$'dollar'$character,",
    "Further,$allow$for$each$word$in$a$column$to$be$either"
]
alignment = "center"
print("\n".join(align_columns(text, alignment)))
```

#### 出力
```
  Given      a      text   file   of    many   lines,
   are    delineated   by    a   single 'dollar' character,
Further,    allow    for   each  word    in     a   column to be either
```
