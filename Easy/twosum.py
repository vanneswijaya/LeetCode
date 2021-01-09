class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        a = 1
        b = 0
        sol = []
        for x in nums:
            for y in range(a,len(nums)):
                res = x+nums[y]
                if res == target:
                    sol.append(b)
                    sol.append(y)
            a+=1
            b+=1
            if a==len(nums):
                break
        return sol