from simple_iterator import SimpleIterator


def read_from_console() -> SimpleIterator:
    print("Enter matrix dimension:")
    while True:
        try:
            x: int = int(input())
            if x > 20 or x < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid dimension, try again")

    print("Enter accuracy:")
    while True:
        try:
            accuracy: float = float(input())
            if accuracy <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid accuracy, try again")

    print("Type coefficient matrix and free variable with columns divided by whitespace and rows by line break")
    matrix = []
    for line in range(x):
        while True:
            data = input().strip().split(" ")
            if len(data) != x + 1:
                print("Invalid line, try again")
                continue
            break
        data = [float(i) for i in data]
        matrix.append(data)

    return SimpleIterator(x, accuracy, matrix)


def read_from_file(filename: str) -> SimpleIterator:
    f = open(filename, "r")
    matrix = []

    try:
        n, accuracy = list(map(float, f.readline().strip().split(' ')))
        n = int(n)
        if n > 20 or n < 0 or accuracy <= 0:
            raise ValueError

        for line in range(n):
            data = f.readline().strip().split(" ")
            if len(data) != n + 1:
                raise ValueError
            data = [float(i) for i in data]
            matrix.append(data)

        return SimpleIterator(n, accuracy, matrix)

    except ValueError:
        raise ValueError('Invalid file content')
