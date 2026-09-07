# Remove Element

**Source:** LeetCode
**Difficulty:** Easy
**Pattern:** Two Pointers

## Approach

`i` scans through the array while `k` keeps track of the position where the next element that is not equal to `val` should be placed.

Whenever `nums[i] != val`, we copy `nums[i]` to `nums[k]` and move `k` forward.

At the end, `k` represents the number of elements that are not equal to `val`.

## Complexity

* Time: O(n)
* Space: O(1)

## Lesson

The slow/fast pointer technique can modify an array in-place by using one pointer to scan the elements and another to control where valid elements are written.
