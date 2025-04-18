---
sidebar_label: はじめに
sidebar_position: 100
---
# Python Knock

## 概要
本リポジトリは、Python の基本構文を学んだ方向けに、より高度な問題を提供するためのものです。各問題は **pytest** によるテストをすべて通過することで正解と判定されます。
また、実務を意識し、コードの品質を向上させるために **ruff** や **mypy** によるチェックも行います。

さらに、環境構築をスムーズにするために、ローカル環境のほか **Amazon CodeCatalyst** や **GitHub Codespaces** への対応も進めています。

## 環境構築
### ローカル環境
1. Python のセットアップ（推奨バージョン: 3.10 以上）
2. 仮想環境の作成
   ```sh
   python -m venv venv
   source venv/bin/activate  # Windows の場合: venv\Scripts\activate
   ```
3. 必要なパッケージのインストール
   ```sh
   pip install -r requirements.txt
   ```

### Amazon CodeCatalyst / GitHub Codespaces
これらの環境では、リポジトリをクローンするだけで設定が自動的に適用されます。

## 問題カテゴリ
各問題は以下のカテゴリに分類されます。

| カテゴリ番号 | カテゴリ名 | 説明 | 問題1 | 問題2 |
|-------------|-------------|---------------------------------------------------|----------------|----------------|
| 1 | 組み込み関数 | Python の標準ライブラリに含まれる組み込み関数の使い方を学ぶ | 工程能力算出 | 年齢分布の集計 |
| 2 | リストの操作 | リストの作成、操作、並べ替え、要素の削除、検索などを学ぶ | ラングトンのアリ | ライフゲーム |
| 3 | データ構造 リスト | リストの特性を理解し、柔軟なデータ管理を学ぶ | 接続数算出 | クラスタリング |
| 4 | データ構造 タプル | タプルの特性を理解し、活用方法を学ぶ | カウント1 | サーバーログの解析 |
| 5 | データ構造 辞書 | 辞書の特性を理解し、データ検索手法を学ぶ | カウント2 | lru キャッシュ |
| 6 | データ構造 集合 | 集合の特性を理解し、データ管理や集合演算を学ぶ | 重複排除1 | 重複排除2 |
| 7 | データ構造 スタック/キュー | スタックやキューの特性を理解し、実装方法を学ぶ | スタック | キュー |
| 8 | 文字列 | 文字列の特性を理解し、部分文字列の抽出や検索を学ぶ | 列の幅(Align columns) | 略称チェック |
| 9 | 日付 | 日付の特性を理解し、datetime モジュールを活用する | 曜日 | 会議室予約 |
| 10 | itertools | コレクションモジュールを理解し、データ構造を効率的に活用する | ランレングス符号化 | Hit&Blow |
| 11 | 探索 | itertools モジュールを理解し、反復処理を効率化する方法を学ぶ | 近似値チェック | 特定の範囲の個数 |
| 12 | 再帰 | 再帰の特性を理解し、効率的な解法を学ぶ | レーベンシュタイン距離 | ハノイの塔 |

## 問題の解答方法
1. 各問題フォルダ内の `main.py` に解答コードを記述する。
2. `tests/` フォルダ内の `test_*.py` にあるテストがすべて成功することを確認する。
   ```sh
   pytest
   ```
3. `ruff` や `mypy` のチェックを通過する。
   ```sh
   ruff check .
   mypy .
   ```

## コントリビューション
このプロジェクトへの貢献を歓迎します！
1. Issue や Pull Request を作成してください。
2. コーディング規約を守るために `ruff` と `mypy` を活用してください。
3. pytest のテストを必ず追加し、すべて通過することを確認してください。

## ライセンス
このプロジェクトは MIT ライセンスのもとで公開されています。
