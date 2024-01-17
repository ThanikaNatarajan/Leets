class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = len(word1)
        j = len(word2)
        a = 0
        b = 0
        ch = ""
        while a < i and b < j:
            ch = ch + word1[a]
            a += 1
            ch = ch + word2[b]
            b += 1
        ch = ch + word1[a:] + word2[b:]
        return ch
