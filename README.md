# Домашка 006 — Lists, Comprehension & Tuples

## Задание

Реализуй функции в 4 файлах. Всего 24 функции.

### Обязательно:
- `list_ops.py` — 5 функций: sum_list, max_list, count_item, reverse_list, flatten_once
- `comprehension.py` — 6 функций (каждая одной строкой): squares, evens_only, long_words, pairs, unique_chars, word_lengths
- `tuples.py` — 6 функций: point, x_coord, y_coord, distance, midpoint, swap

### Продвинуто:
- `rational.py` — 7 функций: rational, numer, denom, add_rational, mul_rational, equal_rational, print_rational

## Ограничения

❌ Нельзя использовать:
- `sum()`, `max()`, `min()`, `sorted()`, `reversed()`
- `.sort()`, `.reverse()`, `.index()`, `.count()`

✅ Можно использовать:
- `len()`, `range()`, `in`
- Индексы и срезы
- List / set / dict comprehension
- Циклы for/while
- `from math import gcd, sqrt` (для rational.py и tuples.py)

## Как сдать

1. Форкни репозиторий
2. Реализуй функции
3. `pytest tests/ -v`
4. Commit и push
5. Проверь Actions
