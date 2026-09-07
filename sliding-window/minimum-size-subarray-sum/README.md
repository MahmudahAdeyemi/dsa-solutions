# Minimum Size Subarray Sum

**Source:** LeetCode
**Difficulty:** Medium
**Pattern:** Sliding Window

## Approach

I used a sliding window with two pointers, `left` and `right`.

I expand the window by moving `right` and adding each number to `currentsum`. Whenever the sum becomes greater than or equal to the target, I shrink the window from the left while keeping the sum valid. This allows me to find the smallest valid subarray.

`minimumvalue` keeps track of the smallest valid window found.

## Complexity

* Time: O(n)
* Space: O(1)

## Lesson

When working with a positive-number array, a sliding window can efficiently find the minimum-length subarray that satisfies a sum condition without checking every possible subarray.
