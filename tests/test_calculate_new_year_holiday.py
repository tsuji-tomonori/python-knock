from src.calculate_new_year_holiday import calculate_new_year_holiday


def test_sample1():
    """
    サンプルテストケース1 (year=2025):
    基本期間 12/29～1/3 に加え、前日 2024-12-28（土）と翌日 2025-01-04,05（土・日）が追加される
    → 休暇期間: 2024-12-28 ～ 2025-01-05, 休暇日数: 9日
    """
    result = calculate_new_year_holiday(2025)
    expected = ("2024-12-28", "2025-01-05", 9)
    assert result == expected


def test_sample2():
    """
    サンプルテストケース2 (year=2026):
    基本期間 12/29～1/3 に加え、前日 2024-12-27,28（土・日）と翌日 2025-01-04（日）が追加される
    → 休暇期間: 2025-12-27 ～ 2026-01-04, 休暇日数: 9日
    """
    result = calculate_new_year_holiday(2026)
    expected = ("2025-12-27", "2026-01-04", 9)
    assert result == expected
