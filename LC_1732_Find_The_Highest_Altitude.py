class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        alti = 0
        array = []

        for i in range(len(gain)):
            alti += gain[i]
            array.append(alti)

        
        if max(array) < 0:
            return 0
        else:
            return max(array)

        
#Time Complexity: O(n)
#Space Complexity: O(n)
