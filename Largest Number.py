class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        for i in range(n - 1):
            largest = i
            for j in range(i + 1, n):
                num1 = str(nums[largest]) + str(nums[j])
                num2 = str(nums[j]) + str(nums[largest])
                if num1 < num2:
                    largest = j
            if i != largest:
                nums[i], nums[largest] = nums[largest], nums[i]
        Output = "".join(map(str, nums))
        return str(int(Output))
