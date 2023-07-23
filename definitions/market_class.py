from matplotlib import pyplot as plt
import random

# Market class represents a market with sellers and buyers
class Market:
    def __init__(self):
        self.buyer_prices = []
        self.sellers = {}

    def add_seller(self, name, cost_equation, profit_margin):
        # Adds to the market a seller selling goods at a certain cost function and profit margin.
        self.sellers.update({name: {'Costs': cost_equation, 'Profit Margin': 1 + profit_margin, 'Quantity': 1, 'Previous Profit': 0, 'Change': '+'}})
    
    def add_buyers(self, prices_list):
        # Adds to the market a list of prices. Each price represents the maximum price
        # a customer is willing to spend on a product.
        self.buyer_prices += prices_list
    
    def session(self):
        # sessions(self) goes through a day of customers buying and selling.
        # Bottom two functions are used when shifting the amount of goods a
        # company makes after each session.
        def change_sign(sign):
            if sign == '+':
                return '-'
            elif sign == '-':
                return '+'
        
        def change_quantity(sign):
            if sign == '+':
                return 1
            elif sign == '-':
                return -1
        
        # current_market collects data on session activities.
        current_market = {}
        for seller in self.sellers:
            current_market[seller] = {
                'Price per Item': (self.sellers[seller]['Costs'](self.sellers[seller]['Quantity'])/self.sellers[seller]['Quantity'])*self.sellers[seller]['Profit Margin'],
                'Quantity': self.sellers[seller]['Quantity'],
                'Revenue': 0
                }
        
        # Buyers are randomized.
        session_buyers = sorted(self.buyer_prices, key=lambda x: random.random())
        for buyer_price in session_buyers:
            session_sellers = sorted(self.sellers, key=lambda x: current_market[x]['Price per Item'])
            for seller in session_sellers:
                # Loop replicates a buyer looking for and (possibly) buying the cheapest product available that they are willing to buy.
                if buyer_price >= current_market[seller]['Price per Item'] and current_market[seller]['Quantity'] > 0:
                    current_market[seller]['Revenue'] += current_market[seller]['Price per Item']
                    current_market[seller]['Quantity'] -= 1
                    break
        
        # This loop saves the revenue earned from the session to the self.sellers dictionary.
        # The loop also changes the quantity produced depending on whether revenue increased or decreased from the last session.
        for seller in self.sellers:
            current_profit = current_market[seller]['Revenue'] - self.sellers[seller]['Costs'](self.sellers[seller]['Quantity'])
            if current_profit < self.sellers[seller]['Previous Profit']:
                self.sellers[seller]['Change'] = change_sign(self.sellers[seller]['Change'])
            if self.sellers[seller]['Quantity'] <= 1:
                self.sellers[seller]['Change'] = '+'
            
            self.sellers[seller]['Previous Profit'] = current_profit
            self.sellers[seller]['Quantity'] += change_quantity(self.sellers[seller]['Change'])

# Main code defines a test case.
if __name__ == '__main__':
    m = Market()

    m.add_buyers([i*5 for i in range(101)])
    m.add_seller('Malwart Co.', lambda x: (25*x**2), 0.05)
    m.add_seller('Gartet Inc.', lambda x: (250*x), 0.10)

    seller_quantities = {}
    seller_prices = {}
    seller_profits = {}
    for i in range(1000):
        for company in m.sellers:
            if company not in seller_quantities:
                seller_quantities[company] = []        
            if company not in seller_prices:
                seller_prices[company] = []

            seller_quantities[company] += [m.sellers[company]['Quantity']]
            seller_prices[company] += [(m.sellers[company]['Costs'](m.sellers[company]['Quantity'])/m.sellers[company]['Quantity'])*m.sellers[company]['Profit Margin']]
        m.session()
    
    buyer_quantities = [i+1 for i in range(len(m.buyer_prices))]
    buyer_prices = sorted(m.buyer_prices, key=lambda x: -x)
    plt.scatter(buyer_quantities, buyer_prices, label = 'Demand')
    
    for company in m.sellers:
        plt.scatter(seller_quantities[company], seller_prices[company], label = company)

    plt.xlabel('Quantity')
    plt.ylabel('Price')
    plt.legend()

    plt.show()