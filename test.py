#!/usr/bin/ python

from rTree import RTree



def printTree(node):
	print node.nodeType
	if node.IsLeaf():
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
	rTree.Insert(rTree.MakeKey([1,2], 0, [3])) 
	rTree.Insert(rTree.MakeKey([2,3], 1, [10]))
	rTree.Insert(rTree.MakeKey([1,3], 2, [13]))
	rTree.Insert(rTree.MakeKey([4,5], 3, [15]))
	rTree.Insert(rTree.MakeKey([2,2], 5) )
	rTree.Insert(rTree.MakeKey([4,3], 6))
	rTree.Insert(rTree.MakeKey([5,5], 7))
	rTree.Insert(rTree.MakeKey([6,7], 8))
	rTree.Insert(rTree.MakeKey([2,10], 9, [11,10]))

	print "<<<<<<<<< Afer Insertion >>>>>>>>>>"
	printTree(rTree.root)


	# rTree.Delete(mbr, [id])
	rTree.Delete(rTree.MakeKey(mbrDim=[4,5]))
	rTree.Delete(rTree.MakeKey(mbrDim=[2,10], id=9))
	rTree.Delete(rTree.MakeKey(mbrDim=[1,10]))
	rTree.Delete(rTree.MakeKey(mbrDim=[1,2]))
	rTree.Delete(rTree.MakeKey(mbrDim=[2,3]))
	rTree.Delete(rTree.MakeKey(mbrDim=[1,3]))
	
	print "deletion > insertion"
	
	rTree.Insert(rTree.MakeKey( [1,2], 0, [3]) )
	rTree.Insert(rTree.MakeKey( [2,3], 1,[10]))
	rTree.Insert(rTree.MakeKey( [1,3], 2,[13]))
	rTree.Insert(rTree.MakeKey( [2,10],9, [11,10]))
	rTree.Insert(rTree.MakeKey( [1,10],4, [1,10]))
	rTree.Insert(rTree.MakeKey( [4,5], 3,[15]))
	
	print "<<<<<<<< After Deletion >>>>>>>>>>"
	printTree(rTree.root)

if __name__ == "__main__":
	main()