class Solution:
    def judgeCircle(self, moves: str) -> bool:
        d = Counter(moves)
        if d['L'] == d['R'] and d['U'] == d['D']:
            return True
        return False