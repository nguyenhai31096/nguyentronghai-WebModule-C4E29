from flask import Flask, render_template
app = Flask(__name__)
#way 1
@app.route('/bmi/<int:weight>/<int:height>')
# def bmi(weight, height):
   
#    height_m = height/100
#    bmi = weight/(height_m**2)
#    if bmi < 16 :
#       return 'BMI:{} . Severely underweight'.format(str(bmi))
#    elif 16 <= bmi < 18.5:
#       return 'BMI:{} . Underweight'.format(str(bmi))
#    elif 18.5 <= bmi < 25 :
#       return 'BMI:{} . Normal'.format(str(bmi))
#    elif 25<= bmi < 30 :
#       return 'BMI:{} . Overweight'.format(str(bmi))   
#    else :
#       return 'BMI:{} . Obese'.format(str(bmi))

# if __name__ == '__main__':
#   app.run( debug=True)

# Way2

def height(weight,height):
   height_m = int(height)/100
   bmi = weight/(height_m**2) 
   return render_template("bmi.html", bmi = bmi)

if __name__ == '__main__':
    app.run(debug=True)