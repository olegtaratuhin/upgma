"""
This file contains unit tests for UPGMA algorithm.
"""

from unittest import TestCase
from upgma_simple import UpgmaTrivial as upgma, AttributeException as exc


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
            [0,  0,  0,  0, 43],  # D
            [0,  0,  0,  0,  0]   # E
        ]
        tree = "((C,D),((A,B),E))"
        self.assertEqual(tree, upgma(labels, matrix).tree)
