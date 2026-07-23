CODE in Python :

class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Base cases for n < 3
        if n < 3:
            return n
        
        # For n >= 3, the number of unique XOR values is 2^(bit_length(n))
        return 1 << n.bit_length()
