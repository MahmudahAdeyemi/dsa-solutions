# Valid Anagram

**Source:** LeetCode
**Difficulty:** Easy
**Pattern:** Hash Map / Frequency Counting

## Approach

I first check whether both strings have the same length. If they don't, they cannot be anagrams.

I then use two hash maps to count the frequency of each character in `s` and `t`. After building both frequency maps, I compare their keys and character counts to determine whether the strings contain the same characters with the same frequencies.

## Complexity

* Time: O(n)
* Space: O(n)

## Lesson

Hash maps can be used to count the frequency of elements. For an anagram problem, two strings must contain exactly the same characters with exactly the same frequencies.
