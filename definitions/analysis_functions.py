from definitions.market_class import Market
import numpy as np
from matplotlib import pyplot as plt

# Functions run and take data from sessions in a market class.
# Then, the functions output a matplotlib graph showcasing the data.
def single_company(market_class):
    # single_company() runs sessions with only one seller and takes in session data.
    quantity_sold = []
    price_per_item = []
    profits = {}

    company_name = list(market_class.sellers.keys())[0]

    for i in range(10000):
        data = market_class.sellers[company_name]
        current_quantity = data['Quantity']
        costs = data['Costs']
        
        quantity_sold.append(current_quantity)
        price_per_item.append((costs(current_quantity)/current_quantity)*data['Profit Margin'])
        
        market_class.session()
        data = market_class.sellers[company_name]
        
        if current_quantity not in profits:
            profits[current_quantity] = []
        
        profits[current_quantity].append(data['Previous Profit'])
        
    # Supply and Demand Extraction
    buyer_prices = np.array(sorted(market_class.buyer_prices)[::-1])
    buyer_quantities = [i + 1 for i in range(len(buyer_prices))]

    # Quantity Charts/Profit Simplification
    names = profits.keys()
    for quantity in names:
        count = len(profits[quantity])
        average = sum(profits[quantity])/count
        
        profits[quantity] = (count, average)

    ## Graph Definitions
    fig, ((ax1, ax4), (ax2, ax3)) = plt.subplots(2, 2, height_ratios=[10,10], facecolor='#ffffff')
    ax4.remove()
    fig.set_figwidth(20)
    fig.set_figheight(10)

    # Supply and Demand
    ax1.scatter(quantity_sold, price_per_item, label='Supply', c='#e80707')
    ax1.scatter(buyer_quantities, buyer_prices, label='Demand', c='#078ee8')

    ax1.set_title('Supply and Demand', fontsize=15, color='#000000')
    ax1.set_xlabel('Quantity', fontsize=15, color='#000000')
    ax1.set_ylabel('Price', fontsize=15, color='#000000')

    ax1.legend()

    # Quantity v Profits
    quantities = profits.keys()
    prices = [val[1] for val in profits.values()]
    colors = ['#0a8f00' if i >= 0 else '#e80707' for i in prices]

    ax2.bar(quantities, prices, color=colors)

    ax2.set_title('Average Profit (Loss) per Quantity', fontsize=15, color='#000000')
    ax2.set_xlabel('Quantity', fontsize=15, color='#000000')
    ax2.set_ylabel('Average Profit (Loss)', fontsize=15, color='#000000')

    # Quantity v Instance
    counts = [val[0] for val in profits.values()]
    ax3.bar(quantities, counts, color='#078ee8')

    ax3.set_title('Count of Quantity Produced', fontsize=15, color='#000000')
    ax3.set_xlabel('Quantity', fontsize=15, color='#000000')
    ax3.set_ylabel('Count', fontsize=15, color='#000000')

    plt.tight_layout()
    plt.show()

def multiple_companies(market_class):
    # Data extraction for each company:
    market_data = {}
    for seller in market_class.sellers:
        market_data.update({seller: {'Quantity Sold': [], 'Price per Item': [], 'Profits': {}, 'Profit Margin': market_class.sellers[seller]['Profit Margin']}})
    
    general_data = {'Total Quantity': [], 'Average Price': []}

    # Profit Simplification
    competitors = market_data.keys()
    
    for i in range(10000):
        total_quantity = 0
        price_sum = 0
        for seller in competitors:
            instance_data = market_class.sellers[seller]
            current_quantity = instance_data['Quantity']
            costs = instance_data['Costs']

            market_data[seller]['Quantity Sold'].append(current_quantity)
            market_data[seller]['Price per Item'].append((costs(current_quantity)/current_quantity)*market_data[seller]['Profit Margin'])

            total_quantity += current_quantity
            price_sum += (costs(current_quantity))
        
        general_data['Total Quantity'].append(total_quantity)
        general_data['Average Price'].append(price_sum/total_quantity)
        
        market_class.session()
        
        for seller in competitors:
            instance_data = market_class.sellers[seller]
            current_quantity = market_data[seller]['Quantity Sold'][-1]
            if current_quantity not in market_data[seller]['Profits']:
                market_data[seller]['Profits'][current_quantity] = []
            market_data[seller]['Profits'][current_quantity].append(instance_data['Previous Profit'])

    # Profit Simplification
    for seller in competitors:
        quantities = market_data[seller]['Profits'].keys()
        for quantity in quantities:
            count = len(market_data[seller]['Profits'][quantity])
            average = sum(market_data[seller]['Profits'][quantity])/count

            market_data[seller]['Profits'][quantity] = (count, average)

    
    # Buyer Prices
    buyer_prices = np.array(sorted(market_class.buyer_prices)[::-1])
    buyer_quantities = [i + 1 for i in range(len(buyer_prices))]

    # Suplot Definition
    fig, axs = plt.subplots(1 + len(competitors), 2, facecolor='#ffffff')
    fig.set_figwidth(20)
    fig.set_figheight(20)

    # Supply and Demand Curve
    axs[0][0].scatter(buyer_quantities, buyer_prices, label='Demand',c='#078ee8')
    for seller in market_data:
        axs[0][0].scatter(market_data[seller]['Quantity Sold'], market_data[seller]['Price per Item'], label=seller)

    axs[0][0].set_title('Supply and Demand', fontsize=15, color='#000000')
    axs[0][0].set_xlabel('Quantity', fontsize=15, color='#000000')
    axs[0][0].set_ylabel('Price', fontsize=15, color='#000000')

    axs[0][0].legend()

    # Average Curve
    axs[0][1].scatter(buyer_quantities, buyer_prices, label='Demand',c='#078ee8')
    axs[0][1].scatter(general_data['Total Quantity'], general_data['Average Price'], label='Supply', c='#33b572')

    axs[0][1].set_title('Market Supply and Demand', fontsize=15, color='#000000')
    axs[0][1].set_xlabel('Quantity', fontsize=15, color='#000000')
    axs[0][1].set_ylabel('Price', fontsize=15, color='#000000')

    axs[0][1].legend()

    # Quantity
    for i, competitor in enumerate(competitors):
        # Quantity v. Profits
        quantities = market_data[competitor]['Profits'].keys()
        prices = [val[1] for val in market_data[competitor]['Profits'].values()]
        colors = ['#0a8f00' if i >= 0 else '#e80707' for i in prices]
        axs[i+1][0].bar(quantities, prices, color=colors)
        axs[i+1][0].set_title(f'Average Profit (Loss) per Quantity for {competitor}', fontsize=15, color='#000000')
        axs[i+1][0].set_xlabel('Quantity', fontsize=15, color='#000000')
        axs[i+1][0].set_ylabel('Average Profit (Loss)', fontsize=15, color='#000000')
        
        # Quantity v Instance
        counts = [val[0] for val in market_data[competitor]['Profits'].values()]
        axs[i+1][1].bar(quantities, counts, color='#078ee8')

        axs[i+1][1].set_title('Count of Quantity Produced', fontsize=15, color='#000000')
        axs[i+1][1].set_xlabel('Quantity', fontsize=15, color='#000000')
        axs[i+1][1].set_ylabel('Count', fontsize=15, color='#000000')
    
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    mk = Market()
    mk.add_buyers([i*5 for i in range(1, 101)])
    mk.add_seller('Company 1', lambda q: 250*q, 0.10)
    
    single_company(mk)