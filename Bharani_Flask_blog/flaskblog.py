from flask import Flask, render_template, url_for, flash, redirect
from forms import PostForm
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
date = datetime.now()
blogposts = [
    {
        'author': 'Bharani',
        'title': 'Football',
        'content': 'When will Bharani watch a live football match',
        'date_posted': date.strftime("%d/%m/%y")
    },
    {
        'author': 'Netra',
        'title': 'Linux',
        'content': 'Likes to uninstall a working version of linux and then break it with new',
        'date_posted': date.strftime("%d/%m/%y")
    },
    {
        'author': 'Brinda',
        'title': 'Food In India',
        'content': 'Likes to try out new dish',
        'date_posted': date.strftime("%d/%m/%y")
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=blogposts, title='Home')


@app.route("/post")
def posts():
    return render_template('posts.html',  posts=blogposts, title='Posts')


@app.route("/post_creation", methods=['GET', 'POST'])
def post_creation():
    form = PostForm()
    if form.validate_on_submit():
        flash('Your post is done')
        return redirect(url_for('home'))
    return render_template('post_creation.html', title='Post Creation', form=form, posts=posts)


if __name__ == '__main__':
    app.run(debug=True)
