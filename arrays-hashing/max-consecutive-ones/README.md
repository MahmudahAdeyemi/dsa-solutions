# Max Consecutive Ones

**Source:** NeetCode
**Difficulty:** Easy
**Pattern:** Iteration / Counting

## Approach

Traverse the array while keeping track of the current number of consecutive `1`s using `count`.

When the current element is `1`, increase `count`. When a `0` is encountered, reset `count` to `0` because the consecutive sequence has been broken.

After each element, update `maxcount` with the largest streak found so far.

## Complexity

* Time: O(n)
* Space: O(1)

## Lesson

When looking for the longest consecutive sequence, we can maintain a running count and reset it whenever the sequence is broken. Updating the maximum during the traversal allows us to solve the problem in a single pass.
