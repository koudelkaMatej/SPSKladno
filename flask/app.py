from flask import Flask, render_template, url_for
app = Flask(__name__) # název před route

@app.route('/')
def home():
    return "Ahoj, světe od učitele!"

@app.route('/1')
def pozdrav_returnem():
    return "Ahoj, světe od jedničky!"

@app.route('/2')
def pozdrav_ze_souboru():
    return render_template("index2.html")

@app.route('/3')
def pozdrav_ze_souboru_CSS():
    return render_template("index3.html")

@app.route('/4')
def pozdrav_z_promenny():
    text = "Ahoj z proměnné"
    return render_template("index4.html", message = text)

@app.route('/5') # Vložení obrázku do HTML z pythonu
def obrazek():
    image_url = url_for('static', filename='images/pan.png')  # cesta k obrázku
    #                         prvni je nazev v HTML druhý je název v pythonu
    return render_template('index5.html', image_url=image_url) 