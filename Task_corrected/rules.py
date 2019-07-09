import pandas as pd
import random as randn
import math

# List of prices according to: http://codekata.com/kata/kata09-back-to-the-checkout/
items = ['A', 'B', 'C', 'D']
data = {'A': [50], 
        'B': [30],
        'C': [20],
        'D': [15]}
df = pd.DataFrame(data, columns = items)

#Offers or Promotions according the instructions: http://codekata.com/kata/kata09-back-to-the-checkout/
offer_A = 130 # 3 items
offer_B = 45  # 2 items

