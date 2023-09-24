

class Solution:

    def partition(self, start, end, array):

        pivot_index = start
        pivot = array[pivot_index]

        while start < end:

            while start < len(array) and array[start] <= pivot:
                start += 1

            while array[end] > pivot:
                end -= 1

            if start < end:
                array[start], array[end] = array[end], array[start]

        array[end], array[pivot_index] = array[pivot_index], array[end]

        return end

    def quick_sort(self, start, end, arr):

        if start < end:

            p = self.partition(start, end, arr)

            self.quick_sort(start, p-1, arr)
            self.quick_sort(p+1, end, arr)

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        nums = nums1 + nums2
        self.quick_sort(0, len(nums) - 1, nums)

        if len(nums) % 2 != 0:
            return float(nums[len(nums) // 2])
        elif len(nums) % 2 == 0:
            num_1 = nums[:int(len(nums)/2)][-1]
            num_2 = nums[int(len(nums)/2):][0]
            return float((num_1 + num_2) / 2)
