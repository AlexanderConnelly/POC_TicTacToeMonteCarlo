"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided


# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 25         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    
# Add your functions here.
def mc_trial(board, player):
    """
    this function will play thru a game given the 
    input board
    """
    #CHeck to see if board is complete:
    while board.check_win() == None:
        #grab list of possible moves
        p_moves = board.get_empty_squares()
        #randomly select next move from list
        next_move = p_moves[random.randrange(0,len(p_moves))]
        # run in game
        board.move(next_move[0],next_move[1],player)
        # switch player
        player = provided.switch_player(player)
        #print board.clone()
            
    print board.clone()
    
def mc_update_scores(scores, board, player):
    """
    This function will update a grid of scores 
    for each outcome of mc_trial
    """
    # get dim
    dim = board.get_dim()
    # See who won the board
    #if player x won, add score current to playerx locations
    outcome = board.check_win()
    print outcome
    if outcome == provided.PLAYERX:
        # add SCORE_CURRENT where ITS PLAYERX
        for dummy_row in range(dim):
            for dummy_col in range(dim):
                if board.square(dummy_row,dummy_col) == provided.PLAYERX:
                    scores[dummy_row][dummy_col] += SCORE_CURRENT
                if board.square(dummy_row,dummy_col) == provided.PLAYERO:
                    scores[dummy_row][dummy_col] -= SCORE_OTHER
                    
        # subtract SCORE_OTHER where its PLAYERO 
    if outcome == provided.PLAYERO:
        # add SCORE_CURRENT where ITS PLAYERX
        for dummy_row in range(dim):
            for dummy_col in range(dim):
                if board.square(dummy_row,dummy_col) == provided.PLAYERX:
                    scores[dummy_row][dummy_col] -= SCORE_CURRENT
                if board.square(dummy_row,dummy_col) == provided.PLAYERO:
                    scores[dummy_row][dummy_col] += SCORE_OTHER
    
    
def get_best_move(board, scores):
    """
    This function will evaluate the scores tallied
    from each trial, and then choose the best option
    as the nest best move
    """
    #find largest value in grid and then return it as the
    #best answer
    largest_value = -9999
    best_move = (0,0)
    
    for dummy_row in range(board.get_dim()):
        for dummy_col in range(board.get_dim()):
            if scores[dummy_row][dummy_col] > largest_value and board.square(dummy_row,dummy_col) == provided.EMPTY:
                largest_value = scores[dummy_row][dummy_col]
                best_move =(dummy_row,dummy_col)
    return best_move
    
    
    
def mc_move(board, player, trials):
    """ 
    this function will run the current board thru
    a monty carlo simulation, evaluating randomly
    the possible outcomes that can be followed out in a game,
    scoring each outcome, and then choosing the best result
    """
    # create score board:
    scores = [[0 for dummy_rows in range(board.get_dim())] for dummy_cols in range(board.get_dim())]
    
    
    # take in present board, player, and trials
    
    for _ in range(trials):
        #create seperate board to run trials on 
        trial_board = board.clone()
        mc_trial(trial_board,player)
        mc_update_scores(scores,trial_board,player)
    #pick best move and return it
    
    return get_best_move(board,scores)

    
    
    



    
# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.



#provided.play_game(mc_move, NTRIALS, False)        
#poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
