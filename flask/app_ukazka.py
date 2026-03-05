from flask import Flask, render_template

app = Flask(__name__) # název před route

@app.route('/1')
def home():
    return "Ahoj, světe od učitele!"

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

@app.route('/6', methods=['GET', 'POST']) # Předání formulářem z HTML do pythonu 
def prvniFormularCislo():
    result = None
    if request.method == 'POST':
        number = request.form.get('number', type=int) # přečti co je uložené v proměné number ze stránky HTML
        if number is not None:
            result = number + 1  # přičtení jedničky
    return render_template('index6.html', result=result)

if __name__ == '__main__':
    app.run()

