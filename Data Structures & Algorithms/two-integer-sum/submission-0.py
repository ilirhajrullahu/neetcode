class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #[3, 4, 5, 6] , target = 7
        # [0, 1]
        num_dict = {}
        result_list = []
        for index, num in enumerate (nums):
            look_for = target - num
            if look_for in num_dict:
                result_list.append(num_dict[look_for])
                result_list.append(index)
                return result_list
            else:
                num_dict[num] = index
            

            
