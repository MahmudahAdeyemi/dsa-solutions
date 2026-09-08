# Maximum Average Subarray I

**Source:** LeetCode
**Difficulty:** Easy
**Pattern:** Fixed-Size Sliding Window

## Approach

Use a sliding window of exactly `k` elements.

First calculate the sum of the first `k` elements. Then move the window through the array by adding the new element and removing the element that leaves the window.

Track the maximum window sum and divide it by `k` to get the maximum average.

## Complexity

- Time: O(n)
- Space: O(1)

## Lesson

A fixed-size sliding window avoids repeatedly calculating the sum of overlapping subarrays.