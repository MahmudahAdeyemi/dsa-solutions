# Reverse String

**Source:** LeetCode
**Difficulty:** Easy
**Pattern:** Two Pointers

## Approach

Use two pointers, `left` and `right`, starting at the beginning and end of the array.

Swap the characters at these positions, then move `left` forward and `right` backward. Continue until the pointers meet.

The string is modified in-place.

## Complexity

* Time: O(n)
* Space: O(1)

## Lesson

Two pointers can efficiently process an array from both ends. Swapping the elements while moving toward the middle allows the array to be reversed in-place.
