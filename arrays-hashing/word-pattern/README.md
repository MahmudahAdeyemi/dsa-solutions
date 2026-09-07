# Word Pattern

**Source:** LeetCode
**Difficulty:** Easy
**Pattern:** Hash Map / Two-Way Mapping

## Approach

Split the string into words and first make sure the number of words matches the length of the pattern.

Use a dictionary to map each pattern character to a word. If a character already has a mapping, make sure it maps to the same word. If the word is already mapped to another character, return `False`.

This ensures that the mapping between pattern characters and words is one-to-one.

## Complexity

* Time: O(n)
* Space: O(n)

## Lesson

When two things must have a one-to-one relationship, checking only one direction is not enough. Both the character-to-word and word-to-character relationships need to be consistent.
