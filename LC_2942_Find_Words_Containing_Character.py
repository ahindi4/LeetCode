class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:

        ans = []

        for i, word in enumerate(words):
            for l in word:
                if l == x:
                    ans.append(i)
                    break
        return ans
            
        