class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # count the offending strings, set is faster for lookups since
        # it operates like a hash table
        count, seen = 0, set(allowed)
        for word in words:
            for char in word:
                if char not in seen:
                    count += 1
                    break
        return len(words)-count