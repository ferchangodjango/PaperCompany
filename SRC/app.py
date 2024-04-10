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

app=Flask(__name__)
db=MySQL(app)
manager=LoginManager(app)

@manager.user_loader
def userloader(id):
    return ModelUser.GetById(db,id)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        user=User(0,request.form['Username'],request.form['Password'])
        loggeduser=ModelUser.LoggedUser(db,user)
        if loggeduser !=None:
            login_user(loggeduser)
            if loggeduser.password:
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

@app.route('/plot')
def plot():
    data=Analisys.pareto_profit_sellers(db)
    return render_template('page.html',data=data)


if __name__=='__main__':
    app.config.from_object(ConfigObject)
    app.run()