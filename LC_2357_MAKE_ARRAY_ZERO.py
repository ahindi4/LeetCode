class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        if nums is None:
            return 0

        unique_list = set()

        for num in nums:
            if num > 0 and num not in unique_list:
                unique_list.add(num)

        return len(unique_list)

