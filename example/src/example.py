def add_even_numbers(n):
    _sum = 0
    for item in range(1, n):
        if item % 2 == 0:
            _sum = _sum + item
    return _sum