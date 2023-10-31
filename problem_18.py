from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = set()

        diffs_indexes = {}

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                triplet_sum = nums[i] + nums[j] + nums[k]
                diff = target - triplet_sum
                if diff in nums:
                    diffs_indexes[diff] = [i, j, k]
                j += 1
                k -= 1


sol = Solution()
print(sol.fourSum(nums=[1, 0, -1, 0, -2, 2], target=0))
