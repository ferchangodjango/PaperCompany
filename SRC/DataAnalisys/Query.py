

class Query():

    @classmethod
    def queryprofitseller(self):
        query="""SELECT sellers.NAME AS sellers,sum(products.PRODUCTPRICE*sells.QUANTITY)AS profit
                FROM sells
                INNER JOIN sellers ON sells.IDSELLER=sellers.IDSELLER
                INNER JOIN products ON sells.IDPRODUCTS=products.IDPRODUCTS
                GROUP BY sellers
                ORDER BY profit DESC"""
        return query
    @classmethod
    def queryprofitproducts(self):
        query="""SELECT products.PRODUCTNAME as product,sum(sells.QUANTITY*products.PRODUCTPRICE)AS profit
                FROM sells
                INNER JOIN sellers ON sells.IDSELLER=sellers.IDSELLER
                INNER JOIN products ON sells.IDPRODUCTS=products.IDPRODUCTS
                GROUP BY product 
                ORDER BY profit DESC"""
        return query
    @classmethod
    def queryquantityseller(self):
        query="""SELECT sellers.NAME AS sellers,sum(sells.QUANTITY)AS Quantity
                FROM sells
                INNER JOIN sellers ON sells.IDSELLER=sellers.IDSELLER
                INNER JOIN products ON sells.IDPRODUCTS=products.IDPRODUCTS
                GROUP BY sellers
                ORDER BY Quantity DESC"""
        return query
    
    @classmethod
    def queryquantityproducts(self):
        query="""SELECT products.PRODUCTNAME as product,sum(sells.QUANTITY)AS quantity
                FROM sells
                INNER JOIN sellers ON sells.IDSELLER=sellers.IDSELLER
                INNER JOIN products ON sells.IDPRODUCTS=products.IDPRODUCTS
                GROUP BY product 
                ORDER BY quantity DESC"""
        return query
    
    @classmethod
    def querystackchar(self):
        query="""SELECT sellers.NAME AS sellers,products.PRODUCTNAME,products.PRODUCTPRICE*sells.QUANTITY profit
                FROM sells
                INNER JOIN sellers ON sells.IDSELLER=sellers.IDSELLER
                INNER JOIN products ON sells.IDPRODUCTS=products.IDPRODUCTS"""
        
        return query