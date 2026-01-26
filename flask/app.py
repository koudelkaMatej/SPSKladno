from flask import Flask, render_template, url_for, request 
import os
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

@app.route('/6', methods=['GET', 'POST']) # Předání formulářem z HTML do pythonu 
def prvniFormularCislo():
    result = None
    if request.method == 'POST':
        number = request.form.get('number', type=int) # přečti co je uložené v proměné number ze stránky HTML
        if number is not None:
            result = number + 1  # přičtení jedničky
    return render_template('index6.html', result=result)

#vytvoreni slozky, kam budu ukladat nahrane soubory
app.config["UPLOAD_FOLDER"] = "ukazkovyFlask/static/uploadedFiles/"
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
@app.route('/7', methods=['GET', 'POST']) # Předání souboru
def deuhyFormFile():
    content = None
    if request.method == 'POST':
        file = request.files.get('file')
        if file and file.filename.endswith('.txt'):
            # Uložení souboru na disk
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(file_path)
            # Čtení obsahu souboru
            file.seek(0)  # Resetování pointeru souboru
            content = file.read().decode('utf-8')  # Přečti soubor jako text
    return render_template('index7.html', content=content)

import plotly.graph_objects as go
import plotly.io as pio
@app.route('/8')
def graph():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[1, 2, 3, 4], y=[10, 20, 25, 30], mode='lines+markers', name='Data 1'))
    fig.add_trace(go.Scatter(x=[1, 2, 3, 4], y=[15, 18, 22, 27], mode='lines+markers', name='Data 2'))

    fig.update_layout(
        title="Ukázkový interaktivní graf",
        xaxis_title="X-osa",
        yaxis_title="Y-osa",
        template="plotly_white"
    )
    # Převod grafu do HTML
    graph_html = pio.to_html(fig, full_html=False)
    return render_template("index8.html", graph_html=graph_html)

@app.route('/8_2')
def graphBar():
    # Data
    fruit = ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"]
    contestant = ["Alex", "Alex", "Alex", "Jordan", "Jordan", "Jordan"]
    number_eaten = [2, 1, 3, 1, 3, 2]

    # Unikátní soutěžící
    unique_contestants = list(set(contestant))

    # Inicializace grafu
    fig = go.Figure()

    # Přidání stop pro každého soutěžícího
    for current_contestant in unique_contestants:
        # Filtrace dat pro aktuálního soutěžícího
        x = [fruit[i] for i in range(len(fruit)) if contestant[i] == current_contestant]
        y = [number_eaten[i] for i in range(len(number_eaten)) if contestant[i] == current_contestant]

        # Přidání stop
        fig.add_trace(go.Bar(
            x=x, 
            y=y, 
            name=current_contestant,
            hovertemplate=f"Contestant={current_contestant}<br>Fruit=%{{x}}<br>Number Eaten=%{{y}}<extra></extra>"
        ))

    # Nastavení layoutu
    fig.update_layout(
        legend_title_text="Contestant",
        title="Number of Fruits Eaten by Contestants",
    )
    fig.update_xaxes(title_text="Fruit")
    fig.update_yaxes(title_text="Number Eaten")

    # Převod grafu do HTML
    graph_html = pio.to_html(fig, full_html=False)
    return render_template("index8.html", graph_html=graph_html)
