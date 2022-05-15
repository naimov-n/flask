from urllib import request

from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'a really really really really long secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:1@localhost:5432/flask_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer)
    group = db.Column(db.String(100), nullable=True)
    alias = db.Column(db.String(255), nullable=True)
    title = db.Column(db.String(255), nullable=True)
    short_content = db.Column(db.Text(), nullable=True)
    content = db.Column(db.Text(), nullable=True)
    status = db.Column(db.Boolean, default=True)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)


# @app.route('/home/')
# def index():
#     return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/get/<int:pk>', methods=['GET'])
def get(**kwargs):
    # car = Posts.query.all()
    # return car
    id = request.GET.get(kwargs.get('pk'))
    try:
        car = Posts.query.get(id=id)
        return render_template('index.html', cars=car, data={"name": "ulugbek"})

    except:
        return Respons(data={"error":"not fount"}, status=400)




if __name__ == '__main__':
    app.run(debug=True)