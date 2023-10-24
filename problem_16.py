from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()

        diffs = {}

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                triplet_sum = nums[i] + nums[j] + nums[k]

                diff = abs(target - triplet_sum)
                diffs[diff] = triplet_sum

                if triplet_sum < target:
                    j += 1

                else:
                    k -= 1

        return diffs[min(diffs.keys())]


sol = Solution()
print(sol.threeSumClosest(nums=[-1, 2, 1, -4], target=1))
print(sol.threeSumClosest(nums=[0, 0, 0], target=1))
print(sol.threeSumClosest(nums=[4, 0, 5, -5, 3, 3, 0, -4, -5], target=-2))
