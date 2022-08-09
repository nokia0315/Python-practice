from datetime import datetime, date

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    detail = db.Column(db.String(100))
    due = db.Column(db.DateTime, nullable=False)

@app.before_first_request
def init():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        posts = Post.query.order_by(Post.due).all()
        return render_template('index.html', posts=posts, today=date.today())
    else:
        title = request.form.get('title')
        detail = request.form.get('detail')
        due = request.form.get('due')

        due = datetime.strptime(due, '%Y-%m-%d')
        new_post = Post(title=title, detail=detail, due=due)

        db.session.add(new_post)
        db.session.commit()

        flash('新しいリストを投稿しました。')
        return redirect('/')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/delete/<int:id>')
def delete(id):
    post = Post.query.get(id)
    
    db.session.delete(post)
    db.session.commit()
    flash('リストを削除しました。')
    return redirect('/')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    post = Post.query.get(id)
    if request.method == 'GET':
        return render_template('update.html', post=post)
    else:
        post.title = request.form.get('title')
        post.detail = request.form.get('detail')
        post.due = datetime.strptime(request.form.get('due'), '%Y-%m-%d')
        
        db.session.commit()
        flash('リストを編集しました。')
        return redirect('/')
        
@app.route('/detail/<int:id>')
def get_detail(id):
    post = Post.query.get(id)
    return render_template('detail.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)
