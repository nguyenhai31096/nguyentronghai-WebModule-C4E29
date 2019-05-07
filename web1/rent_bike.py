from flask import *
from rent_bike_db import rent_bike
app = Flask(__name__)


@app.route('/rentbike',methods=["GET","POST"])
def rent_bikes():
    if request.method == 'GET':        
        return render_template('rent_bike.html')
    elif request.method == 'POST':
        info = request.form

        info_input = {
            "model" : info['model'],
            "dailyfee" : info['dailyfee'],
            "image" : info['image'],
            "year" : info['year'],
        }
        rent_bike.insert_one(info_input)
        return "Done!"

if __name__ == '__main__':
    app.run(debug=True)