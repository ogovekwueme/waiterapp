from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.login import login_required
from mockdbhelper import MockDBHelper as DBHelper
from user import User

DB = DBHelper()
app = Flask(__name__)

app.secret_key = 'i2QvD4cd4aAPjCampxPkjWliR0znwS9Y3ZC41jmPBlAFzBfiNf1mo0q9G/Iw0GtwCoxSjDz20Bdp4hICXs1RX5KvPwTDdZgrcHW'

login_manager = LoginManager(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/account")
@login_required
def account():
    return "You are logged in"


if __name__ == '__main__':
    app.run(port=5000, debug=True)


