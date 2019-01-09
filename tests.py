"""
This file contains unit tests for UPGMA algorithm.
"""

from unittest import TestCase
from upgma_simple import UpgmaTrivial as upgma, AttributeException as exc
from random_table_generator import read_from, test_files_generator
from tree_validator import is_equivalent


class UpgmaTest(TestCase):

    def test_none(self):
        labels = None
        matrix = None

        self.assertIsNone(upgma(labels, matrix).tree)

    def test_empty(self):
        labels = []
        matrix = []

        self.assertIsNone(upgma(labels, matrix).tree)

    def test_not_aligned(self):
        labels = "A B C".split(' ')
        matrix = [
            [0, 1],
            [0, 0]
        ]

        try:
            self.assertRaises(exc, upgma(labels, matrix))
        except exc:
            pass

    def test_not_square_more(self):
        labels = "A B C".split(' ')
        matrix = [
            [0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0]
        ]

        try:
            self.assertRaises(exc, upgma(labels, matrix))
        except exc:
            pass

    def test_not_square_less(self):
            labels = "A B C".split(' ')
            matrix = [
                [0, 0, 0],
                [0, 0],
                [0, 0, 0]
            ]

            try:
                self.assertRaises(exc, upgma(labels, matrix))
            except exc:
                pass

    def test_example_1(self):
        labels = "A B C D".split(' ')
        matrix = [
            [0, 3, 3, 3],  # A
            [0, 0, 2, 2],  # B
            [0, 0, 0, 1],  # C
            [0, 0, 0, 0]   # D
        ]
        tree = "(A,(B,(C,D)))"
        self.assertEqual(tree, upgma(labels, matrix).tree)

    def test_example_2(self):
        labels = "A B C D E".split(' ')
        matrix = [
            [0, 17, 21, 31, 23],  # A
            [0,  0, 30, 34, 21],  # B
            [0,  0,  0, 28, 39],  # C
            [0,  0,  0,  0,  3],  # D
            [0,  0,  0,  0,  0]   # E
        ]
        tree = "(((A,B),C),(D,E))"
        self.assertEqual(tree, upgma(labels, matrix).tree)

    def test_example_3(self):
        labels = "A B C D E F".split(' ')
        matrix = [
            [0, 17, 21,  6,  1,  4],  # A
            [0,  0,  2, 34, 21,  2],  # B
            [0,  0,  0, 28, 39,  8],  # C
            [0,  0,  0,  0,  3, 20],  # D
            [0,  0,  0,  0,  0,  3],  # E
            [0,  0,  0,  0,  0,  0]   # F
        ]
        tree = "(((A,E),D),((B,C),F))"
        self.assertEqual(tree, upgma(labels, matrix).tree)

    def test_example_4(self):
        labels = "A B C D E F".split(' ')
        matrix = [
            [0,  1, 21,  6,  1,  4],  # A
            [0,  0,  2, 34, 21,  2],  # B
            [0,  0,  0,  1,  3,  8],  # C
            [0,  0,  0,  0,  3, 20],  # D
            [0,  0,  0,  0,  0,  3],  # E
            [0,  0,  0,  0,  0,  0]   # F
        ]
        tree = "((((A,B),E),F),(C,D))"
        self.assertEqual(tree, upgma(labels, matrix).tree)

    def test_example_5(self):
        labels = "A B C".split(' ')
        matrix = [
            [0, 1, 1],
            [0, 0, 8],
            [0, 0, 0]
        ]
        tree = "((A,B),C)"
        self.assertEqual(tree, upgma(labels, matrix).tree)

    def test_example_6(self):
        labels = "A B C".split(' ')
        matrix = [
            [0, 2, 2],
            [0, 0, 1],
            [0, 0, 0]
        ]
        tree = "(A,(B,C))"
        self.assertEqual(tree, upgma(labels, matrix).tree)

    def test_random(self):
        for test_file in test_files_generator():
            labels, matrix = read_from(test_file)

            self.assertTrue(is_equivalent(upgma(labels, matrix).tree, test_file))

