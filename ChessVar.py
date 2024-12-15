# Author: Gannon Strand
# GitHub username: Gannon-Strand
# Date: 12/18/2024
# Description: Several functions & a class to represent a chess board.

class ChessVar:
    """Class that represents a chess board"""
    def __init__(self):
        """Initializes our chess variables"""
        self._game_state = "UNFINISHED"
        self._move_count = 0
        self._board = [ ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r',],
                          ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                          ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'] ]
        self._white_board = [ ['*', '*', '*', '*', '*', '*', '*', '*'],
                              ['*', '*', '*', '*', '*', '*', '*', '*'],
                              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                              ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                              ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'] ]
        self._black_board = [ ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
                              ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                              ['*', '*', '*', '*', '*', '*', '*', '*'],
                              ['*', '*', '*', '*', '*', '*', '*', '*'] ]

    def get_game_state(self):
        """Returns the game state of the chess board"""
        return self._game_state

    def get_board(self, board):
        """Returns the chess board of the given board"""
        if board == "white":
            print("[")
            for row in self._white_board:
                print(row)
            return "]"
        if board == "black":
            print("[")
            for row in self._black_board:
                print(row)
            return "]"
        if board == "audience":
            print("[")
            for row in self._board:
                print(row)
            return "]"

    def make_move(self, move_from, move_to):
        """Makes a move from a certain location on the board to a different one"""
        if len(move_from) != 2 or len(move_to) != 2:
            return False
        move_from_position = self.convert(move_from)
        move_to_position = self.convert(move_to)
        if move_from_position is False or move_to_position is False:
            return False
        legal_check = self.check_legal(move_from_position, move_to_position)
        if legal_check is False:
            return False
        if legal_check is True:
            last_check = self.check_if_piece_in_way(move_from_position, move_to_position)
            if last_check is False:
                return False
            if last_check is True or last_check is None:
                self.move_piece(move_from_position, move_to_position)
                return True

    def check_legal(self, move_from_position, move_to_position):
        """Checks if the move is legal"""
        valid = 0
        valid1 = 0
        for x in range(0,8):
            row = self._board[x]
            for item in row:
                if item == 'K':
                    valid = 1
                if item == 'k':
                    valid1 = 2
        if valid == 1 and valid1 != 2:
            self._game_state = "WHITE_WON"
        if valid != 1 and valid1 == 2:
            self._game_state = "BLACK_WON"
        if self._game_state != "UNFINISHED":
            return False
        piece = self._board[move_from_position[0]][move_from_position[1]]
        move_to_piece = self._board[move_to_position[0]][move_to_position[1]]
        if piece == " ":
            return False
        if self._move_count % 2 == 0:
            """White Move"""
            if piece.isupper() == False:
                return False
        if self._move_count % 2 != 0:
            """Black Move"""
            if piece.isupper() == True:
                return False
        if piece == "p" or piece == "P":
            """Checks if pawn move is legal"""
            if piece == "P":
                if move_from_position[1] == move_to_position[1]:
                    if move_from_position[0]-move_to_position[0] == 1 and move_to_piece == " ":
                        """Checks if white pawn moves 1 up and the space its moving to is empty"""
                        return True
                    if move_from_position[0]-move_to_position[0] == 2 and move_to_piece == " " and move_from_position[0] == 6:
                        """Checks if white pawn moves 2 up and the space its moving to is empty and its in its first turn"""
                        return True
                    else:
                        return False
                if move_from_position[0]-move_to_position[0] == 1 and move_to_piece != " " and move_to_piece.isupper() == False:
                    if move_from_position[1] - move_to_position[1] == 1 or move_from_position[1] - move_to_position[1] == -1:
                        """Checks if white pawn moves 1 up the space its moving to is not empty(and a black piece) and it moves left/right one unit"""
                        return True
                    else:
                        return False
                else:
                    return False
        if piece == "p":
            if move_from_position[1] == move_to_position[1]:
                if move_to_position[0] - move_from_position[0] == 1 and move_to_piece == " ":
                    """Checks if black pawn moves 1 up and the space its moving to is empty"""
                    return True
                if move_to_position[0] - move_from_position[0] == 2 and move_to_piece == " " and move_from_position[
                    0] == 1:
                    """Checks if black pawn moves 2 up and the space its moving to is empty and its in its first turn"""
                    return True
                else:
                    return False
            if move_to_position[0] - move_from_position[0] == 1 and move_to_piece != " " and move_to_piece.isupper() == True:
                if move_to_position[1] - move_from_position[1] == 1 or move_to_position[1] - move_from_position[1] == -1:
                    """Checks if black pawn moves 1 up the space its moving to is not empty(and a white piece) and it moves left/right one unit"""
                    return True
                else:
                    return False
            else:
                return False
        if piece == "r" or piece == "R":
            """Checks if rook move is legal"""
            if move_from_position[1] == move_to_position[1] and move_to_piece == " ":
                """Checks if rook moves up/down and the space its moving to is empty"""
                return True
            if move_from_position[0] == move_to_position[0] and move_to_piece == " ":
                """Checks if rook moves left/right and the space its moving to is empty"""
                return True
            if piece == 'r':
                if move_from_position[1] == move_to_position[1] and move_to_piece != " " and move_to_piece.isupper() == True:
                    """Checks if rook moves up/down and the space its moving to is not empty and occupied by a white piece"""
                    return True
                if move_from_position[0] == move_to_position[0] and move_to_piece != " " and move_to_piece.isupper() == True:
                    """Checks if rook moves left/right and the space its moving to is not empty and occupied by a white piece"""
                    return True
                else:
                    return False
            if piece == 'R':
                if move_from_position[1] == move_to_position[1] and move_to_piece != " " and move_to_piece.isupper() == False:
                    """Checks if rook moves up/down and the space its moving to is not empty and occupied by a black piece"""
                    return True
                if move_from_position[0] == move_to_position[0] and move_to_piece != " " and move_to_piece.isupper() == False:
                    """Checks if rook moves left/right and the space its moving to is not empty and occupied by a black piece"""
                    return True
                else:
                    return False
        if piece == "n" or piece == "N":
            """Checks if Knight move is legal"""
            if move_to_position[1]-move_from_position[1] == 1 and move_from_position[0]-move_to_position[0] == 2:
                """Checks if Knight moves up 2 left 1"""
                if move_to_piece == " ":
                    return True
                if piece == 'n' and move_to_piece.isupper() == True:
                    return True
                if piece == 'N' and move_to_piece.isupper() == False:
                    return True
                else:
                    return False
            if move_from_position[1]-move_to_position[1] == 1 and move_from_position[0]-move_to_position[0] == 2:
                """Checks if Knight moves up 2 right 1"""
                if move_to_piece == " ":
                    return True
                if piece == 'n' and move_to_piece.isupper() == True:
                    return True
                if piece == 'N' and move_to_piece.isupper() == False:
                    return True
                else:
                    return False
            if move_from_position[1]-move_to_position[1] == 2 and move_from_position[0]-move_to_position[0] == 1:
                """Checks if Knight moves up 1 left 2"""
                if move_to_piece == " ":
                    return True
                if piece == 'n' and move_to_piece.isupper() == True:
                    return True
                if piece == 'N' and move_to_piece.isupper() == False:
                    return True
                else:
                    return False
            if move_to_position[1]-move_from_position[1] == 2 and move_from_position[0]-move_to_position[0] == 1:
                """Checks if Knight moves up 1 right 2"""
                if move_to_piece == " ":
                    return True
                if piece == 'n' and move_to_piece.isupper() == True:
                    return True
                if piece == 'N' and move_to_piece.isupper() == False:
                    return True
                else:
                    return False
            if move_from_position[1]-move_to_position[1] == 2 and move_to_position[0]-move_from_position[0] == 1:
                """Checks if Knight moves down 1 left 2"""
                if move_to_piece == " ":
                    return True
                if piece == 'n' and move_to_piece.isupper() == True:
                    return True
                if piece == 'N' and move_to_piece.isupper() == False:
                    return True
                else:
                    return False
            if move_to_position[1]-move_from_position[1] == 2 and move_to_position[0]-move_from_position[0] == 1:
                """Checks if Knight moves down 1 right 2"""
                if move_to_piece == " ":
                    return True
                if piece == 'n' and move_to_piece.isupper() == True:
                    return True
                if piece == 'N' and move_to_piece.isupper() == False:
                    return True
                else:
                    return False
            if move_to_position[1]-move_from_position[1] == 1 and move_to_position[0]-move_from_position[0] == 2:
                """Checks if Knight moves down 1 right 2"""
                if move_to_piece == " ":
                    return True
                if piece == 'n' and move_to_piece.isupper() == True:
                    return True
                if piece == 'N' and move_to_piece.isupper() == False:
                    return True
                else:
                    return False
            if move_from_position[1]-move_to_position[1] == 1 and move_to_position[0]-move_from_position[0] == 2:
                """Checks if Knight moves down 1 left 2"""
                if move_to_piece == " ":
                    return True
                if piece == 'n' and move_to_piece.isupper() == True:
                    return True
                if piece == 'N' and move_to_piece.isupper() == False:
                    return True
                else:
                    return False
            else:
                return False
        if piece == "b" or piece == "B":
            """Checks if Bishop move is legal"""
            for x in range(1,8):
                if move_to_position[1] - move_from_position[1] == x and move_from_position[0] - move_to_position[0] == x:
                    """Checks if Bishop moves up and right"""
                    if move_to_piece == " ":
                        return True
                    if piece == 'b' and move_to_piece.isupper() == True:
                        return True
                    if piece == 'B' and move_to_piece.isupper() == False:
                        return True
                    else:
                        return False
                if move_from_position[1] - move_to_position[1] == x and move_to_position[0] - move_from_position[0] == x:
                    """Checks if Bishop moves down and left"""
                    if move_to_piece == " ":
                        return True
                    if piece == 'b' and move_to_piece.isupper() == True:
                        return True
                    if piece == 'B' and move_to_piece.isupper() == False:
                        return True
                    else:
                        return False
                if move_from_position[1] - move_to_position[1] == x and move_from_position[0] - move_to_position[0] == x:
                    """Checks if Bishop moves down and right"""
                    if move_to_piece == " ":
                        return True
                    if piece == 'b' and move_to_piece.isupper() == True:
                        return True
                    if piece == 'B' and move_to_piece.isupper() == False:
                        return True
                    else:
                        return False
                if move_to_position[1] - move_from_position[1] == x and move_to_position[0] - move_from_position[0] == x:
                    """Checks if Bishop moves down and right"""
                    if move_to_piece == " ":
                        return True
                    if piece == 'b' and move_to_piece.isupper() == True:
                        return True
                    if piece == 'B' and move_to_piece.isupper() == False:
                        return True
                    else:
                        return False
        if piece == "k" or piece == "K":
            """Checks if King move is legal"""
            if move_from_position[1]-move_to_position[1] == 0 and move_from_position[0]-move_to_position[0] == 1:
                """Checks if King moves up 1"""
                if move_to_piece == " ":
                    return True
                if piece == 'k' and move_to_piece.isupper() == True:
                    return True
                if piece == 'K' and move_to_piece.isupper() == False:
                    return True
                else:
                    return False
            if move_from_position[1]-move_to_position[1] == 1 and move_from_position[0]-move_to_position[0] == 1:
                """Checks if King moves up 1 left 1"""
                if move_to_piece == " ":
                    return True
                if piece == 'k' and move_to_piece.isupper() == True:
                    return True
                if piece == 'K' and move_to_piece.isupper() == False:
                    return True
                else:
                    return False
            if move_from_position[1]-move_to_position[1] == 1 and move_from_position[0]-move_to_position[0] == 0:
                """Checks if King moves left 1"""
                if move_to_piece == " ":
                    return True
                if piece == 'k' and move_to_piece.isupper() == True:
                    return True
                if piece == 'K' and move_to_piece.isupper() == False:
                    return True
                else:
                    return False
            if move_from_position[1]-move_to_position[1] == 1 and move_to_position[0]-move_from_position[0] == 1:
                """Checks if King moves down 1 left 1"""
                if move_to_piece == " ":
                    return True
                if piece == 'k' and move_to_piece.isupper() == True:
                    return True
                if piece == 'K' and move_to_piece.isupper() == False:
                    return True
                else:
                    return False
            if move_from_position[1]-move_to_position[1] == 0 and move_to_position[0]-move_from_position[0] == 1:
                """Checks if King moves down 1"""
                if move_to_piece == " ":
                    return True
                if piece == 'k' and move_to_piece.isupper() == True:
                    return True
                if piece == 'K' and move_to_piece.isupper() == False:
                    return True
                else:
                    return False
            if move_to_position[1]-move_from_position[1] == 1 and move_to_position[0]-move_from_position[0] == 1:
                """Checks if King moves down 1 right 1"""
                if move_to_piece == " ":
                    return True
                if piece == 'k' and move_to_piece.isupper() == True:
                    return True
                if piece == 'K' and move_to_piece.isupper() == False:
                    return True
                else:
                    return False
            if move_to_position[1]-move_from_position[1] == 1 and move_to_position[0]-move_from_position[0] == 0:
                """Checks if King moves right 1"""
                if move_to_piece == " ":
                    return True
                if piece == 'k' and move_to_piece.isupper() == True:
                    return True
                if piece == 'K' and move_to_piece.isupper() == False:
                    return True
                else:
                    return False
            if move_to_position[1]-move_from_position[1] == 1 and move_from_position[0]-move_to_position[0] == 1:
                """Checks if King moves up 1 right 1"""
                if move_to_piece == " ":
                    return True
                if piece == 'k' and move_to_piece.isupper() == True:
                    return True
                if piece == 'K' and move_to_piece.isupper() == False:
                    return True
                else:
                    return False
            else:
                return False
        if piece == "q" or piece == "Q":
            """Checks if Queen move is legal"""
            for x in range(1,8):
                if move_to_position[1] - move_from_position[1] == x and move_from_position[0] - move_to_position[0] == x:
                    """Checks if Queen moves up and right"""
                    if move_to_piece == " ":
                        return True
                    if piece == 'q' and move_to_piece.isupper() == True:
                        return True
                    if piece == 'Q' and move_to_piece.isupper() == False:
                        return True
                    else:
                        return False
                if move_from_position[1] - move_to_position[1] == x and move_to_position[0] - move_from_position[0] == x:
                    """Checks if Queen moves down and left"""
                    if move_to_piece == " ":
                        return True
                    if piece == 'q' and move_to_piece.isupper() == True:
                        return True
                    if piece == 'Q' and move_to_piece.isupper() == False:
                        return True
                    else:
                        return False
                if move_from_position[1] - move_to_position[1] == x and move_from_position[0] - move_to_position[0] == x:
                    """Checks if Queen moves up and right"""
                    if move_to_piece == " ":
                        return True
                    if piece == 'q' and move_to_piece.isupper() == True:
                        return True
                    if piece == 'Q' and move_to_piece.isupper() == False:
                        return True
                    else:
                        return False
                if move_to_position[1] - move_from_position[1] == x and move_to_position[0] - move_from_position[0] == x:
                    """Checks if Queen moves down and right"""
                    if move_to_piece == " ":
                        return True
                    if piece == 'q' and move_to_piece.isupper() == True:
                        return True
                    if piece == 'Q' and move_to_piece.isupper() == False:
                        return True
                    else:
                        return False
            if move_from_position[1] == move_to_position[1] and move_to_piece == " ":
                """Checks if Queen moves up/down and the space its moving to is empty"""
                return True
            if move_from_position[0] == move_to_position[0] and move_to_piece == " ":
                """Checks if Queen moves left/right and the space its moving to is empty"""
                return True
            if piece == 'q':
                if move_from_position[1] == move_to_position[1] and move_to_piece != " " and move_to_piece.isupper() == True:
                    """Checks if Queen moves up/down and the space its moving to is not empty and occupied by a white piece"""
                    return True
                if move_from_position[0] == move_to_position[0] and move_to_piece != " " and move_to_piece.isupper() == True:
                    """Checks if Queen moves left/right and the space its moving to is not empty and occupied by a white piece"""
                    return True
            if piece == 'Q':
                if move_from_position[1] == move_to_position[1] and move_to_piece != " " and move_to_piece.isupper() == False:
                    """Checks if Queen moves up/down and the space its moving to is not empty and occupied by a black piece"""
                    return True
                if move_from_position[0] == move_to_position[0] and move_to_piece != " " and move_to_piece.isupper() == False:
                    """Checks if Queen moves left/right and the space its moving to is not empty and occupied by a black piece"""
                    return True
            return False

    def check_if_piece_in_way(self, move_from_position, move_to_position):
        """Checks if any piece is in the way for a move"""
        piece = self._board[move_from_position[0]][move_from_position[1]]
        move_to_piece = self._board[move_to_position[0]][move_to_position[1]]
        board = self._board
        test_list = []
        if piece == 'r' or piece == 'R' or piece == 'q' or piece == 'Q':
            """Scans the row to ensure it can't go past a piece"""
            count = 0
            if move_from_position[1] == move_to_position[1]:
                """Deals with up/down"""
                test = 0
                length = move_from_position[0] - move_to_position[0]
                if length < 0:
                    length = move_to_position[0] - move_from_position[0]
                    test = 1
                if length == 1:
                    return True
                for x in range(length):
                    if test == 1:
                        test2 = move_to_position[0]
                        test2 = test2 - x
                        test_point_to_position = test2, move_from_position[1]
                        if test_point_to_position != move_from_position:
                            check = self.check_legal(move_from_position, test_point_to_position)
                            if test_point_to_position != move_from_position:
                                if check == True:
                                    count += 1
                                    second_check = self._board[test_point_to_position[0]][test_point_to_position[1]]
                                    test_list.append(second_check)
                                if check == False:
                                    return False
                    if test == 0:
                        test2 = move_from_position[0]
                        test2 = test2 - x
                        test_point_to_position = test2, move_from_position[1]
                        if test_point_to_position != move_from_position:
                            check = self.check_legal(move_from_position, test_point_to_position)
                            if test_point_to_position != move_from_position:
                                if check == True:
                                    count += 1
                                    second_check = self._board[test_point_to_position[0]][test_point_to_position[1]]
                                    test_list.append(second_check)
                                if check == False:
                                    return False
            if move_from_position[0] == move_to_position[0]:
                """Deals with left/right"""
                test = 0
                length = move_from_position[1] - move_to_position[1]
                if length < 0:
                    length = move_to_position[1] - move_from_position[1]
                    test = 1
                for x in range(length-1):
                    if test == 1:
                        test2 = move_from_position[1]
                        test2 = test2 + x + 1
                        test_point_to_position = move_from_position[0], test2
                        check = self.check_legal(move_from_position, test_point_to_position)
                        if test_point_to_position != move_from_position:
                            if check == True:
                                count += 1
                                second_check = self._board[test_point_to_position[0]][test_point_to_position[1]]
                                test_list.append(second_check)
                            if check == False:
                                return False
                    if test == 0:
                        test2 = move_to_position[1]
                        test2 = test2 + x + 1
                        test_point_to_position = move_from_position[0], test2
                        check = self.check_legal(move_from_position, test_point_to_position)
                        if test_point_to_position != move_from_position:
                            if check == True:
                                count += 1
                                second_check = self._board[test_point_to_position[0]][test_point_to_position[1]]
                                test_list.append(second_check)
                            if check == False:
                                return False
            list_count = 0
            for item in test_list:
                if item != " ":
                    if item.isupper() == True or item.isupper() == False:
                        list_count += 1
            if list_count > 1:
                return False
            if count > 0:
                return True
        if piece == 'b' or piece == 'B' or piece == 'q' or piece == 'Q':
            """Scans the row to ensure it can't go past a piece'"""
            length1 = move_from_position[1] - move_to_position[1]
            length2 = move_from_position[0] - move_to_position[0]
            test = 0
            if length1 < 0:
                length1 = move_to_position[1] - move_from_position[1]
                test = 1
            if length2 < 0:
                length2 = move_to_position[0] - move_from_position[0]
                test = 2
            for x in range(length1):
                if test == 1:
                    """Right"""
                    test2 = move_from_position[1]
                    test2 = test2 + x
                    test3 = move_from_position[0]
                    test3 = test3 - x
                    test_point_to_position = test3, test2
                    if test_point_to_position != move_from_position:
                        check = self.check_legal(move_from_position, test_point_to_position)
                        if check == False:
                            return False
                        if check == True:
                            test = 3
                if test == 0:
                    """Left"""
                    test2 = move_from_position[1]
                    test2 = test2 - x
                    test3 = move_from_position[0]
                    test3 = test3 - x
                    test_point_to_position = test3, test2
                    if test_point_to_position != move_from_position:
                        check = self.check_legal(move_from_position, test_point_to_position)
                        if check == False:
                            return False
                        if check == True:
                            test = 3
                if test == 2:
                    """Left"""
                    test2 = move_from_position[1]
                    test2 = test2 - x
                    test3 = move_from_position[0]
                    test3 = test3 + x
                    test_point_to_position = test3, test2
                    if test_point_to_position != move_from_position:
                        check = self.check_legal(move_from_position, test_point_to_position)
                        if check == False:
                            return False
                        if check == True:
                            test = 3
            if test == 3:
                return True
        else:
            return True

    def move_piece(self, move_from_position, move_to_position):
        """Moves the piece"""
        piece = self._board[move_from_position[0]][move_from_position[1]]
        move_to_piece = self._board[move_to_position[0]][move_to_position[1]]
        self._board[move_to_position[0]][move_to_position[1]] = piece
        self._board[move_from_position[0]][move_from_position[1]] = " "
        if self._move_count % 2 == 0:
            """White Board"""
            piece = self._white_board[move_from_position[0]][move_from_position[1]]
            move_to_piece = self._white_board[move_to_position[0]][move_to_position[1]]
            self._white_board[move_to_position[0]][move_to_position[1]] = piece
            self._white_board[move_from_position[0]][move_from_position[1]] = " "
            piece2 = self._black_board[move_from_position[0]][move_from_position[1]]
            move_to_piece2 = self._black_board[move_to_position[0]][move_to_position[1]]
            self._black_board[move_to_position[0]][move_to_position[1]] = piece2
            self._black_board[move_from_position[0]][move_from_position[1]] = " "
            for x in range(0,8):
                row = self._board[x]
                for y in range(len(row)):
                    item = self._board[x][y]
                    if item != " ":
                        if item.isupper() == False:
                            point = x,y
                            check = self.check_legal(move_to_position, point)
                            if check == True:
                                self._white_board[point[0]][point[1]] = item
                                self._black_board[move_to_position[0]][move_to_position[1]] = piece
        if self._move_count % 2 != 0:
            """Black Board"""
            piece = self._black_board[move_from_position[0]][move_from_position[1]]
            move_to_piece = self._black_board[move_to_position[0]][move_to_position[1]]
            self._black_board[move_to_position[0]][move_to_position[1]] = piece
            self._black_board[move_from_position[0]][move_from_position[1]] = " "
            piece2 = self._white_board[move_from_position[0]][move_from_position[1]]
            move_to_piece2 = self._white_board[move_to_position[0]][move_to_position[1]]
            self._white_board[move_to_position[0]][move_to_position[1]] = piece2
            self._white_board[move_from_position[0]][move_from_position[1]] = " "
            for x in range(0, 8):
                row = self._board[x]
                for y in range(len(row)):
                    item = self._board[x][y]
                    if item != " ":
                        if item.isupper() == True:
                            point = x, y
                            check = self.check_legal(move_to_position, point)
                            if check == True:
                                self._black_board[point[0]][point[1]] = item
                                self._white_board[move_to_position[0]][move_to_position[1]] = piece
        self._move_count = self._move_count + 1

    def convert(self, move):
        """Converts the move_from and move_to into a tuple"""
        dictionary_files = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
        file = dictionary_files[move[0]]
        rank = 8 - int(move[1])
        if rank > 8 or rank < 0:
            return False
        return rank, file
