#!/usr/bin/ python

from rTree import RTree, NodeType, Key, Data



def printTree(node):
	print node.nodeType
	if node.nodeType == NodeType.leaf:
		for key in node.keys:
			print key.child.id, key.mbr.minDim, key.child.data

	else:
		for key in node.keys:
			print node.MBR().minDim, node.MBR().maxDim
			printTree(key.child)
	
def main():
	M = 6
	m = M/2
	rTree = RTree(M,m)


	# rTree.Insert(id, mbr, [sateliteData])
	rTree.Insert(rTree.MakeKey(0, [1,2],  [3])) 
	rTree.Insert(rTree.MakeKey(1, [2,3], [10]))
	rTree.Insert(rTree.MakeKey(2, [1,3], [13]))
	rTree.Insert(rTree.MakeKey(3, [4,5], [15]))
	rTree.Insert(rTree.MakeKey(5, [2,2]) )
	rTree.Insert(rTree.MakeKey(6, [4,3]))
	rTree.Insert(rTree.MakeKey(7, [5,5]))
	rTree.Insert(rTree.MakeKey(8, [6,7]))
	rTree.Insert(rTree.MakeKey(9, [2,10], [11,10]))

	print "<<<<<<<<< Afer Insertion >>>>>>>>>>"
	printTree(rTree.root)


	# rTree.Delete(mbr, [id])
	rTree.Delete([4,5])
	rTree.Delete([2,10], 9)
	rTree.Delete([1,10])
	rTree.Delete([1,2]) 
	rTree.Delete([2,3])
	rTree.Delete([1,3])

	print "deletion > insertion"
	
	rTree.Insert(rTree.MakeKey(0, [1,2],  [3]) )
	rTree.Insert(rTree.MakeKey(1, [2,3], [10]))
	rTree.Insert(rTree.MakeKey(2, [1,3], [13]))
	rTree.Insert(rTree.MakeKey(9, [2,10], [11,10]))
	rTree.Insert(rTree.MakeKey(4, [1,10], [1,10]))
	rTree.Insert(rTree.MakeKey(3, [4,5], [15]))
	
	print "<<<<<<<< After Deletion >>>>>>>>>>"
	printTree(rTree.root)

if __name__ == "__main__":
	main()