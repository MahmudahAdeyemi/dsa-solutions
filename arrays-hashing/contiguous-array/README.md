# Contiguous Array

**Source:** LeetCode
**Difficulty:** Medium
**Pattern:** Prefix Sum + Hash Map

## Approach

Convert every `0` into `-1`. This makes a subarray with an equal number of `0`s and `1`s have a sum of `0`.

Use a running sum while traversing the array. Store the first index where each running sum occurs in a hash map.

If the same running sum appears again, the elements between the two positions have a sum of `0`, meaning they contain an equal number of `0`s and `1`s. Use the distance between the indices to track the longest such subarray.

## Complexity

* Time: O(n)
* Space: O(n)

## Lesson

Prefix sums can turn a difficult subarray condition into a repeated-value problem. When the same prefix sum appears twice, the elements between those positions have a sum of zero.
