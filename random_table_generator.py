"""
This file contains random generator for tables.
"""

import random


class RandomGenerator(object):
    """
    Class for generating random tables (properly formatted) and saving them
    for testing purposes.
    """

    def __init__(self, seed=None):
        if seed is not None:
            random.seed(seed)

    def generate(self, number_of_tests, min_test_size=5, max_test_size=1000):
        for i in range(number_of_tests):
            test_size = random.randint(min_test_size, max_test_size)

            labels = ['L' + str(i) for i in range(test_size)]
            matrix = [['0' for _ in range(test_size)] for _ in range(test_size)]
            for j in range(test_size):
                for k in range(j + 1, test_size):
                    matrix[j][k] = str(random.random())

            with open("random_tests/test_" + str(i) + ".txt", "w") as f:
                f.write(' '.join(labels))
                f.write('\n')
                for l in range(test_size):
                    f.write(labels[l])
                    f.write(' ')
                    f.write(' '.join(matrix[l]))
                    f.write('\n')


def read_from(file, sep=' '):
    with open(file, "r") as f:
        labels = None
        matrix = []
        for line in f.readlines():
            if labels is None:
                labels = line.split(sep)
                labels[-1] = labels[-1].strip()  # hack for annoying '\n'
                continue
            _, *args = line.split(' ')
            matrix.append([float(x) for x in args])

    return labels, matrix


def test_files_generator():
    for i in range(10):
        yield "random_tests/test_{0}.txt".format(i)


if __name__ == "__main__":
    g = RandomGenerator()
    g.generate(1)
    # labels, matrix = read_from("random_tests/test_0.txt")
    # print(labels)
    # print(matrix)
    # print([filename for filename in test_files_generator()])
