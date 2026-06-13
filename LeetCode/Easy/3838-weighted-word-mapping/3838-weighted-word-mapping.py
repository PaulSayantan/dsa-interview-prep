class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        # We use a list to store the resulting characters. 
        # Appending to a list and joining at the end is more efficient 
        # than doing string concatenation (+=) inside a loop.
        result = ''
        
        # Iterate through each word in the input list
        for w in words:
            
            # 1. Calculate the total weight of the current word.
            # We use a generator expression inside sum() for efficiency.
            # ord(ch) - ord('a') maps 'a'->0, 'b'->1 ... 'z'->25 to index the weights array.
            word_sum = sum(weights[ord(ch) - ord('a')] for ch in w)
            
            # 2. Determine the mapped character.
            # Modulo 26 keeps the shift within the bounds of the alphabet.
            # We map backward from 'z' (ASCII 122).
            # Subtracting the shift gives us the correct ASCII integer, 
            # and chr() converts it back to a string character.
            mapped_char = chr(122 - word_sum % 26)
            
            
            result += (mapped_char)

        return result