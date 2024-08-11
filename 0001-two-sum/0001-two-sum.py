class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        searched_element = set()
        for index, element in enumerate(nums):
            other_element = target - element
            if other_element in searched_element:
                return [index, nums.index(other_element)]
            searched_element.add(element)