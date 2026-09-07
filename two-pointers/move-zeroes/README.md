# Move Zeroes

**Source:** LeetCode
**Difficulty:** Easy
**Pattern:** Two Pointers

## Approach

Use two pointers. `i` scans through the array, while `k` keeps track of the position where the next non-zero element should be placed.

Whenever `nums[i]` is not zero, swap `nums[i]` with `nums[k]` and move `k` forward. This moves all non-zero elements to the front while keeping the zeroes at the end.

## Complexity

* Time: O(n)
* Space: O(1)

## Lesson

The slow/fast pointer technique can be used to rearrange an array in-place while keeping only the elements we care about in the front.
