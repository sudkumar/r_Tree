#!/usr/bin/ python

from node import *

class RTree():
  """R-Tree Class"""
  def __init__(self, M, m):
    self.M = M
    self.m = m
    self.root = Node()

  '''
  K = Key()
  Insert new tuple Key in tree
  '''
  def Insert(self, tupleId, minDim, maxDim):
      
    # create the key to insert
    mbr = MBR(minDim, maxDim)
    K = Key(tupleId, mbr)

    # Find position for new record
    leafNode = self.ChooseLeaf(self.root, K)
    K.node = leafNode


    N1 = None
    N2 = None

    # add record to leaf if it has space
    if not leafNode.IsFull(self.M):
      leafNode.keys.append(K)
      N1 = leafNode
    # else make a split after adding node to leaf
    else:
      leafNode.keys.append(K)
      N1, N2 = leafNode.Split(self.m)
    # now adjust the tree
    self.AdjustTree(N1, N2)

  '''
  K = Key()
  Find leaf node for new Key in tree
  '''
  def ChooseLeaf(self, N, K):
    if(N.nodeType == NodeType.leaf):
      return N
    # intialization 
    minExpandableArea = float("inf")
    L = Node()

    for key in N.keys:
      combinedArea = key.mbr.Combine(K.mbr)                        
      expandableArea = combinedArea.Area() - key.mbr.Area()
      
      if(minExpandableArea == None or minExpandableArea > expandableArea):
        minExpandableArea = expandableArea
        L = key.childNode
      elif(minExpandableArea == expandableArea):
        if L.MBR().Area() > key.mbr.Area():
          L = key.childNode
    return self.ChooseLeaf(L, K)

  '''
  N = leafNode
  NN = if N was previously splitted
  Ascend from a leaf node L to the root, adjusting covering rectangles,
  and propagating node splits if necessary
  '''
  def AdjustTree(self, N1, N2 = None):
    # check if done
    if(N1.parent == None):
      # reached at root
      if(N2 != None):
        # root was splitted
        self.MakeRoot(N1, N2)
      return 

    # update the parents mbr for N1
    N1.parent.mbr = N1.MBR()

    # get the parent node
    parentNode = N1.parent.node


    # if previously node was splitted, make a new parent node and 
    # then do some adjustment
    if N2 != None:
     # make a new key which is parent of splited node
      newKey = Key(mbr=N2.MBR(), node=parentNode)
      N2.parent = newKey
      newKey.childNode = N2
      # add this new key to parent of N1 if it is not full 
      # else add and split parent
      if not parentNode.IsFull(self.M):
        parentNode.keys.append(newKey)
        return self.AdjustTree(parentNode, None)
      else:
        parentNode.keys.append(newKey)
        N, NN = parentNode.Split(self.m)
        return self.AdjustTree(N, NN)
    # else Adjust the parent node
    else:
      return self.AdjustTree(parentNode, None)


  '''
  Make a root with given two nodes which are result of a split
  '''
  def MakeRoot(self, N1, N2):

    if(N1.nodeType != NodeType.leaf):
      N1.nodeType = NodeType.node
    if(N2.nodeType != NodeType.leaf):
      N2.nodeType = NodeType.node

     # create a new node
    self.root = Node(nodeType=NodeType.root)
    # create key for N1
    newKey = Key(mbr=N1.MBR(), node=self.root)
    N1.parent = newKey
    newKey.childNode = N1
    
    self.root.keys.append(newKey)
    # create key for N2
    newKey = Key(mbr=N2.MBR(), node=self.root)
    N2.parent = newKey
    newKey.childNode = N2
    self.root.keys.append(newKey)
   

  def Delete(self, tupleId, minDim, maxDim):
    if len(self.root.keys) == 0:
      print "Tree is empty"
      return

    # create the key for search
    mbr = MBR(minDim, maxDim)
    K = Key(tupleId, mbr)

    # Find leaf node that contains this key
    leafNode = self.FindLeaf(self.root, K)
    if not leafNode:
      print "Key not present in Tree"
      return 

    # remove key from leaf node
    numKeys = len(leafNode.keys)
    keyFound = False
    for i in range(numKeys):
      if leafNode.keys[i].tupleId == K.tupleId:
        keyFound = True
        leafNode.keys.pop(i) 
        break
    if not keyFound:
      print "Key not present"
      return
    # propagate MBR changes upwards
    self.CondenseTree(leafNode, []) 

    # update root if it don't have  keys >= 2
    if self.root.nodeType == NodeType.root and len(self.root.keys) == 1:
      childNode = self.root.keys[0].childNode
      self.root = childNode
      self.root.parent = None
      for key in self.root.keys:
        key.node = self.root
      if self.root.nodeType == NodeType.node:
        self.root.nodeType = NodeType.root



  """
  Find leafnode that contains K in subtree rooted at N
  """
  def FindLeaf(self, N, K):
    # return for recursive calls if we are at leaf
    if N.nodeType == NodeType.leaf:
      if N.MBR().Contains(K.mbr):
        return N
      else:
        return None

    # else iterate through all the keys in N find K if it is there
    keys = N.keys
    for key in keys:
      if key.mbr.Overlaps(K.mbr):
        L = self.FindLeaf(key.childNode, K)
        if L:
          return L
    # key not found in N, return None
    return None

  """
  Adjust Tree by condensing it's height after any deletion operation
  @params: N: node where entries have been modified
  @params: EN: list of eliminated nodes during adjustment (if it's size goes below m)
  """
  def CondenseTree(self, N, EN):
    if N.nodeType != NodeType.root and N.parent != None:
      # get the parent key of N
      parentKey = N.parent

      # get the parent node
      P = parentKey.node

      # check if N underflows or not
      if N.Underflows(self.m):
        P.keys.remove(parentKey)
        EN.append(N)
      else:
        parentKey.mbr = N.MBR()

      self.CondenseTree(P, EN)
    # we are at root node
    elif len(EN) != 0:
      # EN is not empty
      while len(EN) != 0:
        # we are looping in reverse direction because items are inserted in 
        # order of increasing height and we want none leaf node to place at the height
        # where the were previously
        node = EN.pop()
        # if node N was from a leaf, then insert at leaf
        if node.nodeType == NodeType.leaf:
          for key in node.keys:
            self.Insert(key.tupleId, key.mbr.minDim, key.mbr.maxDim)
        else:
          # insert at the same heigt as it was removed to maintain it's leaves at the same height as main tree
          # the parent key of the node was removed because of onderflow, so search in it's siblings where we can add it 
          # so the area expansion is minimum
          parentNode = node.parent.node
          minExpandableArea = float("inf")
          myFriendNode = None

          for key in parentNode.keys:
            nodeMBR = N.MBR()
            keyMBR = key.mbr
            combinedArea = keyMBR.Combine(nodeMBR).Area()
            expandableArea = combinedArea - keyMBR.Area() - nodeMBR.Area()
            if minExpandableArea > expandableArea:
              minExpandableArea = expandableArea
              myFriendNode = key.childNode
        
          if myFriendNode:
            # add node to friend node (add keys of node into friend node)
            # check the node attribute of key from node to myFriendNode
            for key in node:
              key.node = myFriendNode

            myFriendNode.keys = myFriendNode.keys + node.keys
            if myFriendNode.Overflows(self.M):
              print "Node goes overflow after adding deleted, so doing adjustment"
              N1, N2 = myFriendNode.Split(self.m)
              self.AdjustTree(N1, N2)
          else:
            # there is no keys left in parent node
            # this case won't arise, just to see if it does
            print "Unable to get friend node for removed node"