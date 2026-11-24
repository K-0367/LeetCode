import math
from typing import List

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 1
        
        # Calculate the LCM of the entire array to set an upper bound for pruning
        total_lcm = 1
        for num in nums:
            total_lcm = math.lcm(total_lcm, num)
            
        for i in range(n):
            curr_prod = nums[i]
            curr_gcd = nums[i]
            curr_lcm = nums[i]
            
            for j in range(i + 1, n):
                curr_prod *= nums[j]
                curr_gcd = math.gcd(curr_gcd, nums[j])
                curr_lcm = math.lcm(curr_lcm, nums[j])
                
                if curr_prod == curr_lcm * curr_gcd:
                    max_len = max(max_len, j - i + 1)
                
                # Pruning: if product exceeds the maximum possible LCM * max(nums),
                # it can never match again as we multiply more positive integers.
                if curr_prod > total_lcm * curr_gcd:
                    break
                    
        return max_len
