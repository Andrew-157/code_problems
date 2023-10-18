

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        result = set()

        nums.sort()

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                triplet_sum = nums[i] + nums[j] + nums[k]
                if triplet_sum == 0:
                    result.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif triplet_sum < 0:
                    j += 1
                else:
                    k -= 1
        return list(result)


sol = Solution()
print(sol.threeSum(nums=[-1, 0, 1, 2, -1, -4]))
print(sol.threeSum(nums=[0, 1, 1]))
print(sol.threeSum(nums=[0, 0, 0]))
print(sol.threeSum([0, 0, 0, 0]))
print(sol.threeSum([-2, 0, 1, 1, 2]))
