import pytest
import math
from main import task_warehouse_correction, task_zone_calculation


def test_warehouse_swap_logic():
    """Проверяем, что категории поменялись местами, а Vegetable исчез."""
    category, _ = task_warehouse_correction()
    assert category == "Fruits", "Ошибка: В category_a должны оказаться Фрукты"


def test_warehouse_total_value():
    """Проверяем математику: (150*40) + 20% = 6000 + 1200 = 7200."""
    _, total = task_warehouse_correction()
    assert total == 7200.0, f"Ошибка: Ожидалось 7200.0, получено {total}"


def test_warehouse_output(capsys):
    """Проверяем, что программа выводит правильный текст в консоль."""
    task_warehouse_correction()
    captured = capsys.readouterr()
    assert "Текущая категория A: Fruits" in captured.out
    assert "7200.0" in captured.out


def test_zone_calculation_math():
    with pytest.MonkeyPatch.context() as m:
        m.setattr('builtins.input', lambda _: "Test-Zone")
        _, side = task_zone_calculation()
        assert side == 15.0
        assert isinstance(side, float)


def test_zone_user_input(monkeypatch, capsys):
    fake_input = "Cold-Storage-01"
    monkeypatch.setattr('builtins.input', lambda prompt: fake_input)

    zone_id, side = task_zone_calculation()

    captured = capsys.readouterr()

    # 4. Проверки
    assert zone_id == "Cold-Storage-01", "Функция должна вернуть введенный ID"
    assert "Расчет для объекта: Cold-Storage-01" in captured.out
    assert "Длина стены зоны: 15.0 метров" in captured.out
