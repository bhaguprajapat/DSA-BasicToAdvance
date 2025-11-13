"""
Best Time to Buy and Sell Stock
leetcode problem:- https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

description:- You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


approuch:-
first of all we inilitaze two variable one is max_profit=0 secound is bestBuyDay=prices[0]
then trigger all element with for loop
check with if condition if bestBuyDay< current_element then 
calculate profit like current_element-bestBuyday
then find max profit currnt ya last profit
then update bestBuyDay with current element is currnt is min then bestBuyPrice 
at the end return max_profit



time Compexity:- O(n) 
space compexity:- O(1)
"""

def BuyAndSellStocks(prices):
    max_profit=0
    best_buy_price=prices[0]
    for curr in range(len(prices)):
        if prices[curr]>best_buy_price:
            curr_profit=prices[curr]-best_buy_price
            max_profit=max(curr_profit,max_profit)
        best_buy_price=min(best_buy_price,prices[curr])
    return max_profit
prices=[7,1,5,3,6,4]
print(BuyAndSellStocks(prices))