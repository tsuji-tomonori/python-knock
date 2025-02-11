class ScopeManager:
    def __init__(self): ...

    def enter_scope(self) -> None:
        """
        新しいスコープを作成し、現在のスコープを一段深くする。
        """
        ...

    def exit_scope(self) -> None:
        """
        現在のスコープを破棄し、1 つ上のスコープに戻る。
        最上位のグローバルスコープを削除しようとした場合は何もしない。
        """
        ...

    def set_variable(self, name: str, value: int) -> None:
        """
        現在のスコープに、変数名 name をキーとして value を保存する。
        """
        ...

    def get_variable(self, name: str) -> int | None:
        """
        現在のスコープから順に変数 name を探し、見つかった場合はその値を返す。
        どのスコープにも存在しない場合は None を返す。
        """
        ...
