from flask import Flask, render_template_string

app = Flask(__name__)
CSS = '''
<style>
    body {
        font-family: Arial, sans-serif;
        text-align: center;
        background-color: #f0f0f0;
        margin: 0;
        padding: 0;
    }
    .container {
        padding: 20px;
        background-color: #fff;
        border-radius: 8px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        display: inline-block;
        max-width: 800px;
        margin-top: 20px;
    }
    img {
        max-width: 100%;
        height: auto;
        border-radius: 8px;
    }
    a {
        display: inline-block;
        margin: 10px;
        text-decoration: none;
        color: #007BFF;
        font-weight: bold;
    }
    a:hover {
        text-decoration: underline;
    }
    h1 {
        color: #333;
    }
    p {
        color: #666;
    }
</style>
'''

@app.route("/food1")
def food1():
    return render_template_string(f'''
    {CSS}
    <div class="container">
        <h1>Food Picture 1</h1>
        <img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.thefoodjoy.com%2Flamb-burgers-w-spicy-fries%2F&psig=AOvVaw2ZZXmqkfnyoLtzHHUXrunH&ust=1721377425167000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCMC4wOGUsIcDFQAAAAAdAAAAABAT" alt="Food Image 1">
        <a href="/food2">Next Food Pic</a>
        <a href="/home">Home</a>
    </div>
    ''')

@app.route("/food2")
def food2():
    return render_template_string(f'''
    {CSS}
    <div class="container">
        <h1>Food Picture 2</h1>
        <img src="https://images.squarespace-cdn.com/content/v1/65051c54e713d71d6acf3fba/6f433272-2489-4894-88b6-2e3341d5242c/20230720BarLucaandBLxKeraWongPhotography-460.jpg" alt="Food Image 2">
        <a href="/food3">Next Food Pic</a>
    </div>
    ''')

@app.route("/food3")
def food3():
    return render_template_string(f'''
    {CSS}
    <div class="container">
        <h1>Food Picture 3</h1>
        <img src="https://images.sbs.com.au/dims4/default/9a6b553/2147483647/strip/true/crop/2309x1299+0+0/resize/1280x720!/quality/90/?url=http%3A%2F%2Fsbs-au-brightspot.s3.amazonaws.com%2F35%2F98%2Fa86b7ba74a6ba67a6b313b1289e6%2Frx080-recipes-lara-burger-creditjiwonkim-tcus5-5.jpg" alt="Food Image 3">
        <a href="/home">Home</a>
    </div>
    ''')

@app.route("/pet1")
def pet1():
    return render_template_string(f'''
    {CSS}
    <div class="container">
        <h1>Pet Picture 1</h1>
        <img src="https://media.wired.com/photos/593261cab8eb31692072f129/master/pass/85120553.jpg" alt="Pet Image 1">
        <a href="/pet2">Next Pet Pic</a>
    </div>
    ''')

@app.route("/pet2")
def pet2():
    return render_template_string(f'''
    {CSS}
    <div class="container">
        <h1>Pet Picture 2</h1>
        <img src="https://i.pinimg.com/736x/0a/97/b9/0a97b9506033451140c9ff3b79172d9c.jpg" alt="Pet Image 2">
        <a href="/home">Home</a>
        <a href="/pet1">Previous Pet Pic</a>
        <a href="/pet3">Next Pet Pic</a>
    </div>
    ''')

@app.route("/pet3")
def pet3():
    return render_template_string(f'''
    {CSS}
    <div class="container">
        <h1>Pet Picture 3</h1>
        <img src="https://cdn.cnn.com/cnnnext/dam/assets/130819142015-cutest-animal-1-fennec-fox.jpg" alt="Pet Image 3">
        <a href="/pet2">Previous Pet Pic</a>
    </div>
    ''')

@app.route("/space1")
def space1():
    return render_template_string(f'''
    {CSS}
    <div class="container">
        <h1>Space Picture 1</h1>
        <img src="https://www.sciencefriday.com/wp-content/uploads/2023/03/pillars-of-creation-webb-min.png" alt="Space Image 1">
        <a href="/space2">Next Space Pic</a>
        <a href="/home">Home</a>
    </div>
    ''')

@app.route("/space2")
def space2():
    return render_template_string(f'''
    {CSS}
    <div class="container">
        <h1>Space Picture 2</h1>
        <img src="https://th-thumbnailer.cdn-si-edu.com/RyPIlp1ZzFFyPBcvDamP41k8R88=/1072x720/filters:no_upscale():focal(2362x1597:2363x1598)/https://tf-cmsv2-smithsonianmag-media.s3.amazonaws.com/filer_public/18/f4/18f4e941-b85b-45ae-b07c-52eaa6ca1f84/gettyimages-1237093074.jpg" alt="Space Image 2">
        <a href="/space3">Next Space Pic</a>
        <a href="/space1">Previous Space Pic</a>
    </div>
    ''')

@app.route("/space3")
def space3():
    return render_template_string(f'''
    {CSS}
    <div class="container">
        <h1>Space Picture 3</h1>
        <img src="https://media.wired.com/photos/5e961efdca6a5100098746f8/master/pass/space-human-body-backchhannel.jpg" alt="Space Image 3">
        <a href="/space2">Previous Space Pic</a>
    </div>
    ''')

@app.route("/home")
def home():
    return render_template_string(f'''
    {CSS}
    <div class="container">
        <h1>Welcome!</h1>
        <p>Welcome home!</p>
        <a href="/food1">Go to the first food photo!</a>
        <a href="/pet2">Go to the first pet photo!</a>
        <a href="/space1">Go to the first space photo!</a>
    </div>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
