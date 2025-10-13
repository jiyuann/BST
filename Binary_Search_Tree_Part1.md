## Data Structures - Binary Search Tree (Part 1)

## Tree

For simple collections of elements, an array or linked list might suffice. But for collections of hierarchical elements, where each element might refer to more than one other element, a different kind of abstract data structure is needed.

One such data structure is the **tree**. A tree consists of multiple nodes linked in a specific manner, with one node designated as the root.

Each node has:

- only one parent node (with the exception of the root node which has no parent),
- a **key**,
- zero or more child nodes

## Binary Search Tree
A binary search tree (BST) is a specific kind of tree: each node in a BST cannot have more than 2 child nodes. This mimics the hierarchical structure required by the binary search algorithm.

The node keeps track of its children via two attributes: left and right.

The nodes of a BST must be linked using the following specific rules:
1. The **left child** must have a key less than the node’s key,
2. The **right child** must have a key greater than the node’s key.

These rules enable the **BST** to **maintain** its **nodes** in a **sorted order**, **provided** there are no **duplicate keys** in the BST. **BST algorithms** that **allow duplicate values** are **not discussed here**.

## Basic Operations:

## Searching
Searching for a target key in the BST involves traversing the tree.

The general algorithm for searching for a key in a BST is given below:

1. Start at the root of the tree.
2. Compare the key you're searching for with the value of the current node:
3. If the key matches the current node’s value, you’ve found the key! Stop.
4. If the key is smaller than the current node’s value, move to the left child.
5. If the key is larger, move to the right child.
6. Repeat the comparison at each child node as you move:
7. Continue moving left or right depending on whether the key is smaller or larger.
8. If you reach a point where there is no child to move to (i.e., a None or null value), the key is not in the tree. Stop.
9. If you find the key, return True. If not, return False.

* <i>Do also remember to check if the tree is empty...</i>

## Inserting/ Editing
The process for inserting a key into the BST is **very similar to key search in the BST**.

The general algorithm for inserting a node into a BST is given below:

1. Create a new node with the value you want to insert.
2. Check if the tree is empty:
3. If it is, set the new node as the root of the tree and stop.
4. If the tree is not empty, start at the root of the tree.
5. Compare the value of the new node with the current node’s value:
6. If the new value is smaller, move to the left child.
7. If the new value is larger or equal, move to the right child.
8. Repeat the comparison at each child node:
9. Keep moving left or right until you find an empty spot (i.e., a None or null value).
10. When you find an empty spot, insert the new node there:
11. If it's smaller than the last node you visited, place it as the left child.
12. If it's larger or equal, place it as the right child.
13. The node is now inserted in its correct position, keeping the binary search tree structure intact.

## Visual Example (Inserting 15 into the BST)
`      20`<br>
`     /  \`<br>
`   10    30`<br>
`   /`<br>
`  5`

To insert 15:
- Start at the root (20), move left because 15 < 20.  
- At node 10, move right because 15 > 10.  
- Insert 15 as the right child of node 10.

The resulting tree:

`      20`<br>
`     /  \`<br>
`   10    30`<br>
`   / \`<br>
`  5   15`

## BST Implementation

Reference:
[Tree Notes](https://docs.google.com/document/d/1vmMKC6qzvKVJg3-SRSzbivBvTvgjXi1BhjuMVsjlHKI/edit#heading=h.lk2evne25w9)
[Linked List Notes](https://docs.google.com/document/d/1d5DVPfbw_o475AmZ9n13ORy9fd8dBynkVbkVRthhms8/edit#heading=h.mejovh4ux3)

In your pairs, your task is to create an iterative BST implementation with the following requirements:

A `Node` class with the following **attributes**:
- `left` initialised to `None`
- `right` intialised to `None`
- `key`

A `BSTree` class with the following **attribute**:
- `root` initialised to `None`

and the following **methods**:
- `is_empty()` returns True if the Tree is empty or False otherwise 
- `insert(key)` inserts a `Node` instance with the associated key into the BST
- `search(key)` returns `True` if key if found, `False` otherwise

<i>**Remember to add your docstrings**</i>

## Conclusion
Binary Search Trees may appear a little confusing at first but the only way to get the hang of it is to keep practicing. That’s it for this tutorial. In the next tutorial, we'll look at some different ways to traverse a Binary Search Tree. Happy Pythoning!