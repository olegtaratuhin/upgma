"""
This file contains visualiation example.
"""

from upgma_simple import UpgmaTrivial as upgma


if __name__ == '__main__':
    labels = "A B C D".split(' ')
    matrix = [
        [0, 3, 3, 3],
        [0, 0, 2, 2],
        [0, 0, 0, 1],
        [0, 0, 0, 0]
    ]

    tree = upgma(labels, matrix).tree
    print(tree)
    upgma(labels, matrix).draw_ascii()
