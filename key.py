#!/usr/bin/ python

class Data():
	""" Satelite data """
	def __init__(self, id, data=None):
		self.id = id
		self.data = data

class Key():
  """Key for R-Tree"""
  def __init__(self, mbr=None, child=None, node=None,):
    self.mbr = mbr
    self.child = child
    self.node = node
