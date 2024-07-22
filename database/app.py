from flask import Flask, render_template, request, redirect, session, url_for, flash
import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyBnVFeaD5wi2_gJrYxWqcwy-VPfW4dlgQA",
    "authDomain": "auth-lab-33f74.firebaseapp.com",
    "databaseURL": "https://auth-lab-33f74.firebaseio.com",
    "projectId": "auth-lab-33f74",
    "storageBucket": "auth-lab-33f74.appspot.com",
    "messagingSenderId": "696774828142",
    "appId": "1:696774828142:web:27352bfbbcf4fa37c2867f"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.create_user_with_email_and_password(email, password)
            session['user'] = user
            session['quotes'] = []
            flash('Account created successfully!', 'success')
            return redirect(url_for('home'))
        except Exception as e:
            flash(f"An error occurred: {e}", 'danger')
    return render_template('signup.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session['user'] = user
            session['quotes'] = []
            flash('Signed in successfully!', 'success')
            return redirect(url_for('home'))
        except Exception as e:
            flash(f"Invalid credentials: {e}", 'danger')
    return render_template('signin.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    if 'user' not in session:
        flash('Please sign in to access this page', 'warning')
        return redirect(url_for('signin'))

    if request.method == 'POST':
        quote = request.form['quote']
        session['quotes'].append(quote)
        flash('Quote submitted successfully!', 'success')
        return redirect(url_for('thanks'))
    return render_template('home.html')

@app.route('/thanks')
def thanks():
    if 'user' not in session:
        flash('Please sign in to access this page', 'warning')
        return redirect(url_for('signin'))
    return render_template('thanks.html')

@app.route('/display')
def display():
    if 'user' not in session:
        flash('Please sign in to access this page', 'warning')
        return redirect(url_for('signin'))

    quotes = session.get('quotes', [])
    return render_template('display.html', quotes=quotes)

@app.route('/signout')
def signout():
    session.pop('user', None)
    session.pop('quotes', None)
    flash('Signed out successfully!', 'success')
    return redirect(url_for('signin'))

if __name__ == '__main__':
    app.run(debug=True)
