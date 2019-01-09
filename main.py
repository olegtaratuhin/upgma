"""
This file contains visualiation example.
"""

from upgma_simple import UpgmaTrivial as upgma


if __name__ == '__main__':
    labels = "A B C D".split(' ')
    matrix = [
        [0, 3, 3, 3],  # A
        [0, 0, 2, 2],  # B
        [0, 0, 0, 1],  # C
        [0, 0, 0, 0]   # D
    ]

    tree = upgma(labels, matrix).tree
    print(tree)
    upgma(labels, matrix).draw_ascii()
