class Solution:
    def minTimeToType(self, word: str) -> int:
        total, pointer = 0, 0
        for e in word:
            next_char = ord(e) - ord('a')
            path_1 = abs(pointer - next_char)
            path_2 = 26 - path_1
            total = total + min(path_1, path_2)
            pointer = next_char
        return total + len(word)