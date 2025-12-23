"""
Назначение: Лабораторная работа №2. Операции с переменными и модуль math.
Автор: Студент
Версия: 1.0
"""
import math


def task_warehouse_correction():
    """
    Задание 1: Исправление категорий и расчет стоимости с НДС.
    """
    category_a = "Vegetables"
    category_b = "Fruits"
    
    price_per_unit_a = 150  # цена за ящик
    quantity_a = 40         # количество ящиков
    vat_rate = 0.2          # НДС 20%

    category_a, category_b = category_b, category_a

    total_value = (price_per_unit_a * quantity_a) + (price_per_unit_a * quantity_a * vat_rate)

    print(f"Текущая категория A: {category_a}")
    print(f"Общая стоимость партии с НДС: {total_value}")

    return category_a, total_value


def task_zone_calculation():
    """
    Задание 2: Расчет стороны квадратной зоны хранения.
    """
    area_total = 225

    zone_id = input("Введите идентификатор зоны: ")

    side_length = math.sqrt(area_total)

    print(f"Расчет для объекта: {zone_id}")
    print(f"Длина стены зоны: {side_length} метров")
    
    return zone_id, side_length


if __name__ == "__main__":
    print("--- Задание 1 ---")
    task_warehouse_correction()
    
    print("\n--- Задание 2 ---")
    task_zone_calculation()
