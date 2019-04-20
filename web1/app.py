from flask import Flask, render_template
app = Flask(__name__)

foods = [
    {
        "title": "thịt chó",
        "description": "rất ngon",
        "link" : "http://media.kinhtedothi.vn//2018/02/12/thit_cho_trung_quoc_benh_dai.jpg",
        "type": "eat",
    },
    {
        "title": "bún chả",
        "description": "rất ngon",
        "link" : "https://www.dvpmarket.com/wp-content/uploads/2018/03/Bun-cha-Ha-Noi-thom-ngon-hap-dan.jpg",
        "type": "eat",
    },
    {
        "title": "tiết canh",
        "description": "rất kinh",
        "link" : "https://vcdn-suckhoe.vnecdn.net/2019/01/23/photo1527847101966-15278471019-7986-2036-1548214608.png",
        "type": "eat",
    },
    {
        "title": "detox",
        "description": "giảm cân",
        "link": "https://detoxgreen.vn/wp-content/uploads/2018/03/maxresdefault-1.jpg",
        "type": "drink",
    },
    {
        "title": "coffee",
        "description": "đắng",
        "link":"https://cdn.tuoitre.vn/thumb_w/640/2018/3/29/photo-1-1522310569261591693730.jpg",
        "type": "drink",
    },
    {
        "title": "volka",
        "description": "phê",
        "link": "https://quanngon138.com/upload/product/volka-smirnoff-nga1522165193.png",
        "type": "drink",
    }
    ]
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
    return render_template("food.html", foods= foods)
@app.route('/food/<int:index>')
def detail(index):
    detail_food = foods[index]
    return render_template('food_detail.html', food_detail = detail_food)
if __name__ == '__main__':
  app.run( debug=True)
 