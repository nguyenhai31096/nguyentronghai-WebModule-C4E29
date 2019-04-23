from flask import Flask, render_template,request
app = Flask(__name__)

bike_list = []
@app.route('/rentbike',methods=["GET","POST"])
def rent_bike():
    if request.method == 'GET':        
        return render_template('rent_bike.html')
    if request.method == 'POST':
        info = request.form
        info_input = {
            "BikeModel" : info['model'],
            "Dailyfee" : info['dailyfee'],
            "ImageLink" : info['image'],
            "Year" : info['year'],
        }
        bike_list.append(info_input)
        print(info_input)
        return "Done!"

if __name__ == '__main__':
  app.run(debug=True)
 