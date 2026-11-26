class Solution:
    def canAliceWin(self, n: int) -> bool:
        needed = 10
        alice_turn = True
        
        # Keep playing as long as there are enough stones for the current move
        while n >= needed:
            n -= needed
            needed -= 1
            alice_turn = not alice_turn  # Switch turns
            
        # If it stops on Alice's turn, she couldn't make a move (Alice loses).
        # If it stops on Bob's turn, Bob couldn't make a move (Alice wins).
        return not alice_turn