# Planted bugs in many-bugs/inventory.py

The fixture is copied into each run, so this key stays outside it.

1. `__init__`: mutable default, shared between instances.
2. `page`: `size - 1` returns one item too few.
3. `total_value`: ignores `qty`.
4. `average_price`: divides by zero on an empty inventory.
5. `remove_empty`: removes from the list while iterating it.
6. `find`: compares strings with `is`.
7. `take`: crashes on an unknown sku, and allows negative stock.
8. `save`: the file is never closed, so data may stay unflushed.
9. `load`: swallows every error and leaks the file handle.
10. `is_expired`: the comparison is reversed.
