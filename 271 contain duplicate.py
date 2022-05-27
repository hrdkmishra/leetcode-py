class Solution:
    def containsDuplicate(self, nums) -> bool:
        table = set()

        for num in nums:
            if num in table:
                return True
            else:
                table.add(num)
        return False


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    mysolution = Solution()
    print(mysolution.containsDuplicate(nums))
