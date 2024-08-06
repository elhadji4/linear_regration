import random
import copy

# Object used to create new boards

class Board:
    def __init__(self, size):
        self.size = size
        self.board = []

    # Used to fill the "board" property with a list with a length equal to the "size" property
    def create_board(self):
        for y_pos in range(self.size):
            for x_pos in range(self.size):
                #  Create a Tile instance  
                
                #  Gives it the coordinates (depending on x_pos and y_pos)
                #  Add it to the board property
                if x_pos != 0 and x_pos != 7 and y_pos != 0 and y_pos != 7:
                    self.board.append(Tile(x_pos, y_pos, "🟩", "🟩"))
                else:
                    self.board.append(Tile(x_pos, y_pos, "X", "🟩"))
        self.place_initial_pawns()

    #  This will print the game board, depending on the data_type
    #  Data types are "Coordinates", "Type" and "Content"
    def draw_board(self, data_type):
        display_board = []
        line_breaker = 0
        print([0, ' 0', ' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7'])
        for board_index in self.board:
            if (board_index.x_pos == 0):
                display_board.append(board_index.y_pos)
            if data_type == "Coordinates":
                display_board.append([board_index.x_pos, board_index.y_pos])
            elif data_type == "Type":
                display_board.append(board_index.type)
            else:
                display_board.append(board_index.content)
            line_breaker += 1
            if line_breaker > 7:
                print(display_board)
                line_breaker = 0
                display_board = []
        print("\n")

    # Place the 4 initial pawns at the center of the board (2 white and 2 black)
    def place_initial_pawns(self):
        #  We pick the 4 central tiles
        #  And place 2 black pawns and 2 white pawns
        self.board[27].content = "⚪"
        self.board[28].content = "⚫"
        self.board[35].content = "⚫"
        self.board[36].content = "⚪"

    # Check if the position in inside the board
    # Return true or false depending if it is inside or not
    def is_on_board(self, x_pos, y_pos):
        if x_pos < 0 or x_pos > 7 or y_pos < 0 or y_pos > 7:
            return False
        else:
            return True

    # Check if the tile is an empty tile ("🟩")
    # Return true or false depending if it is empty or not
    def is_tile_empty(self, x_pos, y_pos):
        if self.board[(x_pos) + y_pos * 8].content == "🟩":
            return True
        else:
            return False

    # Takes a position (x_pos, y_pos) and a color 
    # Try to simulate the move
    # Returns either false if the move is not valid
    # Or returns which pawns will change color if true
    # The returned list will contain [numbers_of_pawns_to_change, [direction_x, direction_y]]
    def is_legal_move(self, x_pos, y_pos, color):

        # North / Nort-East / East / South-East / South / South-West / West / North-West
        directions = [
            [0, -1],
            [1, -1],
            [1, 0],
            [1, 1],
            [0, 1],
            [-1, 1],
            [-1, 0],
            [-1, -1],
        ]

        # Opposite of the color of the placed pawn
        if color == "⚪":
            awaited_color = "⚫"
        else:
            awaited_color = "⚪"

        current_x_pos = x_pos
        current_y_pos = y_pos
        is_legal = False
        # [number_of_tile_to_flip, direction]
        # Si on a un pion noir placé en 2,3, on veut:
        # [[1, [1, 0]]
        tiles_to_flip = []

        if (not self.is_tile_empty(current_x_pos, current_y_pos) or not self.is_on_board(current_x_pos, current_y_pos)):
            return False

        # Check for every direction
        for current_dir in directions:
            number_of_tiles_to_flip = 1
            # Get your original coordinates + the direction modifier
            current_x_pos = x_pos + current_dir[0]
            current_y_pos = y_pos + current_dir[1]
            # Check if the new position is on the board and empty
            if self.is_on_board(current_x_pos, current_y_pos):
                #  Get the tile informations
                current_index = self.board[current_x_pos + current_y_pos * 8]
                # If the tile contains a pawn of the opposite color, continue on the line
                while current_index.content == awaited_color:
                    current_x_pos += current_dir[0]
                    current_y_pos += current_dir[1]
                    if self.is_on_board(current_x_pos, current_y_pos):
                        current_index = self.board[current_x_pos +
                                                   current_y_pos * 8]
                        # If the line ends with a pawn of your color, then the move is legal
                        if current_index.content == color:
                            is_legal = True
                            tiles_to_flip.append(
                                [number_of_tiles_to_flip, current_dir])
                            break
                    else:
                        break
                    number_of_tiles_to_flip += 1

        if is_legal:
            return tiles_to_flip
        else:
            return False

    # Takes a position (x_pos, y_pos), an array with a number of tiles to flip and a direction, and a color
    # The array should be obtained with the "is_legal_move" function
    # Doesn't return anything, but will change the color of the tiles selected by "tiles_to_flip"
    def flip_tiles(self, x_pos, y_pos, tiles_to_flip, color):
        # x_pos and y_pos = new pawn position
        # tiles_to_flip = list containing the number of pawn to flip and a direction
        # ex: [
        # [1, [1, 0]],
        # ] means we're changing 1 pawn to the right
        # color = the new color of the pawns to flip
        for current_dir in tiles_to_flip:
            current_x_pos = x_pos + current_dir[1][0]
            current_y_pos = y_pos + current_dir[1][1]
            for nb_tile in range(current_dir[0]):
                current_index = self.board[current_x_pos + current_y_pos * 8]
                current_index.content = color
                current_x_pos += current_dir[1][0]
                current_y_pos += current_dir[1][1]

# Used to create each tile of your board
# Contains a position (x, y), a type to check if it's a boder tile or not, and a content to check if there is a pawn inside the tile


class Tile:
    #   Type is used to check if its an "🟩" empty tile or a "X" border tile
    #   Content is used to check if a pawn is placed o (Empty), B (Black), W (White)
    def __init__(self, x_pos, y_pos, type, content):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.type = type
        self.content = content

# Used to create new ruleset
# Contains the score, the active player, the game_over check and functions allowing to interact with the game


class Game:
    def __init__(self):
        self.score_black = 2
        self.score_white = 2
        self.active_player = "⚫"
        self.is_game_over = False
        self.winner = "Noone"

    # Place a pawn on the board (checks if the move is legal before placing it)
    # It takes a position (x, y), a Board object instance and a color
    # The function will automatically check if the move is valid or not
    def place_pawn(self, x_pos, y_pos, board_instance, color):
        if not board_instance.is_on_board(x_pos, y_pos):
            print("Coordinates outside the board")
        else:
            if board_instance.board[(x_pos) + y_pos * 8].content == "🟩":
                tiles_to_flip = board_instance.is_legal_move(
                    x_pos, y_pos, color)
                if not tiles_to_flip:
                    print("Invalid move")
                else:
                    board_instance.board[(x_pos) + y_pos * 8].content = color
                    board_instance.flip_tiles(
                        x_pos, y_pos, tiles_to_flip, color)
                    print(f"Pion placé en {x_pos}, {y_pos}")
                    self.update_score(board_instance)
                    self.change_active_player()
                    self.check_for_valid_moves(board_instance)
                    board_instance.draw_board("Content")
            else:
                print("There is already a pawn here")

    # Change the active player color from black to white or white to black
    def change_active_player(self):
        # Prend self.active_player et change la couleur du joueur actif
        if self.active_player == "⚫":
            self.active_player = "⚪"
            print("C'est au tour du joueur blanc")
        else:
            self.active_player = "⚫"
            print("C'est au tour du joueur bot ")

    # Update the players score after a successful move
    def update_score(self, board_instance):
        # Count all the black & white pawns, and update the scores
        w_score = 0
        b_score = 0
        for tile_index in board_instance.board:
            if tile_index.content == "⚪":
                w_score += 1
            elif tile_index.content == "⚫":
                b_score += 1
        self.score_black = b_score
        self.score_white = w_score

    # Check for a valid move, and end the game if there is none for the current player
    def check_for_valid_moves(self, board_instance):
        is_game_over = True
        for tile_index in board_instance.board:
            move_to_check = board_instance.is_legal_move(
                tile_index.x_pos, tile_index.y_pos, self.active_player)
            if move_to_check != False:
                is_game_over = False

        if is_game_over:
            self.check_for_winner()
            self.is_game_over = True

    # Compare the score, and print the winner's color
    def check_for_winner(self):
        print("Partie terminée !")
        print("Le joueur noir a: " + str(self.score_black) + " points")
        print("Le joueur white a: " + str(self.score_white) + " points")
        if (self.score_black > self.score_white):
            print("Le joueur noir a gagné !")
            self.winner = "⚫"
        elif (self.score_white > self.score_black):
            print("Le joueur white a gagné !")
            self.winner = "⚪"
        else:
            print("Égalité !")




class Bot_Françis_nganou:
    def __init__(self):
        self.name = "Françis Nganou"
        self.counter = 0

    # BOT FUNCTIONS
    def get_distance_to_border(self, x, y):
    # Calcule la distance d'une position par rapport aux bordures
        return min(x, 7 - x, y, 7 - y)
    

    def simulate_opponent_move(self, c_board, game, opponent_color):

        # Effectue une simulation du mouvement de l'adversaire
        opponent_moves = []

        if self.counter > 5:
            for tile in c_board.board:
                
                t_to_flip = c_board.is_legal_move(tile.x_pos, tile.y_pos, opponent_color)
                if t_to_flip is not False:
                    opponent_moves.append([tile, t_to_flip])

            if opponent_moves:
                # Choix aléatoire d'un mouvement de l'adversaire
                simulated_move = random.choice(opponent_moves)
                x, y = simulated_move[0].x_pos, simulated_move[0].y_pos

                # Appliquer le mouvement simulé sur une copie du tableau sans utiliser place_pawn
                simulated_board = copy.deepcopy(c_board)
                #simulated_game = copy.deepcopy(game)
                simulated_board.board[(x) + y * 8].content = opponent_color
                for flip_info in simulated_move[1]:
                    for i in range(flip_info[0]):
                        flip_x = x + i * flip_info[1][0]
                        flip_y = y + i * flip_info[1][1]
                        simulated_board.board[flip_x + flip_y * 8].content = opponent_color
                        self.counter +=1
                return simulated_board

            return None  
  
    
    def check_valid_moves(self , c_board , game):
      
        #virtual_board = copy.deepcopy(c_board)
        #virtual_game = copy.deepcopy(game)

        playable_moves = []


        for tile in c_board.board:
            t_to_flip = c_board.is_legal_move(tile.x_pos, tile.y_pos, game.active_player) 
            if t_to_flip != False :

                #strategie de jouer la premiere option disponible
                #return [tile.x_pos , tile.y_pos]

                #lister tous les coups possibles avec leurs gains potentiels
                tile_point = 0
                for item in t_to_flip:
                    tile_point += item[0]
                
                playable_moves.append([tile,tile_point])
  ########

        # Stratégie pour récupérer les bordures au 10ème tour
        if self.counter >= 7:
            border_moves = [[0, y] for y in range(8)] + [[7, y] for y in range(8)] + [[x, 0] for x in range(8)] + [[x, 7] for x in range(8)]
            for move in border_moves:
                for item in playable_moves:
                    if item[0].x_pos == move[0] and item[0].y_pos == move[1]:
                        self.counter += 1
                        return [item[0].x_pos, item[0].y_pos]        
        
          # Stratégie pour maximiser le nombre de pions retournés aux autres tours
                    
          # Ajout de la stratégie Maximize Flip
        if len(playable_moves) > 0:
            # Triez les mouvements en fonction du nombre de pions retournés de manière décroissante
            playable_moves.sort(key=lambda x: x[1], reverse=True)
            # Récupérez les coordonnées du mouvement avec le plus grand nombre de pions retournés
            best_move = playable_moves[0][0]
            self.counter += 1
            return [best_move.x_pos, best_move.y_pos]
        else:
            self.counter += 1
            return None    
        


        # Stratégie pour prendre le coin au 5ème tour
        if self.counter >= 7:
            corner_moves = [[2, 2], [5, 2], [2, 5], [5, 5]]
            for move in corner_moves:
                for item in playable_moves:
                    if item[0].x_pos == move[0] and item[0].y_pos == move[1]:
                        self.counter += 1
                        return [item[0].x_pos, item[0].y_pos]       

    
            #else:
             #   game.check_for_winner()
            
        #strategie de debut de la partie

        if self.counter <= 7:
            #privilegier le centre
            
            min_gain_centre = 50
            centre_moves = []
            min_centre_move = [playable_moves[0][0].x_pos, playable_moves[0][0].y_pos]

            for itm in playable_moves:
                if 2 <= itm[0].x_pos <= 5 and 2 <= itm[0].y_pos <= 5:
                    centre_moves.append(itm)

            if len(centre_moves) > 0:
                for itm in centre_moves:
                    if itm[1] < min_gain_centre:
                        min_gain_centre = itm[1]
                        min_centre_move = [itm[0].x_pos, itm[0].y_pos]
            
            if min_gain_centre != 50:
                self.counter += 1
                return min_centre_move            
            else:
                #on trouve le gain minimum en dehors du centre
                point_min = min([x[1] for x in playable_moves])

                #on recupere ses coordonnées
                for itm in playable_moves:
                    if itm[1] == point_min:
                        self.counter += 1
                        return [itm[0].x_pos, itm[0].y_pos]
        
        #strategie de partie avancée

        #jouer les bordures
        max_bord_gain = 0
        max_bord_move = [playable_moves[0][0].x_pos, playable_moves[0][0].y_pos]

        for itm in playable_moves:
            if itm[0].type == "X":
                if itm[1] >= max_bord_gain:
                    max_bord_gain = itm[1]      
                    max_bord_move = [itm[0].x_pos, itm[0].y_pos]
        
        #au cas ou pas de playable bordure
                    
               
        #strategie de jouer le coup qui rapporte le plus de points

        if max_bord_gain == 0:
             max_point = 0
             max_move = [playable_moves[0][0].x_pos, playable_moves[0][0].y_pos]

             for itm in playable_moves:
                         #eviter les ligne et colones avant dernieres
                 if itm[1] >= max_point and itm[0].x_pos != 1 and itm[0].x_pos != 6 and itm[0].y_pos != 1 and itm[0].x_pos != 6:
                    max_point = itm[1]
                    max_move = [itm[0].x_pos, itm[0].y_pos]
             
             if max_point == 0:
                 for itm in playable_moves:
                    #revenir au lignes avant dernieres
                    if itm[1] >= max_point:
                       max_point = itm[1]
                       max_move = [itm[0].x_pos, itm[0].y_pos]

             self.counter += 1
             return max_move
        else :
            self.counter += 1
            return max_bord_move 
   
        
# Create a new board & a new game instances
        
        #corto bot
class CrotoBotEz:
    def __init__(self):
        self.coners = [[0, 0], [7, 0], [0, 7], [7, 7]]
        self.avoided_tiles = [[1, 0], [0, 1],  [1, 1], [1, 7], [0, 6], [1, 6], [6, 0], [7, 1], [6, 1], [6, 7], [7, 6], [6, 6]]

    # BOT FUNCTIONS
    def get_total_flips(self, moves):
        # Calcule le nombre total de pions retournés pour chaque coup possible
        total_flips = []
        for move in moves:
            t_to_flip = c_board.is_legal_move(move[0].x_pos, move[0].y_pos, game.active_player)
            if t_to_flip is not False:
                total_flips.append(sum(item[0] for item in t_to_flip))
            else:
                total_flips.append(0)
        return total_flips    
    def get_distance_to_border(self, x, y):

    # Calcule la distance d'une position par rapport aux bordures
        return min(x, 7 - x, y, 7 - y)

    def check_valid_moves(self, board, game):
        max_points = -999
        best_moves = []
        current_move = []

        for current_tile in board.board:
            points = 0

            if(board.is_tile_empty):
                current_move = board.is_legal_move(current_tile.x_pos, current_tile.y_pos, game.active_player)
                
                if (current_move != False):
                    for tiles_to_flip in current_move:
                        points += tiles_to_flip[0]
                    
                    points += self.get_tile_weight(current_tile.x_pos, current_tile.y_pos)
                    if(points > max_points):
                        best_moves = [[current_tile.x_pos, current_tile.y_pos]]
                        max_points = points
                    elif(points == max_points):
                        best_moves.append([current_tile.x_pos, current_tile.y_pos])

        return random.choice(best_moves)
                
    def get_tile_weight(self, x, y):
        total_points = 0

        for current_coord in self.coners:
            if x == current_coord[0] and y == current_coord[1]:
                total_points += 100
                break
            
        for current_coord in self.avoided_tiles:
            if x == current_coord[0] and y == current_coord[1]:
                total_points -= 30
                break
        
        return total_points
            
    
      
othello_board = Board(8)
othello_game = Game() 


# Fill the board with tiles
othello_board.create_board()

# Draw the board
othello_board.draw_board("Type")

# Create 2 bots
my_bot_Françis = Bot_Françis_nganou()
otherBot = Bot_Françis_nganou()

croto_bot = CrotoBotEz()


victoires = {"⚫":0, "⚪":0}
n_matches = 0

for n_matches in range(30):
    while not othello_game.is_game_over:
        # First player / bot logic goes here
        if (othello_game.active_player == "⚫"):
            move_coordinates = my_bot_Françis.check_valid_moves(othello_board , othello_game)
            #move_coordinates = croto_bot.check_valid_moves(othello_board, othello_game)
       
           # changer ici user par bot pour jouer 
    
            othello_game.place_pawn(move_coordinates[0], move_coordinates[1], othello_board, othello_game.active_player)    

        # Second player / bot logic goes here
        else:
        
            move_coordinates = my_bot_Françis.check_valid_moves(othello_board , othello_game) 
            #move_coordinates = croto_bot.check_valid_moves(othello_board, othello_game)
            othello_game.place_pawn(
                move_coordinates[0], move_coordinates[1], othello_board, othello_game.active_player)
            #####

    n_matches += 1
    if othello_game.winner == "⚫":
        victoires["⚫"] += 1
    else:
        victoires["⚪"] += 1

    othello_board = Board(8)
    othello_game = Game()

    # Fill the board with tiles
    othello_board.create_board()

    # Draw the board
    othello_board.draw_board("Content")

print(" Nombre victoire Noire : ", victoires["⚫"])
print(" Nombre victoire Blanc : " , victoires["⚪"])
