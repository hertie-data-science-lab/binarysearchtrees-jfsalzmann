# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 15:18:23 2023

@author: Johann-Friedrich Salzmann, Finn Krueger
"""

from mlbt import MutableLinkedBinaryTree

lbt = MutableLinkedBinaryTree()

print(len(lbt))
print(lbt.root())

lbt.add_root(1)
lbt.add_left(lbt.root(), 2)
lbt.add_right(lbt.root(), 3)

l = lbt.left(lbt.root())
r = lbt.right(lbt.root())

lbt.add_left(l, 4)
lbt.add_right(l, 5)

lbt.add_left(r, 6)
lbt.add_right(r, 7)



print(len(lbt))
print(lbt.height(lbt.root()))
print()

# Test code for previous assignment
print("Preorder traversal:")
for node in lbt.preorder():
    print(node)
print()

print("Postorder traversal:")
for node in lbt.postorder():
    print(node)
print()

print("Inorder traversal:")
for node in lbt.inorder():
    print(node)
print()




# Test code for BST assignment
print("Converting to BST")
lbt.toBST()


print("Inorder traversal after conversion:")
for node in lbt.inorder():
    print(node)
print()