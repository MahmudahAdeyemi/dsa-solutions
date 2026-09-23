# Sort Colors

**Source:** LeetCode
**Difficulty:** Medium
**Pattern:** Two Pointers / Dutch National Flag

## Approach

Use three pointers: `left`, `i`, and `right`.

`left` keeps track of where the next `0` should be placed, while `right` keeps track of where the next `2` should be placed. The pointer `i` scans through the array.

* If `nums[i]` is `0`, swap it with `nums[left]` and move both `left` and `i`.
* If `nums[i]` is `1`, it is already in the correct middle section, so only move `i`.
* If `nums[i]` is `2`, swap it with `nums[right]` and move `right`. Do not move `i` because the new value at `i` has not been examined yet.

Continue until `i` passes `right`.

## Complexity

* Time: O(n)
* Space: O(1)

## Lesson

With multiple possible values, multiple pointers can divide the array into sections that are already correctly positioned. When swapping with the right side, the incoming element must be examined before moving the scanning pointer.
