from src.scope_manager import ScopeManager


# サンプルテストケース1
def test_sample1():
    sm = ScopeManager()
    sm.set_variable("x", 10)
    assert sm.get_variable("x") == 10  # グローバルスコープで設定された "x" は 10

    sm.enter_scope()
    assert sm.get_variable("x") == 10  # 内側のスコープでも外側の "x" は参照可能

    sm.set_variable("x", 20)
    assert sm.get_variable("x") == 20  # 内側のスコープで上書きされた "x" は 20

    sm.exit_scope()
    assert (
        sm.get_variable("x") == 10
    )  # スコープを抜けると、グローバルスコープの "x" (10) が参照される


# サンプルテストケース2
def test_sample2():
    sm = ScopeManager()
    sm.set_variable("y", 5)

    sm.enter_scope()
    sm.enter_scope()
    sm.set_variable("z", 30)
    assert sm.get_variable("z") == 30
    assert sm.get_variable("y") == 5  # 外側のスコープから "y" を取得

    sm.exit_scope()
    assert (
        sm.get_variable("z") is None
    )  # 内側のスコープが破棄されたため "z" は存在しない


# サンプルテストケース3
def test_sample3():
    sm = ScopeManager()
    assert sm.get_variable("unknown") is None  # 未設定の変数は None

    sm.enter_scope()
    assert (
        sm.get_variable("unknown") is None
    )  # 内側のスコープでも見つからない場合は None


# サンプルテストケース4
def test_sample4():
    sm = ScopeManager()
    sm.set_variable("a", 100)
    sm.set_variable("b", 200)

    sm.enter_scope()
    sm.set_variable("b", 300)  # "b" を内側のスコープで上書き
    assert sm.get_variable("a") == 100  # 外側の "a" はそのまま
    assert sm.get_variable("b") == 300  # 内側の "b" を参照

    sm.exit_scope()
    assert sm.get_variable("b") == 200  # 内側の "b" は破棄され、外側の "b" が参照される


# サンプルテストケース5
def test_sample5():
    sm = ScopeManager()
    sm.exit_scope()  # グローバルスコープでの exit_scope() は無視される
    sm.set_variable("x", 5)
    sm.exit_scope()  # これも無視される
    assert sm.get_variable("x") == 5  # "x" はグローバルスコープに残る
