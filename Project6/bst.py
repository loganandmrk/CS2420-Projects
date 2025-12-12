'''your bst here'''
class BST:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
    
    def __init__(self):
        self.root = None
        self._size = 0
        
    def size(self):
        return self._size
    
    def is_empty(self):
        return self.root is None
    
    def height(self):
        def _height(node):
            if node is None:
                return -1
            else:
                return 1 + max(_height(node.left), _height(node.right))
        
        return _height(self.root)
            
    def add(self, item):
        if self.root is None:
            self.root = self.Node(item)
            self._size += 1
        else:
            current_node = self.root
            while current_node is not None:
                if current_node.data == item:
                    current_node = None
                elif item < current_node.data:
                    if current_node.left is None:
                        current_node.left = self.Node(item)
                        self._size += 1
                        current_node = None
                        
                    else: 
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = self.Node(item)
                        self._size += 1
                        current_node = None
                        
                    else:    
                        current_node = current_node.right
        return self.root

    def remove(self, item):
        parent = None
        current_node = self.root
        while current_node is not None:
            if current_node.data == item:
                # Node with only one child or no child
                if current_node.left is None and current_node.right is None:
                    if parent is None:
                        self.root = None
                    elif parent.left == current_node:
                        parent.left = None
                    else:
                        parent.right = None
                    self._size -= 1
                    return self.root
                elif current_node.right is None:
                    if parent is None:
                        self.root = current_node.left
                    elif parent.left == current_node:
                        parent.left = current_node.left
                    else:
                        parent.right = current_node.left
                    self._size -= 1  
                    return self.root
                elif current_node.left is None:
                    if parent is None:
                        self.root = current_node.right
                    elif parent.left == current_node:
                        parent.left = current_node.right
                    else:
                        parent.right = current_node.right
                    self._size -= 1
                    return self.root
                else:
                    # Node with two children: Get the inorder successor (leftmost in right subtree)
                    successor_parent = current_node
                    successor = current_node.right
                    while successor.left is not None:
                        successor_parent = successor
                        successor = successor.left
                    
                    # Replace current node's data with successor's data
                    current_node.data = successor.data
                    
                    # Remove the successor node (which has at most one right child)
                    if successor_parent == current_node:
                        # successor is the right child of current_node
                        current_node.right = successor.right
                    else:
                        # successor is in the left subtree of current_node's right child
                        successor_parent.left = successor.right
                
                    self._size -= 1
                    return self.root
            elif current_node.data < item:
                parent = current_node
                current_node = current_node.right
            else:
                parent = current_node
                current_node = current_node.left

        return self.root
                    
    def find(self, item):
        current_node = self.root
        while current_node is not None:
            if current_node.data == item:
                return current_node.data
            elif item < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right
        raise ValueError(f'Item {item} not found in the tree.')
    
    def inorder(self):
        if self.root is None:
            return []
        
        def _inorder(node):
            if node is None:
                return []
            return _inorder(node.left) + [node.data] + _inorder(node.right)
        return _inorder(self.root)
 
    def preorder(self):
        if self.root is None:
            return []
        
        def _preorder(node):
            if node is None:
                return []
            return [node.data] + _preorder(node.left) + _preorder(node.right)
        return _preorder(self.root)
    
    def postorder(self):
        if self.root is None:
            return []
        
        def _postorder(node):
            if node is None:
                return []
            return _postorder(node.left) + _postorder(node.right) + [node.data]
        return _postorder(self.root)
    
    def print_tree(self):
        from prettytree import pretty_tree
        print(pretty_tree(self))