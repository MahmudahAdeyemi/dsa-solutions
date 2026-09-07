# Permutation in String

**Source:** LeetCode
**Difficulty:** Medium
**Pattern:** Sliding Window + Hash Map

## Approach

Use a sliding window with the same length as `s1`.

First, store the character frequencies of `s1` and the first window of `s2`. Then move the window one character at a time by adding the new character and removing the character that leaves the window.

If the frequency dictionaries are equal, the current window contains exactly the same characters as `s1`, meaning it is a permutation of `s1`.

## Complexity

- Time: O(n)
- Space: O(k)

## Lesson

A fixed-size sliding window can be used to find whether a substring has the same character frequencies as another string.