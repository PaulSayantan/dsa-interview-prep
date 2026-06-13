class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        word = ''
        for w in words:
            summ = 0
            for ch in w:
                summ += weights[ord(ch) % 97]
            word += chr(122 - (summ % 26))
        return word
        
        