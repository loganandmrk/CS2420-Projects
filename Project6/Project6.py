from pathlib import Path
from string import whitespace, punctuation
from bst import BST


class Pair:
    ''' Encapsulate letter,count pair as a single entity.
    
    Realtional methods make this object comparable
    using built-in operators. 
    '''
    def __init__(self, letter, count = 1):
        self.letter = letter
        self.count = count
    
    def __eq__(self, other):
        return self.letter == other.letter
    
    def __hash__(self):
        return hash(self.letter)

    def __ne__(self, other):
        return self.letter != other.letter

    def __lt__(self, other):
        return self.letter < other.letter

    def __le__(self, other):
        return self.letter <= other.letter

    def __gt__(self, other):
        return self.letter > other.letter

    def __ge__(self, other):
        return self.letter >= other.letter

    def __repr__(self):
        return f'({self.letter}, {self.count})'
    
    def __str__(self):
        return f'({self.letter}, {self.count})'

def make_tree():
    ''' A helper function to build the tree.
    
    The test code depends on this function being available from main.
    :param: None
    :returns: A binary search tree
    '''
    pass

def main():
    ''' Program kicks off here.

    '''
    tree = BST()
    tree.add(3)
    tree.add(2)
    tree.add(5)
    tree.add(4)
    tree.add(6)
    print(tree.inorder())
    print(tree.preorder())
    print(tree.postorder())
    tree.print_tree()
    tree.remove(5)
    tree.print_tree()
    tree.add(7)
    tree.add(1)
    tree.print_tree()
    tree.remove(2)
    tree.print_tree()
    tree.remove(3)
    tree.print_tree()
    print(tree.height())
    print(tree.find(4))
    print(tree.size())
    tree.remove(4)
    tree.remove(6)
    tree.remove(1)
    print(tree.is_empty())
    tree.remove(7)
    print(tree.is_empty())
    print(tree.size())
    print(tree.height())
    tree.remove(34)
    print(tree.add(10))
    print(tree.inorder())

    
if __name__ == "__main__":
    main()
