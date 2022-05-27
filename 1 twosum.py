class Solution:
    def twoSum(self, nums, target):
        prevMap = {}

        for index, number in enumerate(nums):
            diff = target - number
            if diff in prevMap:
                return [prevMap[diff], index]
            prevMap[number] = index


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    mysolution = Solution()
    print(mysolution.twoSum(nums, target))
