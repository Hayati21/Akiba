class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        losses = {}
        
        for winner, loser in matches:
            if winner not in losses:
                losses[winner] = 0
            if loser not in losses:
                losses[loser] = 0
            
            losses[loser] += 1
            
        zero_loss = [player for player, count in losses.items() if count == 0]
        one_loss = [player for player, count in losses.items() if count == 1]
        
        return [sorted(zero_loss), sorted(one_loss)]