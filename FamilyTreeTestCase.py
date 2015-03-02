#FamilyTree Pyunit test class.

__author__ = "Angel D."

import unittest, FamilyTree

class FamilyTreeTestCase(unittest.TestCase):

	def test_preOrder(self):
		preList = FamilyTree.preorder(FamilyTree.tree)
		self.assert_(preList[0] == "Grandma", str(preList))
		self.assertFalse((preList[0] == "Baby"), str(preList))
		self.assertIn("Me", preList, str(preList))

	def test_inOrder(self):
		inList = FamilyTree.inorder(FamilyTree.tree)
		self.assertNotEqual(inList[0], "Grandma", str(inList))


	def test_postOrder(self):
		postList = FamilyTree.postorder(FamilyTree.tree)
		self.assert_(postList[0] == "Cousin", str(postList))

	def test_levelOrder(self):
		levelList = FamilyTree.levelorder(FamilyTree.tree)
		self.assert_(levelList[0] == "Grandma", str(levelList))

if __name__ == '__main__':
	unittest.main()


