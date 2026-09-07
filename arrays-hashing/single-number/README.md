# Single Number

**Source:** LeetCode
**Difficulty:** Easy
**Pattern:** Hash Map

## Approach

I used a hash map to count how many times each number appears in the array.

After counting all the numbers, I iterate through the dictionary and return the number whose count is `1`.

## Complexity

* Time: O(n)
* Space: O(n)

## Lesson

A hash map can be used to keep track of the frequency of elements and quickly identify the element that appears only once.

An alternative solution uses XOR and achieves O(1) extra space.
