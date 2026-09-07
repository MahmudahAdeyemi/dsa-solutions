# Merge Sorted Array

**Source:** LeetCode
**Difficulty:** Easy
**Pattern:** Two Pointers

## Approach

Use three pointers starting from the end of the arrays.

`i` points to the last valid element in `nums1`, `j` points to the last element in `nums2`, and `k` points to the last position available in `nums1`.

Compare `nums1[i]` and `nums2[j]`, place the larger value at `nums1[k]`, and move the corresponding pointer backward.

We work backwards so that we do not overwrite the elements in `nums1` that still need to be compared.

## Complexity

* Time: O(m + n)
* Space: O(1)

## Lesson

When merging sorted arrays in-place, working from the end allows us to use the extra space already available in `nums1` without overwriting useful values.
