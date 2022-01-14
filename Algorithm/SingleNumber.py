class Solution(object):
    def singleNumber(self,nums):
        num=nums[0];
        for i in nums[1:]:
            num=num ^ i;
        return num;
s=Solution();
print(s.singleNumber([1,2,3,4,4,3]));

