# Find and Replace Pattern

**Source:** LeetCode
**Difficulty:** Medium
**Pattern:** Hash Map / Two-Way Mapping

## Approach

For each word, use a hash map to map each character in `pattern` to the corresponding character in the word.

If a pattern character has already been mapped, make sure it maps to the same word character. If it is a new pattern character, check that the corresponding word character has not already been mapped to another pattern character.

This ensures that the mapping is consistent and one-to-one.

If the word satisfies these conditions for every character, add it to the result.

## Complexity

Let `n` be the number of words and `m` be the length of each word.

* Time: O(n × m)
* Space: O(m)

## Lesson

Pattern-matching problems can often be solved by maintaining a consistent mapping between two sequences. A one-way mapping is not enough when the relationship must be one-to-one, so we also need to make sure that a character in the word is not mapped to multiple pattern characters.
