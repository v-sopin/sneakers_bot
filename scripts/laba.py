items = [11, 5, 7, 2, 1, 34, 12, 18]


def func(items):
    count = 0
    for item in items:
        if item % 2 != 0:  # item % 3 == 0 and item % 5 != 0:
            count += 1

    return count


if __name__ == '__main__':
    print('Count: ', func(items))

