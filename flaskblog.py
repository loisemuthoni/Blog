from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask (__name__)

app.config['SECRET_KEY'] = '563fc69d972dc006577407e79a7953b2'

posts = [
    {
        'author': 'loise',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'dec 30 2019'
    },
    {
        'author': 'mso',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Jan 4 2019'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='about')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
       flash(f'Account created for {form.username.data}!', 'success')
       return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login_html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)