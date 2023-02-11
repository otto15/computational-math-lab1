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
            break
        except ValueError:
            print("Invalid accuracy, try again")

    print("Type coefficient matrix with columns divided by whitespace and rows by line break")
    matrix = []
    for line in range(x):
        data = input().strip().split(" ")
        data = [float(i) for i in data]
        matrix.append(data)

    return SimpleIterator(x, accuracy, matrix)


def read_from_file(filename: str) -> SimpleIterator:
    f = open(filename, "r")
    matrix = []

    n, accuracy = list(map(float, f.readline().strip().split(' ')))
    n = int(n)
    if n > 20 or n < 0:
        print("Invalid file content")
        exit()

    for line in range(n):
        data = f.readline().strip().split(" ")
        data = [float(i) for i in data]
        matrix.append(data)

    return SimpleIterator(n, accuracy, matrix)
