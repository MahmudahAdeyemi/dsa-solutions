# Remove Duplicates from Sorted Array

**Source:** LeetCode
**Difficulty:** Easy
**Pattern:** Two Pointers

## Approach

Because the array is sorted, duplicate values are next to each other.

`i` scans through the array while `k` keeps track of the position where the next unique value should be placed. Whenever `nums[i]` is different from the previous value, we copy it to `nums[k]` and move `k` forward.

At the end, `k` represents the number of unique elements.

## Complexity

* Time: O(n)
* Space: O(1)

## Lesson

A sorted array allows us to detect duplicates by comparing adjacent elements. The slow/fast pointer technique lets us modify the array in-place without using another array.
