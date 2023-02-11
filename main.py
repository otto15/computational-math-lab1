import atexit
import sys
from converter_to_diagonal import check_if_diagonal_predominant, ConversionResult, \
    try_to_convert_to_diagonal_predominant
from pathlib import Path

from matrix_reader import read_from_console, read_from_file
from simple_iterator import SimpleIterator


def input_filename() -> str:
    print("Enter filename: ")
    while True:
        filename: str = input()
        if Path(filename).is_file():
            return filename
        print("Such file does not exists")


def input_matrix() -> SimpleIterator:
    if len(sys.argv) > 1 and Path(sys.argv[1]).is_file():
        return read_from_file(sys.argv[1])

    while (choice := input("Read matrix from the file? (y/n)\n").lower()) not in {'n', 'y'}:
        pass
    if choice == 'n':
        return read_from_console()

    return read_from_file(input_filename())


def quit_gracefully():
    print('Bye, bye...')


if __name__ == '__main__':
    atexit.register(quit_gracefully)
    simple_iterator = input_matrix()

    res: ConversionResult = try_to_convert_to_diagonal_predominant(simple_iterator)
    if res.result:
        simple_iterator.matrix = res.matrix
        simple_iterator.prepare()
        simple_iterator.solve()
        print(f"Answer: {simple_iterator.answer}")
        print(f"Number of iterations: {simple_iterator.iterations_count}")
        print(f"Errors: {simple_iterator.errors}")
    else:
        print("Impossible to convert to diagonal predominant form")