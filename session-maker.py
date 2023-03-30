from matplotlib import pyplot as plt
import random

# Classes represents a market with suppliers and customers
class Market:
    def __init__(self):
        self.buyer_prices = []
        self.sellers = {}

    def add_seller(self, name, cost_equation):
        # Adds to sellers in a market
        self.sellers.update({name: {'Costs': cost_equation, 'Quantity': 1, 'Previous Profit': 0, 'Change': '+'}})
    
    def add_buyers(self, prices_list):
        # Adds to the customers in a market
        self.buyer_prices += prices_list
    
    def session(self):
        # Transisitions a market through a session, seeing companies change the quantity they produce to maximize profit
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
        
        session_buyers = sorted(self.buyer_prices, key=lambda x: random.random())
        session_sellers = sorted(self.sellers, key=lambda x: random.random())
        for seller in session_sellers:
            # How much do you have to sell
            sellable_goods = self.sellers[seller]['Quantity']

            # How much is the cost of production
            production_cost_equation = self.sellers[seller]['Costs']
            production_cost = production_cost_equation(sellable_goods)

            # What is the price per item
            price_per_item = production_cost/sellable_goods

            # How much can be made
            revenue = 0
            for i in range(sellable_goods):
                if len(session_buyers) <= 0:
                    break
                if session_buyers[0] >= price_per_item:
                    revenue += session_buyers.pop(0)
            
            #How much is the profit
            profit_made = revenue - production_cost
            if profit_made >= self.sellers[seller]['Previous Profit']:
                if self.sellers[seller]['Quantity'] <= 1:
                    self.sellers[seller]['Change'] = '+'
                elif self.sellers[seller]['Quantity'] >= len(self.buyer_prices):
                    self.sellers[seller]['Change'] = '-'
            elif profit_made < self.sellers[seller]['Previous Profit']:
                self.sellers[seller]['Change'] = change_sign(self.sellers[seller]['Change'])
                if self.sellers[seller]['Quantity'] <= 1:
                    self.sellers[seller]['Change'] = '+'
                elif self.sellers[seller]['Quantity'] >= len(self.buyer_prices):
                    self.sellers[seller]['Change'] = '-'
            
            self.sellers[seller]['Quantity'] += change_quantity(self.sellers[seller]['Change'])
            self.sellers[seller]['Previous Profit'] = profit_made

    
    
# Main code defines a test case
if __name__ == '__main__':
    m = Market()

    m.add_buyers([i*2.5 for i in range(100)])
    m.add_seller('Malwart Co.', lambda x: (x*70+50))
    m.add_seller('Gartet Inc.', lambda x: (50*x))

    seller_quantities = {}
    seller_prices = {}
    for i in range(90000):
        m.session()
        for company in m.sellers:
            if company not in seller_quantities:
                seller_quantities[company] = []        
            if company not in seller_prices:
                seller_prices[company] = []
            
            seller_quantities[company] += [m.sellers[company]['Quantity']]
            seller_prices[company] += [m.sellers[company]['Costs'](m.sellers[company]['Quantity'])/m.sellers[company]['Quantity']]
    
    buyer_quantities = [i+1 for i in range(len(m.buyer_prices))]
    buyer_prices = sorted(m.buyer_prices, key=lambda x: -x)
    plt.scatter(buyer_quantities, buyer_prices, label = 'Demand')
    
    for company in m.sellers:
        plt.scatter(seller_quantities[company], seller_prices[company], label = company)

    plt.xlabel('Quantity')
    plt.ylabel('Price')
    plt.legend()

    plt.show()