# Number of Sub-arrays of Size K and Average Greater Than or Equal to Threshold

**Source:** LeetCode
**Difficulty:** Medium
**Pattern:** Fixed-Size Sliding Window

## Approach

Use a sliding window of exactly `k` elements.

First, calculate the sum of the first `k` elements and check whether their average is greater than or equal to the threshold.

Then slide the window through the array by adding the new element entering the window and subtracting the element leaving the window.

For each window, check whether its average meets the threshold and increment the count if it does.

## Complexity

* Time: O(n)
* Space: O(1)

## Lesson

When every subarray has the same fixed size, a sliding window allows us to efficiently move from one subarray to the next by removing one element and adding another instead of recalculating the entire sum.
