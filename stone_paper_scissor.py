'''
# Filename: stone_paper_scissor
# extension: python
# Type: command line (CUI)
# genre: Game/QUIZ
# version: 0.1
# Narrated by: Shiv
# Developed by: Kshitij
# Date: 5/5/2020
'''
import sys
import random
class SPS:
	playerA = 0
	playerB = 0
	winTime = [0,0,0]
	total_number_of_game_played = 0
	player_name = ["Player A","Player B"]
	
	def __init__(self):
		try:	
			self.game_title()
			self.reset_player_name()
			self.set_player_name()
			prompt = self.prompt_choice()
			while(prompt != 4):
				if prompt == 1:
					self.procedure()
				if prompt == 2:
					self.rename_player()
				if prompt == 3:
					self.help()
				if prompt == 4:
					break
					self.exit()
				if prompt == 5:
					import stone_paper_scissor as sps
					print(help(sps))
				prompt = self.prompt_choice()
		except Exception as e:
			print("/*/"*25)
			print(e)
		
	def procedure(self):
		player_A = self.choice()
		self.set_playerA_choice(player_A)
		self.reset_score_board()
		while(player_A != 4):
			self.set_playerB_choice(int(random.randint(1,3)))
			self.set_playerA_choice(player_A)
			print("***"*26)
			print(f"{self.get_playerA_name()} : {self.get_character_by_choice(self.get_playerA_choice())}")
			print(f"{self.get_playerB_name()} : {self.get_character_by_choice(self.get_playerB_choice())}")
			self.final_decision()
			self.increment_game_played()
			print("***"*26)
			self.score_board()
			print(f"Number of times games played: {self.get_total_number_of_time_game_played()}")
			player_A = self.choice()
			if player_A == 4:
				self.game_over()
				self.exit()
			if player_A == 5:
				break
		
	def prompt_choice(self):
		ch = input(f"Player Name: {self.get_playerA_name()}, enter your choice:\n1: Play\n2: Rename player data\n3: Help\n4: Exit\n5: About\nI'm waiting for your choice: ")
		while(ch.isdecimal() != True):
			print("Incorrect choice error: 400, Try again:-")
			ch = input(f"({self.get_playerA_name()}) something went wrong. You have to try again, read the choice instruction carefully then the appropriate choice\n1: Play\n2: Rename player data\n3: Help\n4: Exit\n5: About\nI'm waiting for your choice: ")
		return int(ch)
			
	def play(self):
		player_A = self.choice()
		self.set_playerA_choice(player_A)
		self.reset_score_board()
		while(player_A != 4):
			self.set_playerB_choice(int(random.randint(1,3)))
			print("***"*26)
			print(f"{self.get_playerA_name()} : {self.get_character_by_choice(self.get_playerA_choice())}")
			print(f"{self.get_playerB_name()} : {self.get_character_by_choice(self.get_playerB_choice())}")
			self.final_decision()
			self.increment_game_played()
			print("***"*26)
			self.score_board()
			print(f"Number of times games played: {self.get_total_number_of_time_game_played()}")
			player_A = self.choice()
			self.set_playerA_choice(player_A)
			if player_A == 4:
				self.game_over()
			break
	def exit(self):
		print('''
			_______________  ___.______________
			\_   _____/\   \/  /|   \__    ___/
			 |    __)_  \     / |   | |    |   
			 |        \ /     \ |   | |    |   
			/_______  //___/\  \|___| |____|   
				\/       \_/               	
		''')
		sys.exit(0)
		
	def rename_player(self):
		self.reset_player_name()
		self.set_player_name()
		self.clear_total_number_played_time()
	
	def score_board(self):
		'''
		Method name: scoreboard
		parameter: none
		It'll print the scoreboard, the user(player) can see their progress.
		'''
		print(f"Score Board: \t {self.get_playerA_name()} : {self.winTime[0]} \t {self.get_playerB_name()} : {self.winTime[1]} \t Draw: {self.winTime[2]}")
	
	def set_playerA_choice(self, choice):
		if self.is_right_choice(choice):
			self.playerA = choice
			
	def set_playerB_choice(self, choice):
		if self.is_right_choice(choice):
			self.playerB = choice
			
	def reset_choice(self):
		self.playerA = 0
		self.playerB = 0
		
	def get_playerA_choice(self):
		return self.playerA
		
	def get_playerB_choice(self):
		return self.playerB
		
	def is_right_choice(self, choice):
		if choice >= 1 and choice <= 3:
			return True
		return False
	
	def get_character_by_choice(self, choice):
		character = "None"
		if choice == 1:
			character = "Stone"
		elif choice == 2:
			character = "Paper"
		elif choice == 3:
			character = "Scissor"
		else:
			character = "None"
			print("Undefined character, Error code: 401.")
		return character
	
	def is_player_win(self, winner, loser):
		if winner == 1 and loser == 3:
			print("Scissor had broken due the stone stike on it.")
			return True
		if winner == 2 and loser == 1:
			print("Paper had wrapped up the stone.")
			return True
		if winner == 3 and loser == 2:
			print("Scissor had cut the paper.")
			return True
		return False
		
	def is_draw(self, player_A, player_B):
		if player_A == 1 and player_B == 1:
			return True
		if player_A == 2 and player_B == 2:
			return True
		if player_A == 3 and player_B == 3:
			return True
		return False
	
	def final_decision(self):
		if self.is_player_win(self.get_playerA_choice(), self.get_playerB_choice()):
			self.winTime[0] += 1
			print(f"Final decision: {self.get_playerA_name()} win.")
		if self.is_player_win(self.get_playerB_choice(), self.get_playerA_choice()):
			self.winTime[1] += 1
			print(f"Final decision: {self.get_playerB_name()} win.")
		if self.is_draw(self.get_playerA_choice(), self.get_playerB_choice()):
			self.winTime[2] += 1
			print(f"Final decision: Game has been draw, due to the both palyer had pick the same game character.")
	def reset_score_board(self):
		self.winTime[0] = 0
		self.winTime[1] = 0
		self.winTime[2] = 0
	
	def increment_game_played(self):
		self.total_number_of_game_played += 1
	
	def get_total_number_of_time_game_played(self):
		return self.total_number_of_game_played
	def clear_total_number_played_time(self):
		self.total_number_of_gane_played = 0;
	
	def reset_player_name(self):
		self.player_name[0] = "Player A"
		self.player_name[1] = "Player B"
	
	def set_player_name(self):
		self.set_playerA_name(str(input("Enter your name(Player A): ")).split(" ")[0])
		self.set_playerB_name(str(input("Enter your name(Player B): ")).split(" ")[0])
		
	def set_playerA_name(self, name):
		if self.get_playerB_name() != name:
			self.player_name[0] = name
		else:
			self.name_error_clarified()
					
	def set_playerB_name(self, name):
		name = str(name) + str(" (PC)")
		if self.get_playerA_name() != name:
			self.player_name[1] = name
		else:	
			self.name_error_clarified()
			
	def name_error_clarified(self):
		print("/*/"*26)
		print("\nProblem resolve (Error clarified):")
		print("The user had been entered same name in the place of player a and player b.\n")
		print("/*/"*26)
		
	def get_playerA_name(self):
		return self.player_name[0]
		
	def get_playerB_name(self):
		return self.player_name[1]
	
	def choice(self):
		player_A = input(f"Hey {self.get_playerA_name()}, enter your choice:\n1: Stone\n2: Paper\n3: Scissor\n4: Exit\n5:Return\nI'm waiting for your choice: ")
		while(player_A.isdecimal() != True):
			print("Incorrect choice error: 402, Try again:-")
			player_A = input(f"Hey ({self.get_playerA_name()}) something went wrong. You have to try again, read the choice instruction carefully then the appropriate choice:\n1: Stone\n2: Paper\n3: Scissor\n4: Exit\n5:Return\nI'm waiting for your choice: ")
		return int(player_A)
	
	def game_over(self):
		print("\n")
		print("#@#"*26)
		print("\n")
		print('''
			  ____    _    __  __ _____    _____     _______ ____  
			 / ___|  / \  |  \/  | ____|  / _ \ \   / / ____|  _ \ 
			| |  _  / _ \ | |\/| |  _|   | | | \ \ / /|  _| | |_) |
			| |_| |/ ___ \| |  | | |___  | |_| |\ V / | |___|  _ < 
			 \____/_/   \_\_|  |_|_____|  \___/  \_/  |_____|_| \_\
									       
		''')
		print("\n")
		high_score = max(self.winTime[0], self.winTime[1])
		if self.winTime[0] == self.winTime[1]:
			print(f"Draw condition, both player has equal high score.")
		elif self.winTime[0] == high_score:
			print(f"{self.get_playerA_name()} is winner of the game")
			print(f"Congratulation, {self.get_playerA_name()}\nYou've been created a new high score: {high_score}")
		elif self.winTime[1] == high_score:
			print(f"{self.get_playerB_name()} is winner of the game")
			print(f"Congratulation, {self.get_playerB_name()}\nYou've been created a new high score: {high_score}")
		print("Good bye!")
		print("\n")
		print("#@#"*26)
			
	def game_title(self):
		print('''
	_\/_ _\/_ _\/_ _\/_ _\/_ _\/_ _\/_ _\/_ _\/_ _\/_ _\/_ _\/_ 
	 /\   /\   /\   /\   /\   /\   /\   /\   /\   /\   /\   /\  
  __ ___ _       ___    __   _  __  ___ __      __   _  ___  __   __   _  __  
 (_ ` ) / ) )\ ) )_     )_) /_) )_) )_  )_)    (_ ` / `  )  (_ ` (_ ` / ) )_) 
.__) ( (_/ (  ( (__    /   / / /   (__ / \    .__) (_. _(_ .__) .__) (_/ / \  
                     
	_\/_ _\/_ _\/_ _\/_ _\/_ _\/_ _\/_ _\/_ _\/_ _\/_ _\/_ _\/_ 
	 /\   /\   /\   /\   /\   /\   /\   /\   /\   /\   /\   /\                                                           										  
               ''')
	
def main():
	sps = SPS()
	
if __name__ == "__main__":
	main()