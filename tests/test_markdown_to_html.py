from src.markdown_to_html import markdown_to_html


def test_sample():
    md = """# 見出し1

これは *イタリック* と **強調** を含む段落です。

## 見出し2

`コード` を含む別の段落。"""
    expected = (
        "<h1>見出し1</h1>\n"
        "<p>これは <em>イタリック</em> と <strong>強調</strong> を含む段落です。</p>\n"
        "<h2>見出し2</h2>\n"
        "<p><code>コード</code> を含む別の段落。</p>"
    )
    assert markdown_to_html(md) == expected
