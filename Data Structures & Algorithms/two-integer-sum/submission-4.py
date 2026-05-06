class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = dict()
        for i, num in enumerate(nums):
            difference = target - num
            j = lookup.get(difference, None)
            if j is not None:
                return [j, i]
            else:
                lookup[num] = i