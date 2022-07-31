from flask import Flask, render_template

app=Flask(__name__)

posts=[
    {
        'id':1,
        'title': 'what a good day',
        'content':'to mess around with flask'

    },
     {
        'id':2,
        'title': 'focus',
        'content':'your goals are limitless'

    },
     {
        'id':3,
        'title': 'speech',
        'content':'feel free to talk'

    },
     {
        'id':4,
        'title': 'IT',
        'content':'hard asf'

    }, 
    
]
@app.route('/')
@app.route('/index')
def index():

    title="Home page"
    
    context={
        'title':title,
    }
    return render_template('index.html', **context)

@app.route('/about')
def about():

    title="about page"
    context={
        'title':title
    }
    return render_template('about.html', **context)

@app.route('/login')
def login():

    title="login page"
    context={
        'title':title
    }
    return render_template('login.html', **context)

@app.route('/contacts')
def contacts():

    title="contacts page"
    context={
        'title':title
    }
    return render_template('contacts.html', **context)

if __name__ == '__main__':
    app.run(debug=True)