from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
       
        birth_month = request.form.get('birth_month', '')
        
        return redirect(url_for('fortune', birth_month=birth_month))
   
    return render_template('home.html')

@app.route('/fortune')
def fortune():
   
    birth_month = request.args.get('birth_month', '')
    
    fortunes = ["Mysticism", "Augury", "Seer", "Divination", "Clairvoyance", "Tarot", "Astrology", "Prophecy", "Cartomancy", "Runes"]
    
    month_length = len(birth_month)
    index = month_length % len(fortunes)
    selected_fortune = fortunes[index]
    
    return render_template('fortune.html', lol=selected_fortune)

if __name__ == '__main__':
    app.run(debug=True)
