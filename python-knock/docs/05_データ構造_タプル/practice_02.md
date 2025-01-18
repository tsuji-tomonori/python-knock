# 問題(05B): サーバーログの解析

### 問題

サーバーのアクセスログが、以下のような形式のタプルのリストで記録されています。

```python
logs = [
    ("192.168.0.1", "GET /index.html", 200),
    ("192.168.0.2", "POST /login", 401),
    ("192.168.0.1", "GET /about.html", 200),
    ("192.168.0.3", "GET /contact.html", 404),
    ("192.168.0.1", "POST /submit", 500),
    ("192.168.0.2", "GET /dashboard", 200),
]
```

各ログの要素は以下の情報を持っています。

- **IPアドレス (str)**: リクエストを送信したクライアントのIPアドレス
- **リクエスト内容 (str)**: HTTPメソッド（GET/POST など）とリクエストしたリソースのパス
- **ステータスコード (int)**: HTTPレスポンスのステータスコード（例: 200 は成功, 404 は Not Found）

以下のタスクを実装してください。

1. **ステータスコードが 200 のリクエストをすべて抽出** し、それらのログをリストとして返す関数 `filter_successful_requests(logs: list[tuple[str, str, int]]) -> list[tuple[str, str, int]]` を実装してください。

2. **各 IP アドレスのリクエスト回数を集計** し、`{IPアドレス: リクエスト回数}` の辞書を返す関数 `count_requests_by_ip(logs: list[tuple[str, str, int]]) -> dict[str, int]` を実装してください。

---

### 関数の仕様

#### `filter_successful_requests`

**入力**
- `logs`: タプルのリスト `(str, str, int)`

**出力**
- ステータスコードが `200` のリクエストのみを含むリスト

**例**
```python
logs = [
    ("192.168.0.1", "GET /index.html", 200),
    ("192.168.0.2", "POST /login", 401),
    ("192.168.0.1", "GET /about.html", 200),
    ("192.168.0.3", "GET /contact.html", 404),
]

assert filter_successful_requests(logs) == [
    ("192.168.0.1", "GET /index.html", 200),
    ("192.168.0.1", "GET /about.html", 200),
]
```

---

#### `count_requests_by_ip`

**入力**
- `logs`: タプルのリスト `(str, str, int)`

**出力**
- 各 IP アドレスごとのリクエスト回数を集計した辞書 `{str: int}`

**例**
```python
logs = [
    ("192.168.0.1", "GET /index.html", 200),
    ("192.168.0.2", "POST /login", 401),
    ("192.168.0.1", "GET /about.html", 200),
    ("192.168.0.3", "GET /contact.html", 404),
    ("192.168.0.1", "POST /submit", 500),
    ("192.168.0.2", "GET /dashboard", 200),
]

assert count_requests_by_ip(logs) == {
    "192.168.0.1": 3,
    "192.168.0.2": 2,
    "192.168.0.3": 1
}
```
