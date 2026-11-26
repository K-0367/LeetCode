class Solution:
    def canAliceWin(self, n: int) -> bool:
        stones_to_remove = 10
        is_alice_turn = True

        while n >= stones_to_remove and stones_to_remove > 0:
            n -= stones_to_remove
            stones_to_remove -= 1
            is_alice_turn = not is_alice_turn

        return not is_alice_turn
