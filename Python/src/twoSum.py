# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tmp_dict = dict()
        for i, x in enumerate(nums):
            if target - x in tmp_dict:
                return [tmp_dict[target - x], i]
            else:
                tmp_dict[x] = i



if __name__ == '__main__':
    s = Solution()
    print s.twoSum([1,2,3,4,5,6,7,8,9], 10)
    print s.twoSum([], 1)