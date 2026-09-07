# Container With Most Water

**Source:** LeetCode
**Difficulty:** Medium
**Pattern:** Two Pointers

## Approach

I start with two pointers at the beginning and end of the array. This gives me the widest possible container.

For each pair of pointers, I calculate the area using the shorter of the two heights multiplied by the distance between them.

I then move the pointer with the shorter height because the shorter side limits the amount of water the container can hold. I continue this until the two pointers meet while keeping track of the maximum area found.

## Complexity

* **Time:** O(n)
* **Space:** O(1)

## Lesson

I learned that in this problem, moving the pointer with the taller height cannot give a better area because the shorter height is the limiting factor. This allows the two-pointer approach to eliminate unnecessary possibilities while scanning the array once.
