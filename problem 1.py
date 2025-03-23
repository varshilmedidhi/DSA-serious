"""
Problem 1: Maximum Sum Subarray of Size K
Difficulty: Easy

Given an array of integers nums and an integer k, find the maximum sum of any contiguous subarray of size k.

Constraints:
* 1 <= k <= len(nums) <= 10^5
* -10^4 <= nums[i] <= 10^4

Example 1:
Input: nums = [1, 4, 2, 10, 2, 3, 1, 0, 20], k = 4
Output: 24
Explanation: The subarray [2, 10, 2, 3] has the maximum sum of 24

Example 2:
Input: nums = [100, 200, 300, 400], k = 2
Output: 700
Explanation: The subarray [300, 400] has the maximum sum of 700
"""
def max_sum_subarray(nums, k):
    # Your code here
    total=sum(nums[:k])
    max_total=total
    for i in range(len(nums)-k):
        total-=nums[i]
        total+=nums[i+k]
        max_total=max(max_total,total)
    return max_total

assert max_sum_subarray([1, 4, 2, 10, 2, 3, 1, 0, 20], 4) == 24
assert max_sum_subarray([100, 200, 300, 400], 2) == 700
print("all done")