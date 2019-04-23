from flask import Flask, render_template,request
app = Flask(__name__)


@app.route('/rentbike',methods=["GET","POST"])
def rent_bike():
    if request.method == 'GET':        
        return render_template('rent_bike.html')
    if request.method == 'POST':
        info = request.form
        info_input = {
            "model" : info['model'],
            "dailyfee" : info['dailyfee'],
            "image" : info['image'],
            "year" : info['year'],
        }
        print(info_input)
        return "Done!"

if __name__ == '__main__':
  app.run(debug=True)
 