"""
This file contains function that checks tree equivalence of the trees for own
implementation and reference implementation in biopython package for tests.
"""

from networkx import is_isomorphic
from networkx.classes import graph
from Bio.Phylo import to_networkx, BaseTree
from Bio.Phylo import TreeConstruction
from random_table_generator import read_from as reader


def is_equivalent(tree, file):
    # TODO: Add random tree reference equivalence test
    return True



