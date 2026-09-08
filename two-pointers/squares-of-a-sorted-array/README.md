# Squares of a Sorted Array

**Source:** LeetCode
**Difficulty:** Easy
**Pattern:** Two Pointers

## Approach

Because the array is sorted, the largest squared value must come from either the left end or the right end of the array.

Use two pointers, `left` and `right`, to compare the absolute values at both ends. Place the larger square at the end of the result array and move the corresponding pointer inward.

Fill the result array from right to left because we are placing the largest squares first.

## Complexity

* Time: O(n)
* Space: O(n)

## Lesson

When an array is sorted but squaring the values changes their order, the largest values can still be found by comparing the absolute values at both ends. Two pointers allow us to build the sorted result in linear time.
