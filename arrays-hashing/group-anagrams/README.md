# Group Anagrams

**Source:** LeetCode
**Difficulty:** Medium
**Pattern:** Hash Map

## Approach

For each word, sort its characters and use the resulting string as a key in a hash map.

Anagrams contain the same characters, so when their characters are sorted, they produce the same key. Words with the same key are stored in the same group.

At the end, return all the groups from the hash map.

## Complexity

* Time: O(n × k log k), where `n` is the number of words and `k` is the maximum length of a word.
* Space: O(n × k)

## Lesson

A hash map can be used to group values that share the same characteristic. For anagrams, the sorted characters provide a common key for all words in the group.
