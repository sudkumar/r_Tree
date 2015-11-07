# R-Tree
 Implemented in python language

## Usage
> from rTree import RTree

> \# Create instance of class RTree by passing value of M ( maximum allowed size for a node ) and m (minimum allowed size for a node ) to the constructor

> M, m = 4, 2

> rTree = RTree(M, m)

> \# To insert a key into R-Tree

> tupleId = 1
> mbrMinDimensions = [1,2]
> mbrMaxDimensions =  [2,3]
> rTree.Insert(tupleId, mbrMinDimensions, mbrMaxDimensions)

> \# To access root of the rTree 

> root = rTree.root

## Info about keys in rTree
> each key in rTree contains it's <mbr>, <child>, <tupleId>, <node>

> mbr = minimum bounding region for key

> child = child to which this key points, None for leaf keys

> tupleId = tupleId for key, Node for other than leaf keys

> node = node in which this key is present

## Info about nodes in rTree
> each node in rTree contains it's <parent>, <keys>, <nodeType>

> parent = parent key for node, None for root

> keys = an list of keys within the node

> nodeType = an enum for node typle from {NodeType.root, NodeType.node, NodeType.leaf}
