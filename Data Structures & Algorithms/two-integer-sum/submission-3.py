class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = dict()
        for i in range(len(nums)):
            difference = target - nums[i]
            j = lookup.get(difference, None)
            if j is not None:
                return [j, i]
            else:
                lookup[nums[i]] = i