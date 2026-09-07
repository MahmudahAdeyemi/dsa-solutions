# Is Subsequence

**Source:** LeetCode
**Difficulty:** Easy
**Pattern:** Two Pointers

## Approach

Use one pointer to scan through `t` and another variable, `count`, to track the current character needed from `s`.

Whenever the current character in `t` matches the current character in `s`, move `count` forward. If `count` reaches the length of `s`, every character has been found in the correct order.

## Complexity

* Time: O(n)
* Space: O(1)

## Lesson

Two pointers can be used to determine whether one sequence appears inside another while preserving the original order. The characters do not need to be adjacent; they only need to appear in the correct order.
