class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        stack, total, result = [], 0, []
        # we only use elemens to the right of nums
        def dfs(i):
            nonlocal total
            if total == target and stack not in result:
                result.append(stack[:])
            if i == len(nums) or total > target:
                return

            stack.append(nums[i])
            total += nums[i]
            dfs(i)
            total -= nums[i]
            stack.pop()
            dfs(i+1)
        dfs(0)
        return result