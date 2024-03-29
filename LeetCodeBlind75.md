# Leet Code - Blind 75

|Status|Category|Problem|Difficulty|Solution|Date|
|:-:|:-:|:-:|:-:|:-:|:-:|
|:fire:|Array|[1. Two Sum](https://leetcode.com/problems/two-sum/)|Easy|[Python](#1-two-sum)|01/18/2024|
|:fire:|Array|[242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)|Easy|[Python](#242-valid-anagram)|01/18/2024|
|:fire:|Array|[217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)|Easy|[Python](#217-contains-duplicate)|01/18/2024|
|:fire:|Array|[49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)|Medium|[Python](#49-group-anagrams)|01/19/2024|
|:fire:|Array|[347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)|Medium|[Python](#347-top-k-frequent-elements)|01/21/2024|
|:fire:|Array|[238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)|Medium|[Python](#238-product-of-array-except-self)|01/24/2024|
|:fire:|Array|[128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)|Medium|[Python](#128-longest-consecutive-sequence)|01/25/2024|
|:fire:|Bit Manipulation|[191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)|Easy|[Python](#191-number-of-1-bits)|01/25/2024|
|:fire:|Bit Manipulation|[338. Counting Bits](https://leetcode.com/problems/counting-bits/)|Easy|[Python](#338-counting-bits)|01/25/2024|
|:fire:|Bit Manipulation|[190. Reverse Bits](https://leetcode.com/problems/reverse-bits/)|Easy|[Python](#190-reverse-bits)|01/26/2024|
|:fire:|Bit Manipulation|[268. Missing Number](https://leetcode.com/problems/missing-number/)|Easy|[Python](#268-missing-number)|01/26/2024|
|:fire:|Bit Manipulation|[371. Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/description/)|Medium|[Python](#371-sum-of-two-integers)|01/29/2024|
|:fire:|Two Pointers|[125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/description/)|Easy|[Python](#125-valid-palindrome)|01/29/2024|

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

#### 191. Number of 1 Bits
```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        tot = 0
        for x in bin(n)[2:]:
            if x == "1":
                tot += 1
        return tot
```

#### 338. Counting Bits
```python
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            ans.append(bin(i).count("1"))
        return ans
```

#### 190. Reverse Bits
```python
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            bit = (n >> i) & 1  # get the LSB by right shift one bit at a time starting by left shift zero, i from index 0 to 31, total of 32 bits, set bit to AND 1
            result = result | bit << (31 - i)  # shift LSB all the way to left, effectively reversing order, and save to variable result
```

#### 268. Missing Number
```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (1+len(nums)) * len(nums) // 2 - sum(nums)
```

#### 371. Sum of Two Integers
```python
class Solution:
    def getSum(self, a: int, b: int) -> int:
        x = [a, b]
        return sum(x)
```

#### 125. Valid Palindrome
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        res = ""
        for c in s:
            if c.isalnum():
                res += c
        print(res)

        return res == res[::-1]
```