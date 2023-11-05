class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        res, left, windowSum, windowLength = [-1] * len(nums), 0, 0, 2 * k + 1
        
        for right in range(len(nums)):
            windowSum += nums[right]  # Add the current element to the window sum
            
            # Check if the window length is reached
            if right - left + 1 == windowLength:
                # Calculate the average of the window and store it in the result array
                res[left + k] = windowSum // windowLength
                
                # Adjust the window sum and move the left pointer
                windowSum -= nums[left]
                left += 1
        
        return res