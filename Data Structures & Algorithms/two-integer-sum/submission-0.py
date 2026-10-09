class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap={}
        for idx, value in enumerate(nums):
            diff=target-value
            if diff in prevMap:
                return [prevMap[diff], idx]
            prevMap[value]=idx
