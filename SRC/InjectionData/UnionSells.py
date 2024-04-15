#Minando la base de datos.
import pandas as pd
import numpy as np
import random
from ProductsTotales import DataProducts
from SellData import DataSellers
#Get the list of the sellers uniques
ID_SELLER=list(DataSellers['IDSELLER'])
#Get the list of the Id products and the price uniques
ID_PRODUCTS=list(DataProducts['IDPRODUCTS'])
PRICE_PRODUCTS=list(DataProducts['PRODUCTPRICE'])
#Get a random quantity of sells, for 50 sells.
QUANTITY_SELLS=[random.randint(1,10) for i in range(2)]
QUANTITY_ID_RANDMO=[random.randint(0,12) for i in range(2)]
#Main table for use in the list.
TOTAL_SELLER=[(ID_PRODUCTS[QUANTITY_ID_RANDMO[i]],random.choice(ID_SELLER),QUANTITY_SELLS[i]) for i in range(2)]
#print(TOTAL_SELLER)
