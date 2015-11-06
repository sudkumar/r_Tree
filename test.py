#!/usr/bin/ python

from rTree import RTree
from node import NodeType

def printTree(node):
	print node.nodeType
	if node.nodeType == NodeType.leaf:
		for key in node.keys:
			print key.tupleId, key.mbr.minDim

	else:
		for key in node.keys:
			print node.MBR().minDim, node.MBR().maxDim
			printTree(key.childNode)
	
def main():
	M = 6
	m = M/2
	rTree = RTree(M,m)


	rTree.Insert(0, [1,2], [1,2]) 
	
	rTree.Insert(1, [2,3], [2,3])

	rTree.Insert(2, [1,3], [1,3])

	rTree.Insert(3, [4,5], [4,5])


	rTree.Insert(5, [2,2], [2,2]) 
	
	rTree.Insert(6, [4,3], [4,3])

	rTree.Insert(7, [5,5], [5,5])

	rTree.Insert(8, [6,7], [6,7])

	rTree.Insert(9, [2,10], [2,10])

	print "<<<<<<<<< Afer Insertion >>>>>>>>>>"
	printTree(rTree.root)


	rTree.Delete(3, [4,5], [4,5])
	rTree.Delete(9, [2,10], [2,10])
	rTree.Delete(4, [1,10], [1,10])
	rTree.Delete(0, [1,2], [1,2]) 
	
	rTree.Delete(1, [2,3], [2,3])

	rTree.Delete(2, [1,3], [1,3])

	print "deletion > insertion"
	
	rTree.Insert(0, [1,2], [1,2]) 
	rTree.Insert(1, [2,3], [2,3])
	rTree.Insert(2, [1,3], [1,3])

	rTree.Insert(9, [2,10], [2,10])
	rTree.Insert(4, [1,10], [1,10])
	rTree.Insert(3, [4,5], [4,5])
	
	print "<<<<<<<< After Deletion >>>>>>>>>>"
	printTree(rTree.root)

if __name__ == "__main__":
	main()