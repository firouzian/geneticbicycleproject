#!/usr/bin/python

class Gene(object):
	"""Station class"""

	def __init__(self, M1_x, M1_y, M2_x, M2_y, W1_x, W1_y, W2_x, W2_y, ):
		self.name = sname # station name
		self.stock = inistock #represents how many packages are there in a station
		self.trainlist = initrainlist

	def s_load(self):
		for trs in self.trainlist:
			for i,pck in enumerate(self.stock):
				if trs.isfull():
					break
				elif trs.destination==pck.destStation:
					trs.t_load(self.stock[i])
					del self.stock[i]


	def s_unload(self):
		for trs in self.trainlist:
			self.stock.append(trs.tstock)
			trs.t_unload()

	def checkTrains(self):
		return len(self.trainlist)

	def checkStock(self):
		return len(self.stock)

	def deliverstock(self,merc):
		self.stock.append(merc) # merc: Merchandise; 

	def delivertrain(self,trs):
		self.trainlist.append(trs)