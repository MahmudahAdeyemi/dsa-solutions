# Subarray Sum Equals K

**Source:** LeetCode
**Difficulty:** Medium
**Pattern:** Prefix Sum + Hash Map

## Approach

Keep a running prefix sum while traversing the array.

For each current prefix sum, check whether `prefixsum - k` has appeared before. If it has, every occurrence represents a subarray whose sum is `k`, so add its frequency to `count`.

The hash map stores how many times each prefix sum has appeared.

## Complexity

- Time: O(n)
- Space: O(n)

## Lesson

A prefix sum combined with a frequency hash map can count subarrays with a target sum efficiently.