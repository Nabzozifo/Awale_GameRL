import awale as a
import random
import player as p
class Game():

	def playgGame(self,player1,player2):
		def play_player(players):
			his_part=True
			#print("graines : ",players.graines)
			indexdeb=random.choice([i for i in range(len(players.graines))])
			action=players.graines[indexdeb]
			#print("graines : ",players.graines)
			index=indexdeb
			while action>0:
				if index < len(players.graines)-1 and his_part:
					index=index+1
					players.graines[index]+=1
					players.graines[indexdeb]-=1
					action=action-1
					print("graines if : ",players.graines)
				else:
					his_part=False
					index=0
					if players.cote=='Nord':
						player2.graines[index]+=1
						players.graines[indexdeb]-=1
						action=action-1
					else :
						player1.graines[index]+=1
						players.graines[indexdeb]-=1
						action=action-1
					print("graines else : ",players.graines)
					index+=1
		player1_turn=True
		player2_turn=False
		if player1_turn==True and player2_turn==False :
			play_player(player1)
			player1_turn==False
			player2_turn==True
		elif player1_turn==False and player2_turn==True:
			play_player(player2)
			player1_turn==True
			player2_turn==False

	

game=Game()
aw=a.Awale()
p1=p.player('Nord',aw)
p2=p.player('Sud',aw)
print(p1.cote,p1.num_graine,p1.graines)
print(p2.cote,p2.num_graine,p2.graines)
game.playgGame(p1,p2)
print(p1.cote,p1.num_graine,p1.graines)
print(p2.cote,p2.num_graine,p2.graines)