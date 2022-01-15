class Solution(object):
    def findMin(self, nums):    
        left = 0
        right = len(nums) - 1
    
        while left < right:
          
            if nums[left] < nums[right]:
                return nums[left]
            mid = (left + right) // 2
       
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
    
FindMinArr=Solution();

minAr=FindMinArr.findMin([7,2,5,4,1]);
print(minAr)