#FamilyTree Pyunit test class.

__author__ = "Angel D."

import unittest, FamilyTree

class FamilyTreeTestCase(unittest.TestCase):

	def test_preOrder(self):
		l = FamilyTree.preorder(FamilyTree.tree)
		tupL = tuple(l)
		self.assert_(tupL[0] == "Grandma", str(l))
		self.assertFalse((tupL[0] == "Baby"), str(l))
		self.assertIn("Sister", tupL, str(l))

	def test_inOrder(self):
		l = FamilyTree.inorder(FamilyTree.tree)
		tupL = tuple(l)
		self.assertNotEqual(tupL[0], "Grandma", str(l))


	def test_postOrder(self):
		l = FamilyTree.postorder(FamilyTree.tree)
		tupL = tuple(l)
		self.assert_(tupL[0] == "Cousin", str(l))

	def test_levelOrder(self):
		l = FamilyTree.levelorder(FamilyTree.tree)
		tupL = tuple(l)
		self.assert_(tupL[0] == "Grandma", str(l))

if __name__ == '__main__':
	unittest.main()


