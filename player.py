import awale as a
class player():
	def __init__(self,cote,awale):
		self.num_graine=sum(awale.plateau[cote])
		self.cote=cote
		self.graines=awale.plateau[cote]

"""aw=a.Awale()
player1=player('Nord',aw)
print(player1.cote,player1.num_graine,player1.graines)"""
