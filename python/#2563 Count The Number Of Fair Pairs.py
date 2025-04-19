class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # Function to count number of pairs, less than an integer `s`
        def count_pairs_less_than(nums: List[int], s: int) -> int:
            cnt = 0
            left, right = 0, len(nums)-1
            while left < right:
                # If the sum is less greater than or equal to `s`, decrease the right pointer
                if nums[left] + nums[right] >= s:
                    right -= 1
                else:
                    # Else, increment count and the left pointer
                    cnt += abs(right - left)
                    left += 1

            return cnt # Return the number of pairs


        nums = list(sorted(nums)) 
        return (count_pairs_less_than(nums, upper + 1) - count_pairs_less_than(nums, lower))

