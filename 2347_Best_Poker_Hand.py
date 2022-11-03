class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        colors = set(suits)
        if len(colors) == 1: #check if 5 of same suit first
            return "Flush"
        values = Counter(ranks)
        if max(values.values()) >= 3:
            return "Three of a Kind"
        if max(values.values()) == 2:
            return "Pair"
        else:
            return "High Card"