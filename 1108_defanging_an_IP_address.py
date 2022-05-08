class Solution:
    def defangIPaddr(self, address: str) -> str:
        # Faster solution
        defangedIP = ''
        for char in address:
            if char == '.':
                defangedIP += '[.]'
            else:
                defangedIP += char
        return defangedIP
        """
        # Second solution utilizing a while loop
        position = 0
        defangedIP = ''
        while position < len(address):
            if address[position] == '.':
                defangedIP += '[.]'
            else:
                defangedIP += address[position]
            position += 1
        return defangedIP
        """