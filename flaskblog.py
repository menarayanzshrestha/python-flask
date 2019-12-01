# from flask import Flask, escape, request
from flask import Flask, render_template, url_for

app = Flask(__name__) 
# __name__ is just a name of a module

posts = [
    {
        'author' : "Narayan Shrestha",
        'title' : "Blog post 1",
        'content': "First post",
        'date_posted' : "April 24, 2018"
    },
    {
        'author' : "Narayan ",
        'title' : "Blog post 1",
        'content': "First post",
        'date_posted' : "April 24, 2018"
    },
    {
        'author' : "Narayan Shrestha 1",
        'title' : "Blog post 12",
        'content': "First post2",
        'date_posted' : "April 24, 2019"
    }
]

@app.route('/') 
@app.route('/home') 
# decorator
def home():
    return render_template('home.html', posts=posts)

@app.route('/about') 
# decorator
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)