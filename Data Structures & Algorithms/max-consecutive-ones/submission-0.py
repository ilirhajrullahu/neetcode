class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_counter = 0
        maximum_counter = 0
        for i in range(0, len(nums)):
            if nums[i] == 1:
                current_counter += 1
                if current_counter >= maximum_counter:
                    maximum_counter = current_counter
            else:
                current_counter = 0
        return maximum_counter            