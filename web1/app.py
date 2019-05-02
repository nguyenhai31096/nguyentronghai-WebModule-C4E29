from flask import Flask, render_template, request, redirect
from food_db import Foods
from bson.objectid import ObjectId
app = Flask(__name__)



@app.route('/') #>>>>>link in here
def index():
    return "hello c4e 29"

@app.route('/say-hi')
def say_hi():
    return "hi everyone"

@app.route('/say-hi/<name>')
def say_hi_anyone(name):
    return "xin chao {}".format(name)

@app.route('/add/<int:num1>/<int:num2>')
def addnum(num1, num2):
    x = num1 + num2
    x_str = str(x)
    return x_str

@app.route('/food')
def food():
    foods = Foods.find() #get data
    return render_template("food.html", foods= foods)

@app.route('/food/<id>')
def detail(id):
    detail_food = Foods.find_one({'_id': ObjectId(id)})
    return render_template('food_detail.html', food_detail = detail_food)

@app.route('/food/add_food', methods=['GET','POST'])
def add_food():
    if request.method == 'GET':
        return render_template('add_food.html')
    elif request.method == 'POST':
        form = request.form
        new_food = {
            "title": form['title'],
            "description": form['description'],
            "link" : form['link'],
            "type": form['type'],
        }
        Foods.insert_one(new_food)
        return redirect('/food')
@app.route('/food/edit/<id>', methods= ['GET','POST'])
def edit_food(id):
    food = Foods.find_one({"_id": ObjectId(id)})
    if request.method == 'GET':
        return render_template('edit_food.html', food=food)
    elif request.method == "POST":
        form = request.form 
        new_value = { '$set': {
            "title": form["title"],
            "description": form["description"],
            "link": form["link"],
            "type": form["type"]
        }}
        Foods.update_one(food, new_value)
        return redirect('/food')

@app.route('/food/delete/<id>')
def delete(id):
    food = Foods.find_one({"_id": ObjectId(id)})
    Foods.delete_one(food)
    return redirect('/food')
data = {
    "username" : "c4e",
    "pwd" : "c4e",
}
    
@app.route('/login', methods=['GET','POST'])

def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        form = request.form
        login_form = {
            "username": form['username'],
            "pwd": form['pwd'],
        }
        if data["username"] == login_form["username"]:
            if data["pwd"] == login_form["pwd"]:
                return 'WELCOME'
            else:
                return 'forbiden'
        else:
            return 'wrong username!'
            
@app.route('/register', methods=['GET','POST'])
def register_form():
    if request.method == 'POST':
        form = request.form
        return "Register page!"
if __name__ == '__main__':
  app.run( debug=True)

