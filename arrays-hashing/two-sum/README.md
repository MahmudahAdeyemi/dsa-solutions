# Two Sum

**Source:** LeetCode
**Difficulty:** Easy
**Pattern:** Hash Map

## Approach

I use a dictionary called `seen` to store numbers I have already encountered and their indices.

For each number, I calculate its `complement` by subtracting the current number from the target. I then check whether that complement is already in `seen`. If it is, I have found the two numbers that add up to the target.

If the complement isn't in `seen`, I store the current number and its index in the dictionary.

## Complexity

* **Time:** O(n)
* **Space:** O(n)

## Lesson

The main idea I learned is that a hash map can let me quickly check whether the number I need has already appeared, avoiding the need for a nested loop.
