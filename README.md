# R-Tree
 Implemented in python language

## Usage
> from rTree import RTree

> \# Create instance of class RTree by passing value of M ( maximum allowed size for a node ) and m (minimum allowed size for a node ) to the constructor

> M, m = 4, 2

> rTree = RTree(M, m)

> \# To insert a key into R-Tree

    key = rTree.MakeKey(mbrDimensions, [ tupleId ], [ sateliteData ])
 
    rTree.Insert(key)

> tupleId = 1 
> mbrDimensions = [1,2]
> data = [3,4,6]
> key = rTree.MakeKey( mbrDimensions, tupleId, data)
> rTree.Insert(key)

> \# To delete a key from R-Tree
    
    rTree.Delete(key)
    
> rTree.Delete(rTree.MakeKey(mbrDim=[1,2]))    

> \# To access root of the rTree 

> root = rTree.root

## Info about keys in rTree
> each key in rTree contains it's <mbr>, <child>, <node>

> mbr = minimum bounding region for key

> child = child to which this key points

> node = node in which this key is present

## Info about nodes in rTree
> each node in rTree contains it's <parent>, <keys>, <nodeType>

> parent = parent key for node, None for root

> keys = an list of keys within the node

> nodeType = an enum for node typle from {NodeType.root, NodeType.node, NodeType.leaf}
