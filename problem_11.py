

class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0

        first_idx = 0
        last_idx = len(height) - 1

        while first_idx < last_idx:
            area = (last_idx - first_idx) * \
                (height[first_idx] if height[first_idx] <
                 height[last_idx] else height[last_idx])
            if area > max_area:
                max_area = area

            if height[first_idx] < height[last_idx]:
                first_idx += 1

            else:
                last_idx -= 1

        return max_area
