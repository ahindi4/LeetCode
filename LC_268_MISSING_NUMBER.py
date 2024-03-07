
#Solution 1

def MissingNumber(self, nums):
    
    n = len(nums)
    
    expected_sum = n * (n + 1) // 2
    
    actual_sum = sum(nums)
    
    return expected_sum - actual_sum

#Time Complexity: O(n)
#Space Complexity: O(n)
    
  #Solution 2
  
  
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        sorted_list = sorted(nums)

        if sorted_list[0] != 0:
            return 0
        
        for i in range(1, len(sorted_list)):
            difference = sorted_list[i] - sorted_list[i-1]
            if difference > 1:
                return sorted_list[i-1] + 1  

        return sorted_list[-1] + 1
    
    
#Time Complexity: O(nlog(n))
#Space Complexity: O(n)

        
            

    