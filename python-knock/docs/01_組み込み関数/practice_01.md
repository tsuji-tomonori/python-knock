# 問題(01A): 工程能力指数の計算

> 深謀遠慮: 深く考えを巡らし、のちのちの遠い先のことまで見通した周到綿密な計画を立てること。

## 問題文
工程能力指数 (Process Capability Index, **Cpk**) は製造工程の能力を評価するために使用される指標の一つです。Cpk は工程が規格範囲にどの程度適合しているかを示し、工程の品質を判断するのに役立ちます。
Cpk の値が大きいほど、工程は規格範囲内に収まりやすく、品質が高いことを示します。一般的に、Cpk が 1.33 以上であれば工程が安定しているとみなされます。

【$Cpk$ の計算方法】

$Cp$（工程能力指数）は次のように計算されます。

$$Cp = \frac{{USL - LSL}}{{6\sigma}}$$

ここで、

- $USL$ は上側規格限界（Upper Specification Limit）
- $LSL$ は下側規格限界（Lower Specification Limit）
- $σ$ はデータの標準偏差

 $Cpk$（工程能力指数）は次のように計算されます。

$$Cpk = (1-k)Cp$$

kは非対称度を表す指標で、次のように定義されます。

$$k = \frac{{|X - M|}}{{R/2}}$$

ここで、

- $X$ はプロセスの平均値
- $M$ は規格の中心値 $(USL+LSL)/2$
- $R$ は規格幅 $USL-LSL$ です

> 参考
> https://seihin-sekkei.com/words/process-capability/

$Cpk$ を計算する関数を作成してください。

## 入力

```python
from typing import NamedTuple


class Param(NamedTuple):
    usl: float # 規格上限値
    lsl: float # 規格下限値
    data: list[float] # 工程から得られたサンプルデータのリスト データは1件以上


def calc_cpk(param: Param) -> float:
    """
    工程能力指数を計算する関数.

    Args:
        param (Param): 計算に必要な値

    Returns:
        list[int]: 工程能力指数(cpk) 小数点第4位で四捨五入
    """
    ...
```

## 出力
`calc_cpk` 関数は、工程能力指数 (**Cpk**) を **小数点第4位で四捨五入した浮動小数点数値**として返してください。

## サンプル 1
```python
def test_basic_1():
    param = Param(
        usl=10.0,
        lsl=2.0,
        data=[4.5, 5.0, 4.8, 5.2, 5.5]
    )
    assert calc_cpk(param) == 2.626
```

**解説**:
- $USL = 10.0$
- $LSL = 2.0$
- 平均値  $X = \frac{4.5 + 5.0 + 4.8 + 5.2 + 5.5}{5} = 5.0$
- 標準偏差  $\sigma = \sqrt{\frac{(4.5-5.0)^2 + (5.0-5.0)^2 + (4.8-5.0)^2 + (5.2-5.0)^2 + (5.5-5.0)^2}{5 - 1}} =  \sqrt{0.145} = 0.3807886552931$
- 中心値 $M = \frac{USL+LSL}{2} = \frac{10.0 + 2.0}{2} = 6.0$
- 規格幅 $R = USL-LSL = 10.0 - 2.0 = 8.0$
- $k = \frac{{|X - M|}}{{R/2}} =\frac{{|5.0 - 6.0|}}{{8.0/2}} = \frac{1}{4} = 0.25 $
- $Cp = \frac{{USL - LSL}}{{6\sigma}} = \frac{10.0 - 2.0}{6 \times 0.3807886552931} = \frac{8}{2.28473193175917} = 3.501504876259271$
- $Cpk = (1-k)Cp = (1 - 0.25) \cdot 3.501504876259271 = 2.62612865719445325 \fallingdotseq 2.626$
