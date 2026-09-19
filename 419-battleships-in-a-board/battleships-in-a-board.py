class Solution:
    def countBattleships(self, board):
        count = 0

        for i in range(len(board)):
            for j in range(len(board[0])):
                
                if board[i][j] == 'X':
                    
                    # If X is connected from above, not a new ship
                    if i > 0 and board[i - 1][j] == 'X':
                        continue
                    
                    # If X is connected from left, not a new ship
                    if j > 0 and board[i][j - 1] == 'X':
                        continue
                    
                    # This is the starting cell of a battleship
                    count += 1

        return count