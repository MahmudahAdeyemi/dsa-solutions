# Valid Palindrome

**Source:** LeetCode
**Difficulty:** Easy
**Pattern:** Two Pointers

## Approach

First, create a new string containing only the characters we want to compare and convert it to lowercase.

Then use two pointers: `left` starts at the beginning of the string and `right` starts at the end.

Compare the characters at both pointers. If they are different, the string is not a palindrome. Otherwise, move both pointers toward the center.

If all corresponding characters match, return `True`.

## Complexity

* Time: O(n)
* Space: O(n)

## Lesson

Two pointers can efficiently compare elements from opposite ends of a sequence. This avoids creating a reversed copy of the string for the palindrome check.
