class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort(reverse = True)
        res = 0
        for p in players:
            while trainers and p > trainers[-1]:
                trainers.pop()
                
            if trainers and p <= trainers[-1]:
                res += 1
                trainers.pop()
        return res