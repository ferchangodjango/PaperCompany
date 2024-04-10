from faker import Faker
import random
import numpy as np
Seller=[]
fake=Faker()
for i in range(20):
    Seller.append((fake.name(),fake.last_name(),fake.email()))


ProductsPrice=[]
Products=[
    'Offset paper','Bond paper','Coasted paper','Tracing paper','Photo paper',
    'Copy paper','Inkjet paper','Kraft paper','Newsprint','Cardstock',
    'Fish paper','Laid paper','Mette paper'
]
Price=[100,110,105,105,110,
       200,150,120,120,100,
       105,110,150]
for i in range(len(Products)):
    ProductsPrice.append((Products[i],Price[i]))

