# Домашка 006 — Lists and Comprehension

## Задание

Реализуй функции в 9 файлах. Всего 44 функции.

### Обязательно (части 1-5):
- `list_basics.py` — first, last, rest, init
- `list_search.py` — find_index, count, contains
- `aggregation.py` — sum_list, product_list, max_list, min_list, average
- `comprehension.py` — squares, evens, positives, lengths, upper_all
- `higher_order_lists.py` — apply_to_all, filter_by, reduce, count_if, all_satisfy, any_satisfy

### Продвинуто (части 6-7):
- `string_lists.py` — chars, join_chars, reverse_string, is_palindrome, remove_vowels, count_words
- `nested_lists.py` — flatten, deep_sum, matrix_row, matrix_col, transpose
- `practical.py` — unique, intersection, difference, zip_lists, unzip, group_by

### Бонус:
- `algorithms.py` — binary_search, merge_sorted, quicksort, is_sorted

## Ограничения

❌ Нельзя использовать:
- `sum()`, `max()`, `min()`, `sorted()`, `reversed()`
- `.sort()`, `.reverse()`, `.index()`, `.count()`
- `set()`, `dict()` (кроме group_by)

✅ Можно использовать:
- `len()`, `range()`, `in`
- Индексы и срезы
- List comprehension
- Циклы for/while

## Как сдать

1. Форкни репозиторий
2. Реализуй функции
3. `pytest tests/ -v`
4. Commit и push
5. Проверь Actions
