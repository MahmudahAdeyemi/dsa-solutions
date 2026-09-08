# Valid Palindrome II

**Source:** LeetCode
**Difficulty:** Easy
**Pattern:** Two Pointers

## Approach

Use two pointers starting from both ends of the string and compare the characters.

When a mismatch is found, there are only two possible characters that can be removed: the character at the left pointer or the character at the right pointer.

Check both possibilities using a helper function that determines whether the remaining substring is a palindrome. If either is a palindrome, return `True`.

## Complexity

- Time: O(n)
- Space: O(1)

## Lesson

When using two pointers, a mismatch can sometimes create a small number of possible choices. Instead of trying every deletion, we only need to consider the two characters involved in the first mismatch.