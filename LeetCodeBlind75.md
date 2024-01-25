# Leet Code - Blind 75

|Status|Category|Problem|Difficulty|Solution|Date|
|:-:|:-:|:-:|:-:|:-:|:-:|
|:fire:|Array|[1. Two Sum](https://leetcode.com/problems/two-sum/)|Easy|[Python](#1-two-sum)|01/18/2024|
|:fire:|Array|[242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)|Easy|[Python](#242-valid-anagram)|01/18/2024|
|:fire:|Array|[217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)|Easy|[Python](#217-contains-duplicate)|01/18/2024|
|:fire:|Array|[49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)|Medium|[Python](#49-group-anagrams)|01/19/2024|
|:fire:|Array|[347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)|Medium|[Python](#347-top-k-frequent-elements)|01/21/2024|
|:fire:|Array|[238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)|Medium|[Python](#238-product-of-array-except-self)|01/24/2024|
|:fire:|Array|[128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)|Medium|[Python](#128-longest-consecutive-sequence)||


#### 1. Two Sum
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for idx, val in enumerate(nums):
            ans = target - val
            if ans in hashMap:
                return [hashMap[ans], idx]
            hashMap[val] = idx
```

#### 242. Valid Anagram
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        dictS = {}
        dictT = {}

        for char in s:
            dictS[char] = dictS.get(char, 0) + 1
        
        for char in t:
            dictT[char] = dictT.get(char, 0) + 1
        
        return dictS == dictT
```

#### 217. Contains Duplicate
```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) != len(nums):
                return True
        return False
```

#### 49. Group Anagrams
```python
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        hashMap = defaultdict(list)

        for word in strs:
            sorted_word = sorted(word)
            hashMap[tuple(sorted_word)].append(word)

        return hashMap.values()
```

#### 347. Top K Frequent Elements
```python
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = Counter(nums).most_common(k)
        return list(zip(*x))[0]
```

#### 238. Product of Array Except Self
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        prefix = 1 # set first prefix to 1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i] # prefix for next i is current prefix times current num

        postfix = 1 # set last postfix to 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]
        
        return ans
```

#### 128. Longest Consecutive Sequence
```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLen = 0

        for num in numSet:
            if num - 1 not in numSet:
                length = 1

                while num + length in numSet:
                    length += 1

                maxLen = max(maxLen, length)

        return maxLen
```
