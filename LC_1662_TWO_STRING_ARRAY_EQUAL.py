class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:

        if word1 and word2 is None:
            return False

        completeW1 = ""
        completeW2 = ""

        for chr in word1:
            completeW1 += chr

        for chr in word2:
            completeW2 += chr 


        if completeW1 == completeW2:
            return True

        else:
            return False