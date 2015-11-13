#!/usr/bin/ python

class MBR():
    """Minimum Bounding region Structure"""
    def __init__(self, minDim=[], maxDim=[]):
        self.minDim = minDim
        self.maxDim = maxDim

    '''
    Area of MBR
    '''
    def Area(self):
        areaCovered = 1
        for i in range(0, len(self.minDim)):
            areaCovered *= (self.maxDim[i] - self.minDim[i])
        return areaCovered

    '''
    return combined MBR of self with another mbr
    '''
    def Combine(self, mbr):
        minDim = []
        maxDim = []
        # get the minimum of minimum and maximum of maximum
        for i in range(0, len(self.minDim)):
            minDim.append(min(self.minDim[i], mbr.minDim[i]))
            maxDim.append(max(self.maxDim[i], mbr.maxDim[i]))
       
        combinedMBR = MBR(minDim, maxDim)
        return combinedMBR


    '''
    gets the pripority for the mbr
    '''
    def Priority(self):
        value = 0
        for val in self.minDim:
            value += val
        return value

    '''
    returns dominate relationship of self and a mbr 
    '''
    def Dominates(self, mbr):
        dims = len(self.maxDim)
        for dim in range(0, dims):
            # check whether upper part of mbr with respect to lower part of self.mbr
            if self.minDim[dim] < mbr.maxDim[dim]:
                return False    
        return True


    '''
    Return whether self overlaps with mbr or not
    '''
    def Overlaps(self, mbr):
        dims = len(self.maxDim)
        for dim in range(dims):
            lowerOverlaps =  self.minDim[dim] <= mbr.minDim[dim] and mbr.minDim[dim] <= self.maxDim[dim]
            if lowerOverlaps:
                return True
            upperOverlaps = mbr.minDim[dim] <= self.minDim[dim] and self.minDim[dim] <= mbr.maxDim[dim]
            if upperOverlaps:
                return True
        return False


    """
    Returns whether self contains mbr or not
    """
    def Contains(self, mbr):
        dims = len(self.maxDim)
        for dim in range(dims):
            lowerContains =  self.minDim[dim] <= mbr.minDim[dim] and mbr.minDim[dim] <= self.maxDim[dim]
            if not lowerContains:
                return False
            upperContains = self.minDim[dim] <= mbr.maxDim[dim] and mbr.maxDim[dim] <= self.maxDim[dim]
            if not upperContains:
                return False
        return True


    """
    Returns whether self equals to or not
    """
    def Equals(self, mbr):
        dims = len(self.maxDim)
        for dim in range(dims):
            lowerEquals =  self.minDim[dim] == mbr.minDim[dim]
            if not lowerEquals:
                return False
            upperEquals = mbr.maxDim[dim] == self.maxDim[dim]
            if not upperEquals:
                return False
        return True
        
