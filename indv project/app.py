from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import pyrebase

app = Flask(__name__, template_folder='templetes', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

Config = {
    "apiKey": "AIzaSyBeMItHSFtF0ZBfQnL9VvYx0yoH0UIvLUU",
    "authDomain": "y2-indv-project.firebaseapp.com",
    "databaseURL": "https://y2-indv-project-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "y2-indv-project",
    "storageBucket": "y2-indv-project.appspot.com",
    "messagingSenderId": "307816602067",
    "appId": "1:307816602067:web:f7ff9d37f24bd124e43726"
}

firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()
db = firebase.database()

@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.create_user_with_email_and_password(email, password)
            session['user'] = user
            session['user_token'] = user['idToken']
            return redirect(url_for('home'))
        except Exception as e:
            error_message = str(e)
            return render_template('signup.html', error=error_message)
    return render_template('signup.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session['user'] = user
            session['user_token'] = user['idToken']
            return redirect(url_for('home'))
        except Exception as e:
            error_message = str(e)
            return render_template('signin.html', error=error_message)
    return render_template('signin.html')

@app.route('/signout')
def signout():
    session.clear()
    return redirect(url_for('signin'))

@app.route('/home')
def home():
    if 'user' in session:
        return render_template('home.html')
    else:
        return redirect(url_for('signin'))

@app.route('/profile')
def profile():
    if 'user' in session:
        user = session['user']
        user_id = user['localId']
        memes = db.child("memes").order_by_child("created_by").equal_to(user_id).get(session['user_token']).val()
        return render_template('profile.html', user=user, memes=memes)
    else:
        return redirect(url_for('signin'))

@app.route('/mememaker/<name>', methods=['GET', 'POST'])
def mememaker(name):
    if 'user' in session:
        if request.method == 'POST':
            meme_data = request.form.get('memeData')
            if meme_data:
                user = session['user']
                meme = {
                    'url': meme_data,
                    'created_by': user['localId'],
                    'name': name
                }
                db.child("memes").push(meme, session['user_token'])
                return redirect(url_for('profile'))
            else:
                return "Meme data is required", 400
        return render_template('mememaker.html', name=name)
    else:
        return redirect(url_for('signin'))

@app.route('/delete_meme/<meme_id>', methods=['POST'])
def delete_meme(meme_id):
    if 'user' in session:
        db.child("memes").child(meme_id).remove(session['user_token'])
        return redirect(url_for('profile'))
    else:
        return redirect(url_for('signin'))

if __name__ == '__main__':
    app.run(debug=True)
