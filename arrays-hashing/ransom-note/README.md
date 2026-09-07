# Ransom Note

**Source:** LeetCode
**Difficulty:** Easy
**Pattern:** Hash Map / Frequency Counting

## Approach

Count the frequency of every character in `ransomNote` and `magazine` using hash maps.

For each character needed by the ransom note, check that the character exists in the magazine and that the magazine contains at least as many occurrences as required.

If any character is missing or there are not enough occurrences, return `False`. Otherwise, return `True`.

## Complexity

* Time: O(n + m)
* Space: O(k)

## Lesson

Hash maps are useful for counting how many times each value occurs. When comparing two collections, frequency counting can determine whether one contains enough of each required element.
