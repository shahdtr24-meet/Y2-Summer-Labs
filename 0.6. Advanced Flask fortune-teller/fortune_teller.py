from flask import Flask , render_template
import random

app = Flask(__name__)
template_folder='templates',
static_folder='static'

@app.route('/home')
def home():

    return render_template('home.html')


@app.route('/fortune')
def fortune():
    fortunes=["Mysticism","Augury","Seer","Divination","Clairvoyance","Tarot","Astrology","Prophecy","Cartomancy","Runes"]
    lol= random.choice(fortunes)
    return render_template('fortune.html', lol=lol)
if __name__ == '__main__':
    app.run(debug=True)