class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = 'AaEeIiOoUu'
        len_s = len(s)
        final = [i for i in s[:len_s//2] if i in vowels]
        final_2 = [i for i in s[len_s//2:] if i in vowels]
        if len(final) != len(final_2):
            return False
        return True