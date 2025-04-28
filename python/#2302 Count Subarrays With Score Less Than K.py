class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        cnt = 0
        total = 0
        left = 0

        for right in range(len(nums)):
            total += nums[right]

            while total * (right - left + 1) >= k:
                total -= nums[left]
                left += 1

            cnt += (right - left + 1)

        return cnt

