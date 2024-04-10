import pandas as pd
import numpy as np
from DataAnalisys.Graphs import Pareto,barra_stackeada
from bokeh.embed import components
from bokeh.resources import INLINE

class Analisys():
    @classmethod
    def pareto_profit_sellers(self,db):

        try:
            connection=db.connect
            #Primera consulta
            QUERY="""SELECT sellers.NAME AS sellers,sum(products.PRODUCTPRICE*sells.QUANTITY)AS profit
                FROM sells
                INNER JOIN sellers ON sells.IDSELLER=sellers.IDSELLER
                INNER JOIN products ON sells.IDPRODUCTS=products.IDPRODUCTS
                GROUP BY sellers
                ORDER BY profit DESC"""
            DATA_FRAME=pd.read_sql_query(QUERY,connection)
            pareto=Pareto(DATA_FRAME,'sellers','profit')
            script,div=components(pareto)
            js_resources=INLINE.render_js()
            css_resources=INLINE.render_css()

            #Segunda consulta
            QUERY2="""SELECT sellers.NAME AS sellers,sum(sells.QUANTITY)AS Quantity
                FROM sells
                INNER JOIN sellers ON sells.IDSELLER=sellers.IDSELLER
                INNER JOIN products ON sells.IDPRODUCTS=products.IDPRODUCTS
                GROUP BY sellers
                ORDER BY Quantity DESC"""
            
            DATA_FRAME2=pd.read_sql_query(QUERY2,connection)
            pareto2=Pareto(DATA_FRAME2,'sellers','Quantity')
            script2,div2=components(pareto2)
            js_resources2=INLINE.render_js()
            css_resources2=INLINE.render_css()

            #Tercera consulta
            QUERY3="""SELECT products.PRODUCTNAME as product,sum(sells.QUANTITY*products.PRODUCTPRICE)AS profit
                FROM sells
                INNER JOIN sellers ON sells.IDSELLER=sellers.IDSELLER
                INNER JOIN products ON sells.IDPRODUCTS=products.IDPRODUCTS
                GROUP BY product 
                ORDER BY profit DESC"""
            
            DATA_FRAME3=pd.read_sql_query(QUERY3,connection)
            pareto3=Pareto(DATA_FRAME3,'product','profit')
            script3,div3=components(pareto3)
            js_resources3=INLINE.render_js()
            css_resources3=INLINE.render_css()

            #Cuarta consulta
            QUERY4="""SELECT products.PRODUCTNAME as product,sum(sells.QUANTITY)AS quantity
                FROM sells
                INNER JOIN sellers ON sells.IDSELLER=sellers.IDSELLER
                INNER JOIN products ON sells.IDPRODUCTS=products.IDPRODUCTS
                GROUP BY product 
                ORDER BY quantity DESC"""
            
            DATA_FRAME4=pd.read_sql_query(QUERY4,connection)
            pareto4=Pareto(DATA_FRAME4,'product','quantity')
            script4,div4=components(pareto4)
            js_resources4=INLINE.render_js()
            css_resources4=INLINE.render_css()

            #Quinta consulta
            QUERY5="""SELECT sellers.NAME AS sellers,products.PRODUCTNAME,products.PRODUCTPRICE*sells.QUANTITY profit
                FROM sells
                INNER JOIN sellers ON sells.IDSELLER=sellers.IDSELLER
                INNER JOIN products ON sells.IDPRODUCTS=products.IDPRODUCTS"""
            
            DATA_FRAME5=pd.read_sql_query(QUERY5,connection)
            barstack5=barra_stackeada(DATA_FRAME5,'sellers','PRODUCTNAME','profit')
            script5,div5=components(barstack5)
            js_resources5=INLINE.render_js()
            css_resources5=INLINE.render_css()




            data={
                "plot_script":script,
                "plot_div":div,
                "js_resources":js_resources,
                "css_resources":css_resources,
                "plot_script2":script2,
                "plot_div2":div2,
                "js_resources2":js_resources2,
                "css_resources2":css_resources2,
                "plot_script3":script3,
                "plot_div3":div3,
                "js_resources3":js_resources3,
                "css_resources3":css_resources3,
                "plot_script4":script4,
                "plot_div4":div4,
                "js_resources4":js_resources4,
                "css_resources4":css_resources4,
                "plot_script5":script5,
                "plot_div5":div5,
                "js_resources5":js_resources5,
                "css_resources5":css_resources5

            }
            
            return data




        except Exception as ex:
            raise Exception(ex)
        
        
        