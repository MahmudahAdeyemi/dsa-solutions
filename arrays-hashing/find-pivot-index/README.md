# Find Pivot Index

**Source:** LeetCode
**Difficulty:** Easy
**Pattern:** Prefix Sum

## Approach

First, calculate the total sum of the array.

Then, traverse the array while keeping track of the sum of all elements to the left of the current index.

For each index, calculate the right sum using:

`right sum = total sum - left sum - current element`

If the left sum and right sum are equal, the current index is the pivot index.

If no pivot index exists, return `-1`.

## Complexity

* Time: O(n)
* Space: O(1)

## Lesson

A total sum and a running left sum are enough to determine the right sum at every index without creating a separate prefix-sum array.
