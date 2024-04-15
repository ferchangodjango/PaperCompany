import pandas as pd
from DataAnalisys.Graphs import Pareto,barra_stackeada
from bokeh.embed import components
from bokeh.resources import INLINE
from flask import jsonify

class Analisys():
    @classmethod
    def queryexecute(self,db,query,name_column1,name_column2):
        try:
            cursor=db.connection.cursor()
            cursor.execute(query)
            answer=cursor.fetchall()
            db.connection.commit()
            answers=[]
            for row in answer:
                answer_get={
                    name_column1:row[0],
                    name_column2:row[1]
                }
                answers.append(answer_get)
            
            JSONYFY_QUERY=jsonify({
                "TABLA":answers,
                "message":"Get data ok!!"       
            })
            json_table=JSONYFY_QUERY.get_json()
            DATA_FRAME=pd.json_normalize(json_table['TABLA'])
            DATA_FRAME[name_column2]=DATA_FRAME[name_column2].astype(float)
            pareto=Pareto(DATA_FRAME,name_column1,name_column2)
            script,div=components(pareto)
            js_resources=INLINE.render_js()
            css_resources=INLINE.render_css()
            data={
                "script":script,
                "div":div,
                "js_resources":js_resources,
                "css_resources":css_resources
                }
            return data
            
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod 
    def queryexecutestack(self,db,query,name_column1,name_column2,name_column3):
        try:
            cursor=db.connection.cursor()
            cursor.execute(query)
            answer=cursor.fetchall()
            db.connection.commit()
            answers=[]
            for row in answer:
                answer_get={
                    name_column1:row[0],
                    name_column2:row[1],
                    name_column3:row[2]
                }
                answers.append(answer_get)
            JSONIFY_TOTAL=jsonify({
                "TABLA":answers,
                "message":"Data ok!!"})
            JSON_TABLA=JSONIFY_TOTAL.get_json()
            DATA_FRAME=pd.json_normalize(JSON_TABLA['TABLA'])
            DATA_FRAME[name_column3]=DATA_FRAME[name_column3].astype(float)
            barstack=barra_stackeada(DATA_FRAME,name_column1,name_column2,name_column3)
            script,div=components(barstack)
            js_resources=INLINE.render_js()
            css_resources=INLINE.render_css()
            data={
                "script":script,
                "div":div,
                "js_resources":js_resources,
                "css_resources":css_resources
                }
            
            return data

        except Exception as ex:
            Exception(ex)

    @classmethod
    def uniondictionary(self,lista_diccionarios):
        lista_claves_diccionarios=list(lista_diccionarios[0].keys())
        lista_claves_diccionarios_nuevos=[]
        for i in range(len(lista_diccionarios)):
            for j in lista_claves_diccionarios:
                lista_diccionarios[i][j+str(i+1)]=lista_diccionarios[i].pop(j)
        diccionario_totalote={}
        for i in range(len(lista_diccionarios)):
            diccionario_totalote=diccionario_totalote|lista_diccionarios[i]
        return diccionario_totalote
    
