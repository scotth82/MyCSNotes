# Leet Code - Blind 75

|Status|Category|Problem|Difficulty|Solution|Date|
|:-:|:-:|:-|:-:|:-:|:-:|
| X - 01 |Array|[1. Two Sum](https://leetcode.com/problems/two-sum/)|Easy|[Python](#1-two-sum)|09/02/2022|
||Array|[121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)|Easy|Python||
||Array|[217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)|Easy|Python||
||Array|[53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)|Medium|Python||
||Array|[152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)|Medium|Python||
||Array|[153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)|Medium|Python||
||Array|[33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)|Medium|Python||
||Array|[15. 3Sum](https://leetcode.com/problems/3sum/)|Medium|Python||
||Array|[11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)|Medium|Python||
||Binary|[371. Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/)|Medium|Python||
||Binary|[191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)|Easy|[Python](#191-number-of-1-bits)||
||Binary|[338. Counting Bits](https://leetcode.com/problems/counting-bits/)|Easy|Python||
||Binary|[268. Missing Number](https://leetcode.com/problems/missing-number/)|Easy|Python||
||Binary|[190. Reverse Bits](https://leetcode.com/problems/reverse-bits/)|Easy|Python||

#### 1. Two Sum
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
```

#### 191. Number of 1 Bits
```python
Python bitwise operation
```

#### 217. Contains Duplicate
'''python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) != len(nums):
                return True
        return False
'''
