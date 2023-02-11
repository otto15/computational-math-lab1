class SimpleIterator:
    n: int
    accuracy: float
    matrix: list[list[float]]

    approximation: list[list[float]] = []
    errors: list[list[float]]
    iterations_count: int
    answer: list[float]

    def __init__(self, n: int, accuracy: float, matrix: list[list[float]]):
        self.n = n
        self.accuracy = accuracy
        self.matrix = matrix

    def prepare(self):
        first_entry: list = []
        for i in range(self.n):
            max_in_row: float = max(self.matrix[i][:self.n:], key=abs)
            for j in range(self.n + 1):
                if i == j:
                    self.matrix[i][j] = 0
                    continue
                self.matrix[i][j] /= max_in_row * (-1 + (j == self.n) * 2)
            first_entry.append(self.matrix[i][-1])
        self.approximation.append(first_entry)

    def solve(self):
        i: int = 0
        errors: list[list[float]] = []
        while True:
            self.approximation.append([])
            errors.append([])
            for h in range(self.n):
                new_x: float = 0
                for j in range(self.n):
                    if h != j:
                        new_x += self.matrix[h][j] * self.approximation[i][j]
                new_x += self.matrix[h][self.n]
                errors[i].append(abs(new_x - self.approximation[i][h]))
                self.approximation[-1].append(new_x)
            i += 1
            if max(errors[-1]) <= self.accuracy:
                break
        self.answer = self.approximation[-1]
        self.errors = errors
        self.iterations_count = i
