# Best Time to Buy and Sell Stock

**Source:** LeetCode
**Difficulty:** Easy
**Pattern:** Sliding Window

## Approach

Keep track of the lowest price seen so far using `minprice`.

For each price, calculate the profit we would get by buying at `minprice` and selling at the current price. Update `profit` if this is the best profit found so far.

If the current price is lower than `minprice`, update `minprice`.

## Complexity

* Time: O(n)
* Space: O(1)

## Lesson

We don't need to compare every possible buy and sell day. By keeping track of the cheapest price seen so far, we can determine the best possible profit for each selling day in one pass.
