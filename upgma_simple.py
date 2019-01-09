"""
This file contains trivial implementation of UPGMA.
"""

from Bio.Phylo import draw_ascii, read, draw
import io


class AttributeException(Exception):
    def __init__(self, *args):
        super().__init__(args)


class UpgmaTrivial(object):
    """
    A trivial implementation of UPGMA.
    """

    __slots__ = "labels", "matrix", "tree", \
                "_matrix_org", "_labels_org", \
                "_cluster_weight"

    def __init__(self, labels, matrix):
        if matrix is None and labels is None:
            self.tree = None
            return

        if labels is None or matrix is None or len(labels) != len(matrix):
            raise AttributeException("Labels and matrix are not aligned")

        if len(matrix) == 0:
            self.tree = None
            return

        min_dim = min([len(matrix[i]) for i in range(len(matrix))])
        max_dim = max([len(matrix[i]) for i in range(len(matrix))])
        if min_dim != max_dim or min_dim != len(matrix):
            raise AttributeException("Matrix is not square")

        self.labels = labels
        self._labels_org = labels.copy()
        self._cluster_weight = [1 for _ in range(len(labels))]
        self.matrix = matrix
        self._matrix_org = matrix.copy()
        self.tree = None

        for _ in range(len(self.matrix) - 1):
            c1, c2 = self.select()
            self.join_table(c1, c2)
            self.join_labels(c1, c2)

        self.tree = self.labels[0]

    def select(self) -> tuple:
        """
        Select minimal value in matrix to merge.
        Optimizes for upper triangular matrices.
        :return: tuple of row and column corresponding to position of global
                 minimum
        """
        min_val, min_row, min_col = float("inf"), -1, -1
        for i in range(len(self.matrix)):
            for j in range(i + 1, len(self.matrix[i])):  # upper triangular opt
                if self.matrix[i][j] < min_val:
                    min_val, min_row, min_col = self.matrix[i][j], i, j
        return min_row, min_col

    def join_labels(self, c1, c2):
        """
        Join labels for specified items and puts them in c1, c2 is deleted.
        :param c1: first label to merge
        :param c2: second label to merge
        :return: merged label
        """
        self.labels[c1] = "({0},{1})".format(self.labels[c1], self.labels[c2])
        self._cluster_weight[c1] += self._cluster_weight[c2]
        del self.labels[c2]
        del self._cluster_weight[c2]

    def cluster_size(self, c):
        """
        Determine cluster size by index.

        :param c: index of cluster
        :return:
        """
        return self._cluster_weight[c]

    def join_table(self, c1, c2):
        """
        Join table cells and recompute distances to new clusters.
        :param c1: first row (column) to merge
        :param c2: second row (column) to merge
        :return: modified table reference
        """

        for i in range(len(self.matrix)):
            self.matrix[c1][i] = (self.matrix[c1][i] * self.cluster_size(c1) +
                                  self.matrix[c2][i] * self.cluster_size(c2)) / \
                                 (self._cluster_weight[c1] + self._cluster_weight[c2])

        for i in range(len(self.matrix)):
            del self.matrix[i][c2]

        del self.matrix[c2]

    def draw_ascii(self):
        """
        Visualization using standard biopython package.
        :return: None
        """
        newick_tree = read(io.StringIO(self.tree), "newick")
        draw_ascii(newick_tree)

    def draw(self):
        """
        Visualization using standard biopython package.
        :return: None
        """
        newick_tree = read(io.StringIO(self.tree), "newick")
        draw(newick_tree)
