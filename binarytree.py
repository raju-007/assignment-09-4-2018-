# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 11:08:47 2018

@author: rajashekhar
"""

class tree:
 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 

def maxDepth(node):
    if node is None:
        return 0 ; 
 
    else :
 
       
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)
 
        
        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1
 
 
root = tree(1)
root.left = tree(2)
root.right = tree(3)
root.left.left = tree(4)
root.left.right = tree(5)

print ("max depth" ,(maxDepth(root))) 