class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        count = 0
        #         3   5
        #           4
        # [-1 0 2 4 6 8]
        while low <= high:
            pivot = low + (high - low) // 2
            print(low, pivot, high)
            if nums[pivot] > target:
                high = pivot - 1
            elif nums[pivot] < target:
                low = pivot + 1
            else:
                return pivot
        return -1