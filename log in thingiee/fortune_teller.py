from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key' 

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        session['name'] = request.form['name']
        session['birth_month'] = request.form['birth_month']
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/home')
def home():
    name = session.get('name', 'Guest')
    return render_template('home.html', name=name)

@app.route('/fortune')
def fortune():
    birth_month = session.get('birth_month', '')
    month_length = len(birth_month)
    fortunes = ["yassa food for 3 years", "meat ur firs love again", "sari in ur room", "amor stealing my chair again", "meow moewowownewwwww ", "hating ppl u loved ", "the doors of luck are openong for you", "Prophecy", "ur gonna  get bankrubt", "kiddnaped by shalev untell u finish ur cs labs "]
    selected_fortune = random.choice(fortunes)
    return render_template('fortune.html', fortune=selected_fortune)

if __name__ == '__main__':
    app.run(debug=True)
