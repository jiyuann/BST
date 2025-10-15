class Node:
    """
    """
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
  
class BinarySearchTree:
    """
    """
    def __init__(self):
        self.root = None
  
    def is_empty(self):
        """
        Returns True if BST empty and False otherwise
        """
        return self.root == None
    
    def insert(self, key):
        """
        insert the key in the BST
        """
        if self.is_empty() == True:
            self.root = Node(key)
        else:
            current =  self.root
            prev =  None
            while current:
                if current.key == key:
                    return 'Key already exists'
                elif current.key < key:
                    prev = current
                    current = current.left
                else:
                    prev = current
                    current = current.right
            if prev.key < key:
                prev.left = Node(key)
            else:
                prev.right = Node(key)

    def search(self, key):
        """
        search for the key in the BST
        """
        if self.is_empty():
            return False
        else:
            current = self.root
            while current:
                if current.key == key:
                    return True
                elif current.key < key:
                    current = current.left
                else:
                    current = current.right
            return False

    def remove_leaf_node(self, parent, current, key):
        """
        """
        
    def remove_single_child_node(self, parent, current, key):
        """
        """
        if current.left != None or current.right != None:
            if current.left == None:
                if parent.left == current:
                    parent.left = current.right

    def remove_two_child_node(self, parent, current, key):
        """
        """
    def remove(self, key):
        """
        remove the key in the binary search tree
        """
        if self.is_empty():
            return False
        current = self.root
        parent = None
        while current is not None and current.key != key:
            if current.key < key:
                parent = current
                current = current.left
            else:
                parent = current
                current = current.right
                
        #no matching node found
        if not current:
            return False
        # matching node found
        if current.left and current.right: #if have 2 children
            self.remove_two_child_node(parent, current, key)
        elif not current.left or not current.right: #if only got 1 child
            self.remove_single_child_node(parent, current, key)
        else: #if no children
            self.remove_leaf_node(parent,current, key)
            
        

# BST = BinarySearchTree()
# BST.insert('apple')
# BST.insert('orange')
# test = BST.search('hehe')
# print(test)
