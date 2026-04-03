# Домашка 006 — Lists, Comprehension & Tuples

## Задание

Реализуй функции в 4 файлах. Всего 33 функции.

### Обязательно:
- `list_ops.py` — 10 функций: count_item, reverse_list, flatten_once, chunk, interleave, run_length_encode, rotate, deduplicate, zip_lists, unzip
- `comprehension.py` — 9 функций (каждая одной строкой): evens_only, long_words, pairs, unique_chars, word_lengths, transpose, group_by, all_triples, matrix_from_flat

### Продвинуто:
- `interval.py` — 7 функций: interval, lower, upper, width, contains, overlaps, intersection
- `rational.py` — 7 функций: rational, numer, denom, add_rational, mul_rational, equal_rational, print_rational

## Ограничения

❌ Нельзя использовать:
- `sum()`, `max()`, `min()`, `sorted()`, `reversed()`
- `.sort()`, `.reverse()`, `zip()`

✅ Можно использовать:
- `len()`, `range()`, `in`
- Индексы и срезы
- List / set / dict comprehension
- Циклы for/while
- `from math import gcd` (для rational.py)

## Как сдать

1. Форкни репозиторий
2. Реализуй функции
3. `pytest tests/ -v`
4. Commit и push
5. Проверь Actions
