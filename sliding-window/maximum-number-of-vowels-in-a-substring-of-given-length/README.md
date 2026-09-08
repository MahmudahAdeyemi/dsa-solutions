# Maximum Number of Vowels in a Substring of Given Length

**Source:** LeetCode
**Difficulty:** Medium
**Pattern:** Fixed-Size Sliding Window

## Approach

Use a sliding window of exactly `k` characters.

First, count the number of vowels in the first `k` characters and store it in `count`.

Then slide the window through the string one character at a time. When a new character enters the window, increase the count if it is a vowel. When a character leaves the window, decrease the count if it is a vowel.

Keep track of the maximum number of vowels found in any window.

## Complexity

* Time: O(n)
* Space: O(1)

## Lesson

For fixed-size substring problems, we can maintain information about the current window instead of recalculating it from scratch. By adding the incoming character and removing the outgoing character, each window can be processed in constant time.
