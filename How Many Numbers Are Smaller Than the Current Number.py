class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        Output = []
        for i in range(len(nums)):
            Output.append(sorted_nums.index(nums[i]))
        return Output
