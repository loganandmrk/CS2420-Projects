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
    tree = BST()
    with open("C:/Users/ljchr/CS2420-Projects/Project6/around-the-world-in-80-days-3.txt",'r', encoding='utf-8') as file:
        text = file.read()
        for char in text:
            if char not in whitespace and char not in punctuation:
                pair = Pair(char.upper())
                try:
                    if tree.find(pair) is not None:
                        curr_pair = tree.find(pair)
                        curr_pair.count += 1
                except ValueError:
                    tree.add(pair)
    return tree

def main():
    ''' Program kicks off here.

    '''
    tree = make_tree()
    tree.remove(Pair(''))
    print(tree.inorder())

    
if __name__ == "__main__":
    main()
