# Product of Array Except Self

**Source:** LeetCode
**Difficulty:** Medium
**Pattern:** Prefix/Suffix Product

## Approach

I first build an array containing the product of all elements to the left of each position.

Then I traverse the array from right to left while maintaining `rightproduct`, which represents the product of all elements to the right.

For each position, I multiply the existing left product by the right product to get the product of every element except the current one.

## Complexity

* Time: O(n)
* Space: O(1) extra space

The output array is used to store the left products, so I don't need a separate result array or a separate suffix-product array.

## Lesson

An array problem can often be solved by separating the information on the left and right of each position. Prefix and suffix products allow me to calculate the required result in linear time without using division.
