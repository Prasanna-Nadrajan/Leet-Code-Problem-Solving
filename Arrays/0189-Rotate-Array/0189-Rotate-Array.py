class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l = len(nums)
        k %= l
        nums[:] = nums[-k:] + nums[:-k]
