class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:

        completeW1 = ""
        for i in range(len(word1)):
            completeW1 += word1[i]

        completeW2 = ""
        for i in range(len(word2)):
            completeW2 += word2[i]

        if completeW1 == completeW2:
            return True

        return False
    
#This is a brute force solution and does not use any sort of a Data strcuture or algrothim!
#Time Complexity: O(n)
#Space Complexity: O(n)



        