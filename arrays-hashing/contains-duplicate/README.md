# Contains Duplicate

**Source:** LeetCode
**Difficulty:** Easy
**Pattern:** Hash Map

## Approach

I used a hash map to keep track of the numbers I have already seen.

For each number, I check whether it already exists in the dictionary. If it does, then the array contains a duplicate, so I return `True`. Otherwise, I add the number to the dictionary.

If I finish checking the array without finding a duplicate, I return `False`.

## Complexity

* Time: O(n)
* Space: O(n)

## Lesson

A hash map or hash set allows me to quickly check whether I have already encountered an element. This avoids comparing every pair of elements.
