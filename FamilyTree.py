
#FamilyTree
#Majority of code taken from http://rosettacode.org/wiki/Tree_traversal#Python and editted to use as example.

__author__ = "Angel Dixon"

from collections import namedtuple
from sys import stdout
 
Node = namedtuple('Node', 'data, left, right')
tree = Node('Grandma',
            Node('Auntie', Node('Cousin', None, None), None),
            Node('Mom',
                 Node('Brother',
                      Node('Niece', None, None),
                      Node('Nephew', None, None)),
                 Node('Sister',
                 Node('Baby', None, None), None)))
                 
aList = []
 
def toList(s):
    global aList
    if s in aList:
    	aList = []
    aList.append("%s" % s)

 
def preorder(node, visitor = toList):
	if node is not None:
		visitor(node.data)
		preorder(node.left, visitor)
		preorder(node.right, visitor)
	return aList
 
def inorder(node, visitor = toList):
    if node is not None:
        inorder(node.left, visitor)
        visitor(node.data)
        inorder(node.right, visitor)
 	return aList

def postorder(node, visitor = toList):
    if node is not None:
        postorder(node.left, visitor)
        postorder(node.right, visitor)
        visitor(node.data)
 	return aList

def levelorder(node, more=None, visitor = toList):
    if node is not None:
        if more is None:
            more = []
        more += [node.left, node.right]
        visitor(node.data)
    if more:    
        levelorder(more[0], more[1:], visitor)
    return aList

#------Used for testing code before PyUnit------IGNORE------#

#stdout.write('  preorder: ')
#preorder(tree)
#print aList
#stdout.write('\n   inorder: ')
#inorder(tree)
#print aList
#stdout.write('\n postorder: ')
#postorder(tree)
#stdout.write('\nlevelorder: ')
#levelorder(tree)
#print aList
#stdout.write('\n')