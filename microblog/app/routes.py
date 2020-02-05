from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Krista'}
    posts =[
        {
            'author': {'username': 'Shaun'},
            'body': 'Beautiful Day in Denver'

        },
        {
            'author': {'username': 'Devin'},
            'body': 'The Eddie Murphy SNL Episode ROCKED!!!'
            
        },
        {
            'author': {'username': 'Nathan'},
            'body': 'Loving my new computer set up. Best birthday evah!'
        },
        {
            'author': {'username': 'Chris'},
            'body': 'Gotta love the bi-polar weather in Colorado.'
        }
    
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
