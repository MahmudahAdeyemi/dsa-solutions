# Running Sum of 1d Array

**Source:** LeetCode
**Difficulty:** Easy
**Pattern:** Prefix Sum

## Approach

Create a `prefix_sum` array with the same length as `nums`.

The first element is the same as the first element of `nums`. For every following index, add the current number to the previous running sum.

This means each position contains the sum of all elements from the beginning of the array up to that position.

## Complexity

* Time: O(n)
* Space: O(n)

## Lesson

A running sum is a simple form of prefix sum. Instead of repeatedly calculating the sum from the beginning, we can reuse the previous prefix sum to calculate the next one.
