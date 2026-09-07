# Longest Repeating Character Replacement

**Source:** LeetCode
**Difficulty:** Medium
**Pattern:** Sliding Window + Hash Map

## Approach

Use a sliding window with `left` and `right` pointers. Store the frequency of each character in the current window using a hash map.

`max_freq` stores the highest character frequency seen in the window. The number of replacements needed to make every character in the window the same is:

`window length - max_freq`

If this value becomes greater than `k`, shrink the window from the left. Track the largest valid window length.

## Complexity

* Time: O(n)
* Space: O(1)

## Lesson

A sliding window can be used when we need the longest valid substring. The key is identifying a condition that tells us when the current window becomes invalid.
