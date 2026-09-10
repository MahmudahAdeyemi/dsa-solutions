# Count the Number of Special Characters II

**Source:** LeetCode
**Difficulty:** Medium
**Pattern:** Hash Map / Frequency Tracking

## Approach

Maintain two dictionaries to keep track of lowercase and uppercase characters.

As we traverse the word, store each lowercase character in `lowercaselist` and each uppercase character in `uppercaselist`.

If an uppercase character has already appeared before its lowercase counterpart, remove the lowercase character from `lowercaselist`. This ensures that only lowercase characters that appeared before their uppercase versions remain.

Finally, check each remaining lowercase character to see whether its uppercase version exists in `uppercaselist`. If it does, it is a special character and we increase the count.

## Complexity

* Time: O(n)
* Space: O(1)

## Lesson

When a problem depends not only on whether characters exist but also on their order, we can track information while traversing the string. Removing invalid characters as soon as their ordering condition is violated makes the final check simple.
