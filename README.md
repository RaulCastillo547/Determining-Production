# Quantity-Optimizer
Small project that models how companies find the right quantity of products to produce to maximize profits given costs, competition, and demand.

## How to Navigate:
- `Data Analysis.ipynb` is the main file of the project, containing my analysis of what my code can show.
- The definitions folder contains two files with the project's code: `market_class.py` defines the Market() class, and  `analysis_functions.py` defines functions that analyze the Market() class using graphs.

## Overall Notes:
- **Challenges**:
    - Organization/Maintaining Simplicity: I wanted the `Data Analysis.ipynb` file to contain simplified code, having it focus on analysis and leave the code to the `definitions` folder's files. I solved this issue by relying on Python's class and module import systems which allow me to import and use the necessary code.
    - Aligning Model with Math: Modeling my underlying scenario (as described in the `Data Analysis.ipynb` file) in code required some way to ensure that the results I get out match with what I expect mathematically. This system allowed me to resolve initial issues involving graphs not peaking around my predicted a quantity values. However, there was a case involving graphs peaking 1 point beyond my estimated quantity values which was a result of me neglecting to shift my demand curves 1 point to the left.
- **Enjoyed**:
    - Modeling Data: Matplotlib uses easy-to-understand code that made creating charts from scratch relatively easy and fun.
    - Applying What I Learned in Class: During my Introduction to Programming Concepts class, I got to learn about Python's classes and about different methods usable by certain data types. It is through this information that I was able to overcome issues of organization and applying my scenario into code the way I did.
- **For Future Projects**:
    - Account for More Variables: For this project, I was not sure how to account for changes in the cost-margin that would occur in a real-life competitive environment. I was still able to capture some market phenomenon; although other phenomenon is locked behind prices changes. Thus, a future attempt done when I am more knowledgeable will account for more variables.
     - *What I manage to capture*:
        - Law of Demand: In my project, when companies set prices low, they begin to sell more units. This matches the law's statement that lower prices increase the amount of units customers are willing to buy (Hayes, 2022).
        - Competition's Effects on Profits: The scenario and code match the description and mimics some aspects of a pure competition market, given that all companies sell the exact same goods and that the cheapest goods get bought (Hayes, 2020; Hayes, 2023).
    - *What I still need to capture*:
        - Law of Supply: I have not yet found a way to mimic the law of supply likely due to my companies not being able to stockpile goods (Investopedia, 2023).
        - The Conclusion of Pure Competition: Pure competition leads to companies that produce near zero profits as companies continuely decrease their prices (Hayes, 2023); this is not possible in my simulation given that companies cannot change their prices.

Sources:
Hayes, A. (2020, December 28). "Price-taker: Definition, perfect competition, and examples". Investopedia. https://www.investopedia.com/terms/p/pricetaker.asp

Hayes, A. (2022, January 8). "What is the law of demand in economics, and how does it work?". Investopedia. https://www.investopedia.com/terms/l/lawofdemand.asp.

Hayes, A. (2023, May 11). "Perfect competition: Examples and how it works". Investopedia. https://www.investopedia.com/terms/p/perfectcompetition.asp

Investopedia. (2023, April 10). "The law of supply explained, with the ccurve types, and examples". Investopedia. https://www.investopedia.com/terms/l/lawofsupply.asp
