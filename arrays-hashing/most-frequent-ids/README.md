# Most Frequent IDs

**Source:** LeetCode
**Difficulty:** Medium
**Pattern:** Hash Map + Frequency Counting

## Approach

Maintain two hash maps.

`id_count` stores the current frequency of each ID. For every update, calculate the ID's new frequency and update its entry.

`freq_count` stores how many IDs currently have each frequency. When an ID's frequency changes, remove the ID from its old frequency and add it to its new frequency.

Keep track of the largest frequency using `max_freq`. If no ID currently has that frequency, decrease `max_freq` until a frequency that exists is found.

Append the current maximum frequency to the result after every update.

## Complexity

* Time: O(n) amortized
* Space: O(n)

## Lesson

When the value we care about changes dynamically, maintaining a second frequency map can avoid repeatedly searching for the maximum. Instead of calculating the maximum from all IDs after every update, we keep track of which frequencies currently exist.
