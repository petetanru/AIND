"""This file contains all the classes you must complete for this project.

You can use the test cases in agent_test.py to help during development, and
augment the test suite with your own test cases to further test your code.

You must test your agent's strength against a set of agents with known
relative strength using tournament.py and include the results in your report.
"""
import random

infinity = float('inf')

class Timeout(Exception):
    """Subclass base exception for code clarity."""
    pass


def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    ##### distance
    opponent = game.get_opponent(player)
    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(opponent))

    ####### opening heuristics ######
    #
    # capture center
    def center(game, player):
        if game.get_player_location(player) == (2, 2): return 999 + diff + dist
        else: return diff + dist
    #
    # # inflection strat for P1
    # def inflection(game, player):
    #     opp_recent_move = game.get_player_location(game.get_opponent(player))
    #     a, b = opp_recent_move
    #     if game.get_player_location(player) == (b, a): return infinity
    #     else: return diff
    #
    # # P2 avoiding inflection point
    # def secondp_opening(game):
    #     if game.get_player_location(player) in game.get_player_location(opponent): return 0
    #     else: return diff
    #
    # First / Second move to capture center
    if game.move_count == 0 or game.move_count == 1: return center(game, player)
    #
    # # Opening moves (up to 3 turns)
    # if game.move_count % 2 == 0 and game.move_count < 5: return inflection(game,player)
    # if game.move_count % 2 == 1 and game.move_count < 6: return secondp_opening(game)

    ######### 3 improved + distance #######
    row, col = game.get_player_location(player)
    dist_row = abs(2 - row)
    dist_y = abs(2 - col)
    dist = (dist_row + dist_y)/8

    ######## overlaps #######

    diff = float(own_moves - opp_moves)

    return diff + dist


class CustomPlayer:
    """Game-playing agent that chooses a move using your evaluation function
    and a depth-limited minimax algorithm with alpha-beta pruning. You must
    finish and test this player to make sure it properly uses minimax and
    alpha-beta to return a good move before the search time limit expires.

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    iterative : boolean (optional)
        Flag indicating whether to perform fixed-depth search (False) or
        iterative deepening search (True).

    method : {'minimax', 'alphabeta'} (optional)
        The name of the search method to use in get_move().

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """

    def __init__(self, search_depth=3, score_fn=custom_score,
                 iterative=True, method='minimax', timeout=10.):
        self.search_depth = search_depth
        self.iterative = iterative
        self.score = score_fn
        self.method = method
        self.time_left = None
        self.TIMER_THRESHOLD = timeout

    def get_move(self, game, legal_moves, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        This function must perform iterative deepening if self.iterative=True,
        and it must use the search method (minimax or alphabeta) corresponding
        to the self.method value.

        **********************************************************************
        NOTE: If time_left < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        legal_moves : list<(int, int)>
            A list containing legal moves. Moves are encoded as tuples of pairs
            of ints defining the next (row, col) for the agent to occupy.

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """

        self.time_left = time_left
        def time_out_test(self):
            if self.time_left() < self.TIMER_THRESHOLD:
                raise Timeout()


        # TODO: finish this function!

        # Perform any required initializations, including selecting an initial
        # move from the game board (i.e., an opening book), or returning
        # immediately if there are no legal moves


            # The search method call (alpha beta or minimax) should happen in
            # here in order to avoid timeout. The try/except block will
            # automatically catch the exception raised by the search method
            # when the timer gets close to expiring
        # best_move = (-1, -1)
        #
        # if not game.get_legal_moves():
        #     return best_move
        #
        # if self.method == 'alphabeta':
        #     search = self.alphabeta
        # else:
        #     search = self.minimax
        #
        # try:
        #     if self.iterative is True:
        #         d = 1
        #         while True:
        #             score, best_move = search(game, d)
        #             d += 1
        #             time_out_test(self)
        #     else:
        #         score, best_move = search(game, self.search_depth)
        #
        # except Timeout:
        #     pass
        #
        # return best_move

        try:
            # The search method call (alpha beta or minimax) should happen in
            # here in order to avoid timeout. The try/except block will
            # automatically catch the exception raised by the search method
            # when the timer gets close to expiring
            best_move = None

            if not legal_moves:
                return -1, -1

            elif self.method == 'minimax' and self.iterative is True:
                self.search_depth = 999
                for d in range(self.search_depth):
                    time_out_test(self)
                    score, best_move = self.minimax(game, d+1)
                return best_move

            elif self.method == 'minimax' and self.iterative is False:
                score, best_move = self.minimax(game, self.search_depth)
                return best_move

            elif self.method =='alphabeta' and self.iterative is True:
                self.search_depth = 999
                for d in range(self.search_depth):
                    time_out_test(self)
                    score, best_move = self.alphabeta(game, d + 1) # Same as 105
                return best_move

            elif self.method == 'alphabeta' and self.iterative is False:
                score, best_move = self.alphabeta(game, self.search_depth)
                return best_move

        except Timeout:
            return best_move

        # Return the best move from the last completed search iteration


    def minimax(self, game, depth=3, maximizing_player=True):
        """Implement the minimax search algorithm as described in the lectures.

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        maximizing_player : bool
            Flag indicating whether the current search depth corresponds to a
            maximizing layer (True) or a minimizing layer (False)

        Returns
        -------
        float
            The score for the current search branch

        tuple(int, int)
            The best move for the current branch; (-1, -1) for no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project unit tests; you cannot call any other
                evaluation function directly.
        """
        def time_out_test(self):
            if self.time_left() < self.TIMER_THRESHOLD:
                raise Timeout()

        # recursive min max function
        def max_value(state, d_count):

            # test if leaf, if terminal, if depth cutoff, if timeout
            d_count -= 1
            if terminal_test(state): return state.utility(self)
            if cutoff_test(d_count): return self.score(state, self)
            time_out_test(self)
            v = -infinity
            for a in state.get_legal_moves():
                next_move = state.forecast_move(a)
                v = max(v, min_value(next_move, d_count))
            return v

        def min_value(state, d_count):
            d_count -= 1
            if terminal_test(state): return state.utility(self)
            if cutoff_test(d_count): return self.score(state, self)
            time_out_test(self)
            v = infinity
            for a in state.get_legal_moves():
                next_move = state.forecast_move(a)
                v = min(v, max_value(next_move, d_count))
            return v

        # utilities fn
        def terminal_test(state):   return state.is_loser(self) or state.is_winner(self)
        def cutoff_test(d_count):   return d_count <= 0

        # execution body, fixed depth, minimax
        best_action = None
        best_score = -infinity

        for a in game.get_legal_moves():
            next_move = game.forecast_move(a)

            if maximizing_player is True:
                v = min_value(next_move, depth)
                if v > best_score:
                    best_score = v
                    best_action = a

            else:
                best_score = infinity
                v = max_value(next_move, depth)
                if v < best_score:
                    best_score = v
                    best_action = a

        return best_score, best_action


    def alphabeta(self, game, depth=3, alpha=float("-inf"), beta=float("inf"), maximizing_player=True):
        """Implement minimax search with alpha-beta pruning as described in the
        lectures.

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        maximizing_player : bool
            Flag indicating whether the current search depth corresponds to a
            maximizing layer (True) or a minimizing layer (False)

        Returns
        -------
        float
            The score for the current search branch

        tuple(int, int)
            The best move for the current branch; (-1, -1) for no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project unit tests; you cannot call any other
                evaluation function directly.
        """
        def time_out_test(self):
            if self.time_left() < self.TIMER_THRESHOLD:
                raise Timeout()

        # recursive min max function
        def max_value(state, d_count, alpha, beta):

            # test if leaf, if terminal, if depth cutoff, if timeout
            d_count -= 1
            if terminal_test(state): return state.utility(self)
            if cutoff_test(d_count): return self.score(state, self)
            time_out_test(self)

            # init v, and iterates over branches
            v = -infinity
            for a in state.get_legal_moves():
                next_move = state.forecast_move(a)
                v = max(v, min_value(next_move, d_count, alpha, beta))
                if v >= beta: return v
                alpha = max(alpha, v)
            return v

        def min_value(state, d_count, alpha, beta):
            d_count -= 1
            if terminal_test(state): return state.utility(self)
            if cutoff_test(d_count): return self.score(state, self)
            time_out_test(self)
            v = infinity
            for a in state.get_legal_moves():
                next_move = state.forecast_move(a)
                v = min(v, max_value(next_move, d_count, alpha, beta))
                if v <= alpha: return v
                beta = min(beta, v)
            return v

        # utilities fn
        def terminal_test(state):   return state.is_loser(self) or state.is_winner(self)
        def cutoff_test(d_count):   return d_count <= 0

        # execution body, fixed depth
        best_action = None
        best_score = alpha

        for a in game.get_legal_moves():
            next_move = game.forecast_move(a)

            if maximizing_player is True:
                v = min_value(next_move, depth, best_score, beta)
                if v > best_score:
                    best_score = v
                    best_action = a

            else:
                v = max_value(next_move, depth, best_score, beta)
                if v < best_score:
                    best_score = v
                    best_action = a

        return best_score, best_action
