from flask import Flask, render_template, url_for
from flask_wtf import Flaskform
from wtforms import StringField,TextAreaField,PasswordField,SubmitField
from wtforms.validators import InputRequired,EqualTo,Length

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

class SignUpForm(FlaskForm):
    username=StringField(label="Username",validators=[InputRequired(message="Username should not be blank"),
    Length(min=5,max=25)])
    email=StringField(label="Email",validators=[InputRequired(message="Username should not be blank"),Length(max=45,
    message="Email should have less than 45 characters")
    ])
    password=PasswordField(label="Password", validators=[InputRequired(message="Password should not be left blank"),
    Length(min=5,max=12,message="password should be between 5 and 12 characters")
    ])
    confirm=PasswordField(label="Confirm Password", validators=[InputRequired(message="Password should not be left blank"),
    Length(min=5,max=12,message="password should be between 5 and 12 characters"),EqualTo('pasword',message="Passwords do not match")
    ])
    submit=SubmitField(label="Sign up")
    
    

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

@app.route()
def signup():
    form=SignUpForm()

    context={
        'form':form
    }
    return render_template('signup.html',**context)

@app.route('/contacts')
def contacts():

    title="contacts page"
    context={
        'title':title
    }
    return render_template('contacts.html', **context)

if __name__ == '__main__':
    app.run(debug=True)