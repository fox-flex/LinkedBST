"""
File: abstractstack.py
Author: Ken Lambert
"""
try:
    from abstractcollection import AbstractCollection
except ModuleNotFoundError:
    from binary_search_tree.abstractcollection import AbstractCollection

class AbstractStack(AbstractCollection):
    """An abstract stack implementation."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        AbstractCollection.__init__(self, sourceCollection)

    # Mutator methods
    def add(self, item):
        """Adds item to self."""
        self.push(item)
