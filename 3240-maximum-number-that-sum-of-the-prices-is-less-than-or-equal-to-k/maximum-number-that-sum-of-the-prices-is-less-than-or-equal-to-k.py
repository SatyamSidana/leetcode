class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def isvalid(num):
            left_most_bit = int(log(num, 2) + 1)
            num += 1
            result = 0
            
            for i in range(x, left_most_bit+1, x):
                block_size = 2 ** i
                number_of_full_block = num // block_size
                full_blocks_ones = number_of_full_block * (block_size // 2)
                rest_ones = max(0, (num % block_size) - (block_size // 2))
                result += full_blocks_ones + rest_ones
            return result<=k
        l=1
        h=1e15
        ans=0
        while l<=h:
            mid=int((l+h)//2)
            if (isvalid(mid)==True):
                ans=mid
                l=mid+1
            else:
                h=mid-1
        return ans



