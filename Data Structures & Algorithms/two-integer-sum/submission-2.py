class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = dict()
        for i in range(len(nums)):
            difference = target - nums[i]
            j = h.get(difference, None)
            if j is not None:
                return [j, i]
            else:
                h[nums[i]] = i