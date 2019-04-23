from flask import Flask
app = Flask(__name__)

Users = {
'huy' : {
	'name' : 'Nguyen Quang Huy',
	'age' : 29
    },
'tuananh' : {
	'name' : 'Huynh Tuan Anh',
	'age' : 22
    }
}

@app.route('/')
def index():
    return 'Optional'

@app.route('/user/<username>')
def user(username):
    if username in Users:
        user = Users[username]
        return str(user)
    else:
        return "user not found"
if __name__ == '__main__':
  app.run( debug=True)