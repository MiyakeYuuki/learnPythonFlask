import os
from flask import Flask, render_template, request
from flask_login import UserMixin, LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# flask-loginのLoginManagerとflaskアプリの紐付け
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notoapp.db'
# app.config['SECRET_KEY'] = os.urandom(24)
# db = SQLAlchemy(app)

# login_manager = LoginManager()
# login_manager.init_app(app)


# DBのテーブルに対応するUserクラス


# class User(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), nullable=False, unique=True)
#     password = db.Column(db.String(25))

# 「/」へアクセスがあった場合に、"Hello World"の文字列を返す


@app.route("/")
def hello():
    return render_template("index.html")

# 「/templates」へアクセスがあった場合に、index.htmlを返す


@app.route("/templates", methods=["GET"])
def index():
    return render_template("next_index.html")

# 「/nextpage」へアクセスがあった場合に、next_index.htmlを返す


@app.route("/nextpage", methods=["GET"])
def nextpage():
    return render_template("next_index.html")

# チェックボックス処理


@app.route('/', methods=['POST'])
def post():
    name = request.form.getlist('checkbox')
    return render_template('index.html',
                           message='{}の観光地を以下に示します！'.format('と'.join(name)))


# app.pyをターミナルから直接呼び出した時だけ、app.run()を実行する
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
