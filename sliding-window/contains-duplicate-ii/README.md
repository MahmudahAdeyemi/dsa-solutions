# Contains Duplicate II

**Source:** LeetCode
**Difficulty:** Easy
**Pattern:** Sliding Window + Hash Set

## Approach

I used a sliding window represented by a set.

For each number, I first check whether it already exists in the current window. If it does, then there are two equal values whose indices are at most `k` apart, so I return `True`.

After adding the current number to the window, I remove the element at `i - k` whenever the window becomes larger than `k`. This keeps only the relevant elements within the required distance.

## Complexity

* Time: O(n)
* Space: O(k)

## Lesson

Unlike a normal duplicate check where I need to remember every element, this problem only requires remembering elements within a certain distance. A sliding window combined with a hash set makes this efficient.
