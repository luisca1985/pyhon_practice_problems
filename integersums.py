def add_it_up(value: int = 0) -> int:
    iterator = range(value + 1)
    return sum(iterator)

if __name__ == '__main__':
    result_sum = add_it_up(10)
