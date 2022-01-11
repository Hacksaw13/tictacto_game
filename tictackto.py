

def win(current_game):
	def all_same(l):
		if l.count(l[0]) == len(l) and l[0] != 0:
			return True
		else:
			return False
      #horizontal
	for row in game:
           print(row)
           if all_same(row):
                  print(f"player {row[0]} is the winner horizontally!")


      #diagonally
	diags = []
	for col,row in enumerate(reversed(range(len(game)))):
		diags.append(game[row][col])
	if all_same(diags):
		print(f"player{diags[0]} is the winners diagonally")
	diags = []
	for ix in range(len(game)):
		diags.append(game[ix][ix])
	if all_same(diags):
		print(f"player{diags[0]} is the winners diagonally")

             #vertical
	for col in range(len(game)):
		check = []
	for row in game:
		check.append(row[col])

	if all_same(check):
		print(" is the winners vertically")



def game_board(game_map, player=0, row=0, column=0, just_display=False):
	try:
		if game_map[row][column]  != 0:
			print("this position id occupied! choose another")
			return game_map, False
		print("   a  b  c")
		if not just_display:
			game_map[row][column] = player
		for count, row in enumerate(game_map):
			print(count, row)
		return game_map
	except IndexError as e:
		print("Error: did you input roe/column as 0 1 or 2", e)
		return game_map, False
	except Exception as e:
		print("something went wrong at esception error", e)
		return game_map, False

#game=game_board(game,just_display=True)
#game=game_board(game, player=1, row=4, column=1)

play = True
players=[1, 2]
while play:
	game=[[0,0,0],
          [0,0,0],
          [0,0,0]]    
	import itertools
	game_won = False
	game= game_board(game, just_display=True)
	player_choice = itertools.cycle([1, 2])
	while not game_won:
		current_player = next(player_choice)
		print(f"current player:{current_player}")
		played = False


		while not game_won:
				column_choice = int(input("whot column do you want to play? (o, 1, 2):"))
				row_choice = int(input("whot row do you want to play? (o, 1, 2):"))
				game= game_board(game,current_player, row_choice, column_choice)
				if game:
 					played = True

