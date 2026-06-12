# Leetcode Problem 121: Best Time to Buy and Sell Stock

### 1. Conceptual Breakdown

At its core, this is an optimization problem that relies on **array traversal** and **state tracking**. You are looking for the maximum difference between two numbers in an array, with a strict temporal constraint: the smaller number (the buy price) must occur at a lower index than the larger number (the sell price).

The fundamental principle here is a **Greedy Approach** mixed with **Dynamic Programming** concepts (specifically, keeping track of optimal sub-states). Instead of looking at every possible pair of days (which would result in an inefficient $O(n^2)$ time complexity), you only need to keep track of the best possible "buy" state as you move forward through the timeline.

### 2. Intuition Building

Imagine you are walking along a timeline of stock prices from left to right. Because you cannot travel back in time to sell a stock, your focus at any given moment is strictly on the present day.

Every day you check the market, you should ask yourself two logical questions:

1. **Is today's price the absolute lowest I have seen so far?** If it is, this is hypothetically the best day to have bought the stock. You memorize this new low.
2. **If I sell today (assuming I bought at that historical lowest price), how much money do I make?** Is this profit larger than the best profit I've recorded on previous days?

By continuously updating your "lowest seen price" and your "highest potential profit" in a single pass, you guarantee that you find the maximum profit without ever violating the rule that buying must precede selling.

### 3. Step-by-Step Strategy

To solve this in $O(n)$ time complexity, follow this repeatable process:

1. **Initialize your trackers:** * Create a variable to track the minimum price (e.g., `min_price`). Set it to an infinitely high number initially, or the price of the stock on the very first day.
* Create a variable to track the maximum profit (e.g., `max_profit`). Set it to `0`, as you cannot have negative profit (you just wouldn't buy).


2. **Traverse the array:** Loop through the prices array one by one.
3. **Update the minimum price:** For each price, check if it is less than your current `min_price`. If so, update `min_price` to this new, lower value.
4. **Calculate potential profit:** If the current price is *not* the new minimum, calculate the profit you would make if you sold today: $Profit = Price_{current} - Price_{minimum}$.
5. **Update maximum profit:** Compare this new profit to your stored `max_profit`. If it's higher, update `max_profit`.
6. **Return the result:** Once the loop finishes, return your `max_profit`.
