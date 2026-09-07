# Longest Substring Without Repeating Characters

**Source:** LeetCode
**Difficulty:** Medium
**Pattern:** Sliding Window

## Approach

I use a sliding window with two pointers, `left` and `right`, and a set called `window`.

The `right` pointer expands the window by moving through the string. If the current character is already in the window, I move the `left` pointer forward and remove characters until the duplicate is removed.

After making sure the window contains no repeated characters, I calculate its length and keep track of the maximum length found.

## Complexity

* **Time:** O(n)
* **Space:** O(n)

## Lesson

I learned how a sliding window can maintain a valid range while moving through a string. The set allows me to quickly check whether a character is already inside the current window.
