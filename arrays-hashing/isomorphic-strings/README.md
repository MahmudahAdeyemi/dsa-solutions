# Isomorphic Strings

**Source:** LeetCode
**Difficulty:** Easy
**Pattern:** Hash Map

## Approach

I used two hash maps to keep track of the character mappings in both directions.

`sdic` maps characters from `s` to characters in `t`, while `tdic` maps characters from `t` back to characters in `s`.

For each pair of characters, I check whether an existing mapping contradicts the current mapping. If there is a contradiction, the strings are not isomorphic. Otherwise, I update both dictionaries.

## Complexity

* Time: O(n)
* Space: O(n)

## Lesson

When a relationship must be one-to-one, checking the mapping in only one direction is not enough. Using two hash maps allows me to verify the relationship in both directions.
