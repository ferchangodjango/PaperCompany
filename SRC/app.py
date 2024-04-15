from flask import Flask,render_template,request,redirect,flash,url_for
from config import ConfigObject
from flask_mysqldb import MySQL
from flask_login import LoginManager,login_user,logout_user,login_required
#Entities
from models.entities.User import User
#Models
from models.ModelUser import ModelUser
#Data Analisys
from DataAnalisys.DataAnalisys import Analisys
from DataAnalisys.Query import Query

app=Flask(__name__)
db=MySQL(app)
manager=LoginManager(app)

@manager.user_loader
def userloader(id):
    return ModelUser.GetById(db,id)


@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        user=User(0,request.form['Username'],request.form['Password'])
        loggeduser=ModelUser.LoggedUser(db,user)
        if loggeduser !=None:
            
            if loggeduser.password:
                login_user(loggeduser)
                return redirect(url_for('home'))
            
            else:
                flash('Invalid Password')
                return render_template('Auth/login.html')
        
        else:
            flash('User not found')
            return render_template('Auth/login.html')
    else:
        return render_template('Auth/login.html')
    
@app.route('/home')
@login_required
def home():
    return render_template('home.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/plot',methods=['GET'])
@login_required
def plot():
    
    #Definiendo los Query del sistema
    query_seller_profit=Query.queryprofitseller()
    query_seller_quantity=Query.queryquantityseller()

    query_product_profit=Query.queryprofitproducts()
    query_product_quantity=Query.queryquantityproducts()

    query_stack=Query.querystackchar()
    
    #Definiendo graficas
    seller_profit=Analisys.queryexecute(db,query_seller_profit,'sellers','profit')
    seller_quantity=Analisys.queryexecute(db,query_seller_quantity,'sellers','Quantity')

    product_profit=Analisys.queryexecute(db,query_product_profit,'product','profit')
    product_quantity=Analisys.queryexecute(db,query_product_quantity,'product','quantity')

    seller_products_profit=Analisys.queryexecutestack(db,query_stack,'seller','products','profit')
    #Definiendo la lista de diccionarios
    lista_diccionarios=[seller_profit,seller_quantity,product_profit,product_quantity,seller_products_profit]

    #Definiendo el diccionario maestro.
    data=Analisys.uniondictionary(lista_diccionarios)
    
    
    return render_template('generalplot.html',data=data)


if __name__=='__main__':
    app.config.from_object(ConfigObject)
    app.run()